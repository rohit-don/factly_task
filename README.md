--> Scraping

1.Requirements

- Python 3.x
- Scrapy
- BeautifulSoup
- requests
- certifi
- pandas

2. Installation

   a.Navigate to the `scrapy_task` directory:
     ```sh
     cd scrapy_task
     ```
   b. Install the required Python packages:
      ```sh
      pip install -r requirements.txt
      ```

      
3.Code:

Open the new python script in scrapy directory and write the code which,
I have given in the github file,Then save the file with py extension and 
go to the next step usage

    
4. Usage

Run the scraping script to download the PDF and Excel reports:
```sh
python scrapy.py
```
5.Output will be present in the file named cleaned_data.csv in the same directory 
  where you saved the python script

--> Cleaning:


1.Requirements

- pandas
- numpy

2. Installation

   a.Navigate to the `cleaning` directory:
   ```sh
   cd cleaning
   ```
   b. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3.Code
Open the new python script in cleaning directory and write the code which,
I have given in the github file,Then save the file with py extension and 
go to the next step usage

4. Usage

Run the scraping script to download the PDF and Excel reports:
```sh
python clean.py
```
5.Output will be present in the file named combined_table.csv in the same directory 
  where you saved the python script
