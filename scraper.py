import requests
import pandas as pd
from bs4 import BeautifulSoup
import regex as re

urls = pd.read_csv('input.csv')

def getRandomProxy():
    proxy = {
    "http": f"http://scraperapi:4eb1d2723d0d2d978313010ba5ad69e6@proxy-server.scraperapi.com:8001",
    "https": f"http://scraperapi:4eb1d2723d0d2d978313010ba5ad69e6@proxy-server.scraperapi.com:8001"
    }

    return proxy


def extractArticles(articleUrl):
    resp = requests.get(articleUrl, proxies=getRandomProxy(), verify=False)
    soup = BeautifulSoup(resp.text, 'html.parser')

    global article_info
    article_info={
    'art_title' : soup.find('h1',{'class':'entry-title'}).text.strip(),
    'art_text' : soup.find('div',{'class':'td-post-content'}).text.strip()
    }
    
def main():
    articleUrl = urls['URL'][0]
    extractArticles(articleUrl)
    for i in range(0,urls.shape[0]+1):
        print(f"Running for article {i}")
        try:
            articleUrl_final = urls['URL'][i]
            extractArticles(articleUrl_final)
        except Exception as e:
            print(e)
        df = pd.DataFrame(article_info, index=[0])
        df.to_csv('Extracted_text\{}.txt'.format(i+37))
        
       
main()
