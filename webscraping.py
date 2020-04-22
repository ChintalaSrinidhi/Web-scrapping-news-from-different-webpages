from bs4 import BeautifulSoup as soup
import requests
l=['https://timesofindia.indiatimes.com/india','https://www.hindustantimes.com/top-news/','https://indianexpress.com/section/india/','https://www.thestatesman.com/']
k=['w_tle','media-heading','title','storybx-summary']
z=['span','div','h2','span']
h=["Times of India"," Hindustan Times","Indian Express","The Statesman"]
for i in range(len(l)):
    print(h[i])
    my_url=l[i]
    p=requests.get(my_url)
    s=soup(p.content,'html.parser')
    job=s.find_all(z[i],class_=k[i])
    c=0
    for i in job:
        c=c+1
        print(c)
        try:
            # print(i, end="n"*2)
            print(i.find('a').text)
            print(i.find('a').attrs['href'], end="\n" * 2)
            # print(i, end="n"*2)
        except:
            print("No hyperlinks")
            print(i.text)
        if c>20:
            break