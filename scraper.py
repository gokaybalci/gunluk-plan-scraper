import requests
from bs4 import BeautifulSoup

kademe = input("Kademe seçiniz: ")
hafta = input("Hafta seçiniz: ")
kademe_url = str("https://www.ingilizceciyiz.com/"+kademe+"-sinif-ingilizce-gunluk-plan/")

# Requests URL and get response object
response = requests.get(kademe_url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
   
eslesen_haftalar = soup.find_all(lambda tag: len(tag.find_all('a')) == 0 and hafta +". Hafta" in tag.text)

for link in eslesen_haftalar:
    if ('.docx' in link.get('href', [])):
        print("Dosya indiriliyor... ")
    
    # Get response object for link
        response = requests.get(link.get('href'))

    # Write content in docx file
        docx = open(kademe + ". Sınıf " + hafta + ". Hafta" + ".docx", 'wb')
        docx.write(response.content)
        docx.close()


print("İşlem tamamlandı.")