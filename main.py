import random


chars = "1234567890QWERTYJKLZXCVBNMqwertyuzxcvbnm@#%&/?"
symbols = list(chars)

n = int(input('Введите длину пароля: '))

password = ''

for i in range(n):
	password += random.choice(symbols)

print(password)