import requests

def get_data(url):
    json_data = requests.get(url).json()
    return json_data

while True:
    username = str(input('Введите имя пользователя для поиска информации: '))
    url = f'https://api.github.com/users/{username}/events'
    data = get_data(url)
    if not(isinstance(data, list)):
         print("Не удалось получить данные от пользователя")
    else:
        break
dic ={'PushEvent':[],
      'CreateEvent':[],
      'DeleteEvent':[],
      'ForkEvent':[],
      'ReleaseEvent':[],
      'WatchEvent':[]}
for elem in data:
    event_type = elem.get('type')
    if not event_type:
        continue
    repo_info = elem.get('repo')
    if not repo_info:
        continue
    repo_name = repo_info.get('name')
    if not repo_name:
        continue
    if event_type in dic:
        type_array = dic.get(event_type)
        if event_type != 'PushEvent':
            if repo_name not in type_array:
                type_array.append(repo_name)
                dic[event_type] = type_array
        else:
            type_array.append(repo_name)
            dic[event_type] = type_array
for key in dic:
    if dic.get(key):
        if key == 'PushEvent':
            push_array = dic.get('PushEvent')
            while push_array:
                elem0 = push_array[0]
                c = 0
                for elem in push_array:
                    if elem0 != elem:
                        break
                    c+= 1
                print(f'Пользователь отправил {c} commits в репозиторий {elem0}.')
                push_array = push_array[c:]
        if key  == 'CreateEvent':
            create_array = dic.get('CreateEvent')
            while create_array:
                print(f'Пользователь создал {create_array[0]}.')
                create_array.pop(0)
        if key == 'DeleteEvent':
            delete_array = dic.get('DeleteEvent')
            while delete_array:
                print(f'Пользователь удалил {delete_array[0]}.')
                delete_array.pop(0)
        if key == 'ForkEvent':
            fork_array = dic.get('ForkEvent')
            while fork_array:
                print(f'Пользователь создал копию (fork) {fork_array[0]}.')
                fork_array.pop(0)
        if key == 'ReleaseEvent':
            release_array = dic.get('ReleaseEvent')
            while release_array:
                print(f'Пользователь создал релиз в {release_array[0]}.')
                release_array.pop(0)
        if key == 'WatchEvent':
            watch_array = dic.get('WatchEvent')
            while watch_array:
                print(f'Пользователь начал отслеживать {watch_array[0]}.')
                watch_array.pop(0)
