#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

kademe = input("Kademe seçiniz: ")
hafta = input("Hafta seçiniz: ")
kademe_url = str("https://www.ingilizceciyiz.com/"+kademe+"-sinif-ingilizce-gunluk-plan/")

# Requests URL and get response object
response = requests.get(kademe_url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')
print(links)

i = 0

for link in links:
    if ('.docx' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
    
    # Get response object for link
        response = requests.get(link.get('href'))

    # Write content in docx file
        docx = open("docx"+str(i)+".docx", 'wb')
        docx.write(response.content)
        docx.close()
    print("File ", i, " downloaded")

print("Downloaded")