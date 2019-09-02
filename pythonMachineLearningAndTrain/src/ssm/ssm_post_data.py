import requests
import time

'''
ssm post请求
'''
p = {}
p["app_id"] = "1106571733"
p["time_stamp"] = str(time.time())
p["model"] = "住嘉佳园"

r = requests.post("http://localhost:8080/monitor/uploadData.do", data=p)

print(r.content)
