import requests
from bs4 import BeautifulSoup

link = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=UAH&To=USD'

amount = input('Введите количество гривен для конвертации: ')

conv = {
    'Amount': amount,
    'From': 'UAH',
    'To': 'USD'
}

response = requests.get(link, conv)

soup = BeautifulSoup(response.content, 'html.parser')

result = soup.find('span', {'class': 'converterresult-toAmount'})

print(f'{amount} гривен = {result} долларов США')
print(result.text)

