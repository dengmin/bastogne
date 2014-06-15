from base64 import b64encode, b64decode

url = 'http://www.baidu.com'

a = b64encode(url.encode())

print(a.decode())

print(b64decode(a).decode())
