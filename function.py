'''import requests 
web_url = "https://nstidehradun.dgt.gov.in/"
response = requests.get(web_url)
response.headers
print(response.headers)
'''
'''
import requests
from bs4 import BeautifulSoup

def example ():
    url =  "https://nstidehradun.dgt.gov.in/"
    response = requests.get(url)

    if response.status_code == 200 :
        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.title.get_text()
        print(f"title of the page {title}")
    else :
        print(f"faild to recive page.statuscode:{response.status_code}")

if __name__ == "__main__":
    example()
'''
'''
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
div = (soup.find('div', class_="product_price"))
print(div.p.text)
'''

