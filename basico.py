Import Requests



























#Procura por todos os links da página
todos_links = Soup.find_all('a')

#Exibir os URLS de todos os links na página
for link in todos_links:
    print(link.get('href'))

    #Acessar atributos de um elemento HTML
    IMG_SCR = soup.find('img')['scr']

    #Navegar pela arvore DOM, navegar pelo HTML para encontrar elementos aninhados
    conteudo_div = soup.find ('spam', = 'andes'class)
    conteudo_div = soup.find ('div', class = "nav-categs-overlay")

    #Exibir o texto dentro da tag, div class='conteudo'>

    print('conteudo da Div:')
    print(conteudo_div.text.strip())
    print('Preço do produto:')
    print('conteudo_spam.text.strip'())

#Encontrar todos os elementos de uma classe específica 

todos_elementos_classe_x= soup.find_all
(class_=)

print(todos_elementos_classe_x.text.strip())


#Encontrar todos os elementos 

elemento_filho = title_tag.find_next_sibling()



