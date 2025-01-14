import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.adopteunbureau.fr/'


def get_text_if_not_none(e):
    if e:
        return e.text.strip()
    return None


##########################################################
# On récupère les liens de page de toutes les catégories #
##########################################################
response = requests.get(url)
response.encoding = response.apparent_encoding
categorie_page_links = []
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html5lib")
    # On récupère l'ensemble des éléments contenant les catégories
    categorie_lists = soup.find_all("li", class_="child-menu-mega")
    for categorie_list in categorie_lists:
        # On récupère la liste des composants cliquable des catégories
        a_categorie = categorie_list.find_all("a")
        # On récupère les liens et les nom des catégories
        for a_tag in a_categorie:
            text = a_tag.text.strip()
            href = a_tag.get("href")
            categorie_page_links.append((text, href))
else:
    print("ERREUR : ", response.status_code)
# On filtre les catégories
title_to_exclude = [
    'Fauteuils de bureau',
    'Chaises et autres assises',
    'Rangements',
    'Bureaux et benchs',
    'Tables',
    'Accessoires',
    'Herman Miller',
    'Herman Miller Aeron',
    'Herman Miller Mirra',
    'Herman Miller Sayl',
    'Herman Miller Lino',
    'Herman Miller Cosm',
    'Steelcase',
    'Steelcase Please',
    'Humanscale',
    'USM Haller',
    'Vitra'
]
categorie_page_links = list(set(categorie_page_links))
categorie_page_links = [
    item for item in categorie_page_links if item[0] not in title_to_exclude
]
##########################################################
# On récupère les liens des page des produits            #
##########################################################
# for link in categorie_page_links:
product_links = []
# for page in categorie_page_links:
page = categorie_page_links[0]
for i in range(10):  # de 0 à 9
    j = i+1
    url = page[1] + "page/" + str(j) + "/"
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        html = response.text
        # f = open("page" + str(j) + ".html", "w")
        # f.write(html)
        # f.close()
        soup = BeautifulSoup(html, "html5lib")
        produits = soup.find_all("div", class_="porto-tb-item")
        if not produits:
            print(f"Indice i : {j}")
        else:
            for produit_link in produits:
                stock = produit_link.find("a")
                f = open("page.html", "w")
                f.write(stock.text)
                f.close()
                href = stock.get("href")
                product_links.append(href)

# categories_json = [{"url": url} for url in produit_link]
# with open("categories.json", "w", encoding="utf-8") as fichier:
#    json.dump(categories_json, fichier, ensure_ascii=False, indent=4)
##########################################################
# On récupère les infos des produits                     #
##########################################################
products_infos = []
for product_link in product_links:
    response = requests.get(product_link)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        product_infos = []
        html = response.text
        # f = open("page" + str(j) + ".html", "w")
        # f.write(html)
        # f.close()
        soup = BeautifulSoup(html, "html5lib")
        # On récupère le titre
        title = soup.find("h2", class_="product_title").text
        # On récupère le prix
        span_class = soup.findAll("span", class_="woocommerce-Price-amount")
        price = span_class[1].find("bdi").text
        # On récupère le stock
        stock_p = soup.find("p", class_="in-stock")
        if stock_p:
            stock = stock_p.text
        # On récupère les photos
        images_div = soup.find("div", class_="product-thumbs-vertical-slider")
        images_links = images_div.findAll("img", class_="img-responsive")
        # On récupère la description du produit
        desc_div = soup.find("div", class_="tab-content")
        # On créer un tableau avec toutes les infos
        i = [title, price, stock,[img.get("src") for img in images_links], desc_div]
        products_infos.append(i)
#print(products_infos)

# On récupère le titre
# titre = soup.find("h1").text
# print(titre)
# On récupère le prix
# description = soup.find(
#    "span", class_="ht_tax").find("bdi").text
# print(description)
# On récupère les dimensions
# e_dimensions = soup.find_all("tr", class_="porto-attr-data")
# for e_dimension in e_dimensions:
#    dim = e_dimension.find("th").text + e_dimension.find("td").text
#    print(dim)
print("FIN")
