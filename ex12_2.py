import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position:'))
lista=list()
tamanho=0

print(url)

while count > 0:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags=soup('a')
          
    for tag in tags:

    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
        lista.append(tag.get('href', None))
    #print(url)
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)


    url = (lista[tamanho+position-1])
    print(url)
    tamanho = len(lista)
    count = count - 1

