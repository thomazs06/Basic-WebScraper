import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv  # For improved CSV readability

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})

    rows = []

    headers = table.find_all('th')
    header = [header.get_text(strip=True) for header in headers[:8]] 
    rows.append(header)

    data_rows = table.find_all('tr')[1:] 
    for row in data_rows:
        cols = row.find_all('td')
        if len(cols) >= 7:  
            cols_data = [col.get_text(strip=True) for col in cols[:8]]  
            rows.append(cols_data)

    df = pd.DataFrame(rows[1:], columns=rows[0])

    df = df.drop(columns=[col for col in df.columns if 'Ref.' in col], errors='ignore')

    # Save the DataFrame to a CSV file with improved readability
    df.to_csv('largest_companies_by_revenue.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

    print("Data has been scraped and saved to 'largest_companies_by_revenue.csv'.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

