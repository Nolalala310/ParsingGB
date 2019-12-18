#Выполнить запрос методом GET к ресурсам, использующим любой тип авторизации через Postman, Python.
import requests
import json

username = 'Nolalala310'
password = '' #Персональный токен
link = f'https://api.github.com/user'
req = requests.get(link, auth=(username, password))
print(req.status_code)
