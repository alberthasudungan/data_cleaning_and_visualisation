#import web parsing sets
from bs4 import BeautifulSoup
import pandas as pd
import html5lib

#define tables of url
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

#reading the table datasets
dfs = pd.read_html(url)

#displaying the table  
type(dfs)

#extract the data from the website 
dfs

#Analysing historical total numbers of failures per year
failures.head()
close_timestamps = pd.to_datetime(failures['Closing Date'])
close_timestamps.dt.year.value_counts()
