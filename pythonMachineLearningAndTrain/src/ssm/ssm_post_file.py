# coding:utf-8
import time
import requests

'''
ssm - 上传文件
'''

p = {}
p["app_id"] = "1106571733"
p["time_stamp"] = str(time.time())
p["model"] = "住嘉佳园"

url_mul = 'http://localhost:8080/monitor/uploadFile.do'

file = {'file': open('E://MachineLearning//pythonMachineLearningAndTrain//src//ssm//IMG_2966.JPG', 'rb')}

r = requests.post(url_mul, files=file, data=p)
print(r.text)
print(r.content)
