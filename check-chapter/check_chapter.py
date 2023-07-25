import requests

item_url = "http://volonte-d.com/"
response = requests.get(item_url, verify=False)

chapter_id=1089
if 'Chapitre 1088' in response.text:
    print('Le chapitre est sorti')
else:
    print('Le chapitre n\'est pas sorti')
