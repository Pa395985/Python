import requests
from bs4 import BeautifulSoup

def pesquisar_no_mercado_livre():
    #solicitar uma pesquisa do usuário
    #produto_pesquisa= input(""))

    produto_pesquisa= produto_pesquisa.repalce
    ('', '+')

    #URL de pesquisa do Mercado Livre

    url= f'https://lista.mercadolivre.com.br/
    {produto_pesquisa}'

    #Enviar uma solicitação GET para a página de pesquisa

    response= requests.get(url)

    #Verificar se a solicitação foi bem sucedida (código status 200)

    if response.status_code == 200:
       #criar um objeto BeautifulSoup para analisar o conteúdo da página de pesquisa do usuário
       soup = BeautifulSoup(response.text,'html.parser')

       #Encontrar todos elementos HTML correspondentes a pesquisa
       
resultados = soup.find.all ('li, class = 'ul-searche layout_item')
                            
                           
                           #Exibir informações sobre os primeiros resultados

                           for resultado in resultados[:5]: #Exibir os 5 primeiros resultados
                           
                           nome_produto =resultado.find(h2,class = 'ui search-item_title').text
                           preco_produto = resultado.Find
                           




