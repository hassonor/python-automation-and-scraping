import pandas

url_sheet_1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
url_sheet_2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"

data_1 = pandas.read_csv(url_sheet_1)
print(data_1)

data_2 = pandas.read_csv(url_sheet_2)
print(data_2)
