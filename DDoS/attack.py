import requests

url = "http://167.172.2.112/python"
body = {'code': 'print("picante")\n\
i = 0\n\
i = i + 10\n\
print(i)',
'filename': 'aea',
'extension': 'py'}

for i in range(0,100):
    response = requests.post(url,data=body)
    #print(response.text)