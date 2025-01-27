import requests

def get_data(url):
    json_data = requests.get(url).json()
    return json_data
username = str(input('Введите имя пользователя для посика информации: '))
url = f'https://api.github.com/users/{username}/events'
data = get_data(url)
dic = []
c = 0
for elem in data:
    event_type = elem.get('type')
    repo_info = elem.get('repo')
    repo_name = repo_info.get('name')
    dic.append(event_type)
    dic.append(repo_name)
    dic.append('   ')

print(dic)
print(c)
