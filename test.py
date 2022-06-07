import os
import requests


if __name__ == '__main__':

    filepath = 'C:\\Users\\Damian\\IOMA\\Bitacora\\Junio\\Blur Study\\IMG-20220225-WA0004.jpg'
    server_url = 'http://127.0.0.1:5000/check'
    # server_url = 'http://127.0.0.1:5000/test'

    file_request = { 'file': (os.path.basename(filepath), open(filepath, 'rb'), f'image/{os.path.splitext(filepath)[1][1:]}') }

    response = requests.post(server_url, files=file_request, data={ 'blur_accepted': 400 })
    # response = requests.post(server_url, files=file_request)
    print(response.json())