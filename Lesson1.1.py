import requests
import json
username = 'Nolalala310'
link = f'https://api.github.com/users/{username}/repos'
req = requests.get(link)

if req.ok:
    data = json.loads(req.text)
    list = []
    for i in data:
        list.append(i['name'])
    print(f'Названия репозиториев пользователя: {list}')





