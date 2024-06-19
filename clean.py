import pandas as pd
import numpy as np
# Load the Excel reports for 2014-15 and 2015-16
report_2014_15 = pd.ExcelFile('/Users/rohittanuku/Downloads/AISHE2014-15.xlsx')
report_2015_16 = pd.ExcelFile('/Users/rohittanuku/Downloads/AISHE2015-16.xlsx')

# Clean the tables
def clean_table(report):
    sheet_names = report.sheet_names
    tables = []
    for sheet_name in sheet_names:
        table = report.parse(sheet_name)
        # Clean table
        table.dropna(how='all', axis=0, inplace=True)
        table.dropna(how='all', axis=1, inplace=True)
        table.columns = [col.strip().lower().replace(' ', '_') for col in table.columns]
        table.reset_index(drop=True, inplace=True)
        table.fillna(np.nan, inplace=True)
        tables.append(table)
    return tables

table_2014_15 = clean_table(report_2014_15)
table_2015_16 = clean_table(report_2015_16)

# Combine tables
combined_table = pd.concat(table_2014_15 + table_2015_16, ignore_index=True)

# Save the combined table to a CSV file
combined_table.to_csv('combined_table.csv', index=False)