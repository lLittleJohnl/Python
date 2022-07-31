# Informaçãos de http://matematicamuitofacil.com/robots.txt
# User-agent: *
# Disallow: /cgi-bin/
# Disallow: /wusage

import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://matematicamuitofacil.com/index.html") as url:
    page = url.read()

#print(page)

# Após extração realizei a formatação do arquivo html

soup = BeautifulSoup(page, "html.parser")

print(soup.title.string)
#print(soup.find_all("a"))