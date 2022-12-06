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
#links = soup.find(text=[hafta + "hafta"])
#print(links)

                
                    
matched_tags = soup.find_all(lambda tag: len(tag.find_all('a')) == 0 and hafta +". Hafta" in tag.text)

for matched_tag in matched_tags:
       print("Matched:", matched_tag)


for link in matched_tags:
    if ('.docx' in link.get('href', [])):
        print("Downloading file: ")
    
    # Get response object for link
        response = requests.get(link.get('href'))

    # Write content in docx file
        docx = open(kademe + ". Sınıf " + hafta + ". Hafta" + ".docx", 'wb')
        docx.write(response.content)
        docx.close()
    print("File downloaded")

print("Finish")