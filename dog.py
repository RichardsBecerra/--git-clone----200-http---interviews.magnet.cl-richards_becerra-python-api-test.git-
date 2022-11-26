import requests

if __name__ == '__main__':
    url = 'http://dogs.magnet.cl/api/v1/breeds/'
    response = requests.get (url)

    if response.status_code == 200:
        print(response.content)


if __name__ == '__main__':
    url = 'http://dogs.magnet.cl/api/v1/auth/'
    payload = { 'email' : 'email', 'password' : 'password'}

    response = requests.post(url, json=payload)
    print(response.url)

    if response.status_code == 200:
        print(response.content)