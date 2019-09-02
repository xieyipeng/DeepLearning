import requests

'''
ssm 发送get请求
'''

url = "http://localhost:8080/monitor/findRecently.do"
r = requests.get(url)
print(r.json())
