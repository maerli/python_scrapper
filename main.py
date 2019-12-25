import requests
from bs4 import BeautifulSoup
link = "https://news.google.com/search?q=acara%C3%BA&hl=pt-BR&gl=BR&ceid=BR:pt-419"
f = requests.get(link)
html = f.text
soup = BeautifulSoup(html,'html.parser')

dados = []

for article in soup.find_all('article'):
	title = article.h3.text
	url = article.a.get('jslog').split(';')[1]
	url = url.replace('2:http','http')
	dados.append("<a onclick=\"window.location.href='http://legeerook.com/24K7'\" href=\""+url+"\" target=\"top\">"+title+"</a><br>\n")
file = open("index.html","w")

news = """
	<html>
	<head>
		<meta charset="utf8">
		<meta name="description" content="Notícias de Baixo Vale Acaraú">
		<meta name="keywords" content="notícias,acaraú,ceará,brasil,bela cruz,cruz">
		 <meta name="viewport" content="width=device-width, initial-scale=1.0">
		 <meta name="author" content="Marcos Maerli Pereira">
		<style>
			body{
				padding:10px;
				margin:10px;
			}
			a{
				color:black;
				font-weight:bold;
				padding:10px;
				border:1px solid black;
				text-decoration:none;
				outline:none;
				display:block;
				border-radius:10px;
			}
		</style>
	</head>
	<body>
		<div class="container">
			%s
		</div>
	</body>
	</html>
"""%("\n".join(dados))

file.write(news)
file.close()