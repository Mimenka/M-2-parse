import requests
from bs4 import BeautifulSoup
base_url = 'https://dominopizza.ru/'
response = requests.get(base_url, verify=False)
soup = BeautifulSoup(response.text, 'html')
zakuski = soup.find('div',{'id': 'zakuski'})
zakuski_col = zakuski.findAll('div',{'class': 'col'})
zakuski_list = []

for zakuski in zakuski_col:
    zakuski_content = zakuski.a.div.find('div',{'class':'product-card-content'})
    zakuski_content_name = zakuski_content.find('div', {'class': 'product-name'})
    zakuski_content_description = zakuski_content.find('div', {'class': 'description-container'})
    zakuski_content_price = zakuski_content.find('div', {'class': 'price'})
    # zakuski_pic = zakuski.a.div.find('div',{'class': 'product_picture'})
    zakuski_list.append({
        'name': zakuski_content_name.get_text(), 
        'descriptons': zakuski_content_description.get_text(),
        'price': zakuski_content_price.get_text(),
        # 'picture': zakuski_pic.get_text()
    })
print('Закуски')
for zakusk in zakuski_list:
    print('------------------------------')
    print(f'Название: {zakusk["name"]}')
    print(f'Состав: {zakusk["descriptons"]}')
    print(f'Цена: {zakusk["price"]}')
    print('------------------------------')