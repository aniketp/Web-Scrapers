import requests
from bs4 import BeautifulSoup

# function to scrape the main web-page
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://github.com/sakshamsharma?page=' + str(page) +'&tab=repositories'
        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.findAll('a',{'itemprop':'name codeRepository'}):
            href = 'https://github.com' + link.get('href')
            title = link.string

            # passing the link and title to the function which scrapes further into the webpage
            get_about_data(href,title)
            
        page += 1


def get_about_data(repo_url,title):
    source_code = requests.get(repo_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")

    # Prints out the further detail of the items
    for about in soup.findAll('span',{'itemprop':'about'}):
        print(str(title) + ' - ' + str(about.string))        
            
trade_spider(3)

