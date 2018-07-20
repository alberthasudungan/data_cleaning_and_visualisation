#import web scrapper library 
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = =[your chrome driver pathway]

#declare chrome driver pathway
print(chrome_driver_path)

#create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)

#Navigate to the application home page
driver.get([website you want to extract the data])
elmt = driver.find_element_by_css_selector("#quote-header-info > div:nth-child(3) > div > div > span:nth-child(1)")

print(elmt.text)

tbl_selector = "#Col1-1-HistoricalDataTable-Proxy > section > div:nth-child(2) > table > tbody > tr"

tbody_elmt = driver.find_elements_by_css_selector(tbl_selector)

print(len(tbody_elmt))

td_val = ""

for tr_elmt in tbody_elmt:
    td_elmts = tr_elmt.find_elements_by_tag_name("td")
    #print(len(td_elmts))
    
    for td_elmt in td_elmts:
        td_val += td_elmt.text + ", "
        print(td_val)

driver.quit()
