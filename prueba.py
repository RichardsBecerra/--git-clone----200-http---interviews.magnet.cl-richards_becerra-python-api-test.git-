import requests

if __name__ == '__main__':
    url = 'https://www.google.com'
    response = requests.get(url)

    if response.status_code == 200:
        #print(response.content) este nos permitiria ver el contenido en el terminal 
        content = response.content

        file = open('google.html', 'wb')
        file.write(content)
        file.close() #esta funcion me guardo el contenido de la url en un archivo html

