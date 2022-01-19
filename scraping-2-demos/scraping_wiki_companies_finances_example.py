import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def scrap_wiki_html_by_search(to_search):
    # Download and parse the HTML
    start_url = f'https://en.wikipedia.org/wiki/{to_search}'

    # Download the HTML from start_url
    downloaded_html = requests.get(start_url)

    # Parse the HTML with BeautifulShop and create a soup object
    soup = BeautifulSoup(downloaded_html.text, features="lxml")

    full_table = soup.select('table.wikitable')[0]

    table_columns = extract_columns(full_table)
    table_data = extract_rows(full_table)

    # Create a Pandas DataFrame
    df = pd.DataFrame(table_data, columns=table_columns)
    print(df)
    df.to_csv(f'assets/{to_search}_finances_from_wiki.csv', encoding='utf-8')
    # Save a local copy
    # with open(f'assets/wiki_downloaded_{to_search}.html', 'w', encoding="utf-8") as file:
    #     file.write(soup.prettify())


def extract_columns(full_table):
    # Extract the table column headings
    # End result: A list with all the column headings
    table_head = full_table.select('tr th')
    table_columns = []
    regex = re.compile('_\[\w\]')

    for element in table_head:
        column_label = element.get_text(separator=" ", strip=True)
        column_label = column_label.replace(' ', '_')
        column_label = regex.sub('', column_label)
        table_columns.append(column_label)

    return table_columns


def extract_rows(full_table):
    # Extract the table data (rows)
    # End result: A multi-dimensional list containing a list for each row

    table_rows = full_table.select('tr')

    table_data = []
    for index, element in enumerate(table_rows):
        if index > 0:
            row_list = []
            values = element.select('td')
            for value in values:
                row_list.append(value.text.strip())
            table_data.append(row_list)

    return table_data


# Getting Finances data by years :-)
scrap_wiki_html_by_search('BMW')
scrap_wiki_html_by_search('Netflix')
