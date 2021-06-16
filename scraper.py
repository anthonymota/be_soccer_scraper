import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

url="https://www.besoccer.com/livescore"


page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
h=[]
results=soup.findAll('a',class_='match-link')
texs=""
print('\n')
k=""
for a in results:
    all=[]
    for div in a.children:
        try:
            if 'info-head' not in div['class'] and 'date-transform' not in div['class']:
                texs=div.text
                all.append(" ".join(texs.split()).replace('\n',''))
        except:
            pass

    h.append(all)        

for i in h:
    k+=str(i)
    k=k.replace('[','').replace(']','')
    k+="\n"

print(k)

msg=EmailMessage()
msg.set_content(k)


s=smtplib.SMTP('smtp.mail.yahoo.com',587)
s.starttls()
s.login('anthony.mota5','avhelxpbtdsfkfem')
s.sendmail('anthony.mota5@yahoo.com',"anthony.mota5@yahoo.com",str(msg))
s.quit()