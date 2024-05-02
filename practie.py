import requests

api_key = 'b2e42df9-6955-42fc-8032-6505e47c811b'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()
 
for definition in definitions:
    print(definitions)