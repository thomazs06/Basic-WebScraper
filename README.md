# List of largest companies by revenue - Web Scraping 🏨

## **Overview**
This project is a Python script that scrapes the largest companies by revenue from Wikipedia. The script extracts relevant data and saves it into a CSV file for easy access and analysis.

⚠ **This project is for educational purposes only.** ⚠

## **Objectives** 🎯
- Scrape the largest companies by revenue based on the **Fortune Global 500** list.
- Format the data into a structured CSV file.
- Provide a clear and organized way to showcase the extracted data.

## **Technologies Used** 👨‍💻
- **Python**: The primary programming language used for the web scraping.
- **BeautifulSoup**: A library for parsing HTML and XML documents. It is used to extract data from the webpage.
- **Pandas**: A data manipulation and analysis library that helps in creating and managing DataFrames.
- **Requests**: A simple HTTP library for making requests to web pages.

## **How It Works** ⚒
1. **Fetch the Webpage**: The script sends a GET request to the Wikipedia URL containing the list of largest companies by revenue.
2. **Parse the HTML**: Using BeautifulSoup, the script parses the HTML content to find the relevant table.
3. **Extract Data**: The script retrieves the headers and data from the table and stores them in a list.
4. **Create DataFrame**: The extracted data is converted into a Pandas DataFrame for easy manipulation.
5. **Save to CSV**: The DataFrame is then saved as a CSV file with improved readability settings.

## **Installation** 🔧
To run this script, make sure you have Python installed on your machine. You will also need to install the necessary libraries. You can do this using pip:

```bash
pip install requests beautifulsoup4 pandas
