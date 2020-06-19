import requests
import pandas as pd
from  bs4 import BeautifulSoup

pages=[]
titles=[]
prices=[]
rating=[]

entry= {'titles' : titles, 'prices' : prices, 'ratings' : rating, 'pages' : pages}
count_page=1
for i in range(1, count_page+1):         # to extract all the pages  
    url = 'http://books.toscrape.com/catalogue/page-'+ str(i) +'.html'
    pages.append(url)
##print(pages)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    #(soup.prettify())

    for i in soup.find_all('h3'):
        ttl = i.getText()
        titles.append(ttl)
    
    for i in soup.find_all('p' , class_='price_color'):
        rates = i.getText()
        prices.append(rates)
    
    for i in soup.find_all('p' , class_='star-rating'):
        for k,v in i.attrs.items():
            #print(k,v)
            star=v[1]
            rating.append(star)
    
    div = soup.find_all('div', class_='image_container')
    for thumb in div:
        tgs= thumb.find_all('img', class_='thumbnail')
        #url= 'http://books.toscrape.com/' + str(tgs['src'])
       # print(url)
    

df= pd.DataFrame.from_dict(entry, orient='index')
df.index+=1
df.transpose()
df.to_excel('output')                      #convert the data sheet to excel file
print(df)
print('export to excel !!!')



         

