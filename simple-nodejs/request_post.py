import requests

headers = {
    # Already added when you pass json=
    # 'content-type': 'application/json',
}

json_data = {
    "msg": "testing",
}

response = requests.post("http://localhost:8000/test", headers=headers, json=json_data)


print(response.status_code)

import json
from pprint import pprint

pprint(response.json())