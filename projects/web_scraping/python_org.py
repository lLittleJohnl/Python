# Biblioteca usada para requisitar um página web
import urllib.request
# Biblioteca usada para quebrar a página html pelas tags
from bs4 import BeautifulSoup
# Definição da url
with urllib.request.urlopen("https://www.python.org") as url:
    page = url.read()
# Imprime a página
print(page)
# Chamada da função
soup = BeautifulSoup(page, "html.parser")
# Busca a tag title e imprime
soup.title
# Busca a tag title e imprime como string
soup.title.string
# Tag a define um hiperlink
soup.a
# Buscando todos os hiperlinks da página
soup.find_all("a")