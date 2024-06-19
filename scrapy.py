import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urljoin, urlparse
import certifi

# Scrape PDF and Excel reports from AISHE website
def scrape_reports():
    base_url = "https://www.education.gov.in/statistics-new?shs_term_node_tid_depth=384"
    response = requests.get(base_url, verify=certifi.where())
    soup = BeautifulSoup(response.content, 'html.parser')
    reports = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and (href.endswith('.pdf') or href.endswith('.xlsx')):
            reports.append(urljoin(base_url, href))
    return reports

# Download reports
def download_reports(reports):
    for report in reports:
        try:
            response = requests.get(report, stream=True, verify=certifi.where())
            response.raise_for_status()
            file_name = os.path.basename(urlparse(report).path)
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {report}: {e}")

# Extract tables from Excel reports
def extract_tables(reports):
    tables = []
    for report in reports:
        if report.endswith('.xlsx'):
            try:
                file_name = os.path.basename(urlparse(report).path)
                df = pd.read_excel(file_name, sheet_name=None)
                if isinstance(df, dict):
                    for sheet_name, sheet_df in df.items():
                        tables.extend([sheet_df.iloc[i:i+1] for i in range(len(sheet_df))])
                else:
                    tables.extend([df.iloc[i:i+1] for i in range(len(df))])
            except Exception as e:
                print(f"Error extracting tables from {report}: {e}")
    return tables

# Clean and combine tables
def clean_and_combine_tables(tables):
    # Clean tables
    for table in tables:
        table.columns = [col.strip().lower().replace(' ', '_') for col in table.columns]
        table.dropna(inplace=True)
        table.drop_duplicates(inplace=True)
    
    # Combine tables
    combined_table = pd.concat(tables, ignore_index=True)
    return combined_table

# Main function
def main():
    reports = scrape_reports()
    download_reports(reports)
    tables = extract_tables(reports)
    cleaned_table = clean_and_combine_tables(tables)
    cleaned_table.to_csv('cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()