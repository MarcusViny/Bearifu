import requests
from bs4 import BeautifulSoup  # Serve só para paginas que nao seja dinamica que nao mude os inputs

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" }
      
link = "https://www.google.com/search?q=find+all+files+in+directory+python "

requisicao = requests.get(link,headers=headers)
print(requisicao)
#print(requisicao.text)
site = BeautifulSoup (requisicao.text,"html.parser")
#titulo = site.find("title") #find somente para algo especifico 
#pesquisa = site.find_all("input") #find_all serve para fazer a pesquisa de todos os campos como ("input") aparecera todos posso selecionar um por cochetes [0] ;
pesquisa = site.find_all("span")
print(pesquisa)



