from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("/Users/akulsharma/Desktop/chromedriver_mac64/chromedriver")
browser.get(START_URL)

time.sleep(10)

stars_data = []

# Define Star Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        #BeautifulSoup object
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #loop to find all the elements
        for ul_tag in soup.find_all("ul",attrs={"class", "star"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
        #find all elements on the page
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        
        



        
# Calling Method    
scrape()

# Define Header
headers = ["star_name", "distance", "planet_mass", "radius", "luminosity"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(stars_data, columns = headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
    


