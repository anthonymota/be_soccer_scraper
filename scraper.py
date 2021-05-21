import requests
from bs4 import BeautifulSoup

url="https://www.besoccer.com/livescore/2021-05-20"


page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
all=[]

results=soup.findAll('a',class_='match-link')
texs=""

for a in results:
    for div in a.children:
        try:
            texs=div.text
            all.append(" ".join(texs.split()).replace('\n','').replace('EndFull time','').replace('End Group D. MD 5','').replace('DAZN,ESPN',''))
            print(all)
            print('\n')
            print('\n')
        except:
            pass


print(all)