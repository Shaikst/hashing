import urllib.request
import json
response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/Hashing_dictionary.json")
hashing = json.loads(response.read().decode('utf-8'))
print("██████╗░███████╗██╗░░░██╗░░░░░██╗███████╗██████╗░\n██╔══██╗██╔════╝██║░░░██║░░░░░██║██╔════╝██╔══██╗\n██║░░██║█████╗░░╚██╗░██╔╝░░░░░██║█████╗░░██████╦╝\n██║░░██║██╔══╝░░░╚████╔╝░██╗░░██║██╔══╝░░██╔══██╗\n██████╔╝███████╗░░╚██╔╝░░╚█████╔╝███████╗██████╦╝\n╚═════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚══════╝╚═════╝░")
print("Разработанно DevJeb, испольуется 64-ая система")
a=input('Введите текст: ')
b=list(a)
result=""
for s in b:
    result+=hashing[s]
print('Хэшированные данные:\n\n\n' + result)