import requests

content_resource = requests.get('https://api.github.com/users/danilocgsilva/repos')
print(type(content_resource.json()))