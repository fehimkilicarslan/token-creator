import jwt
import pyperclip


key = input("input your secret key:\n")

passwd = input("input your password:\n")

payload = {'pwd': passwd}

token = jwt.encode(payload, key, algorithm='HS256')

pyperclip.copy(token)

print('The token to be copied to the clipboard.')
