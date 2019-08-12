#importing dependencies
import bs4
from urllib.request import urlopen as uQuest
from bs4 import BeautifulSoup as scraper

#accessing the web page to scraped
url_copy = "https://www.imdb.com/"
client = uQuest(url_copy)
html_code = client.read()
client.close()

#parsing the webpage
with open('scraping101.csv','w') as csv_file:
        scraped = scraper(html_code, "html.parser")
        container = scraped.findAll(class_="trending-list-rank-item")
        for element in container:
                #scraping rank, name and %popularity from the dattabase
                rank=element.find(class_="trending-list-rank-item-rank-position").text
                name=element.find(class_='trending-list-rank-item-name').text
                share=element.find(class_='trending-list-rank-item-share').text
                csv_file.write(rank+","+name+","+share+"\n")
        
