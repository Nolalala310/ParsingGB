#Выполнить запрос методом GET к ресурсам, использующим любой тип авторизации через Postman, Python.
import requests
import os

username = 'Nolalala310'
password = os.environ['TOKEN_GITHUB']
link = f'https://api.github.com/user'
req = requests.get(link, auth=(username, password))
print(req.status_code)
