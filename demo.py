author = 'damao'

import requests
from bs4 import BeautifulSoup
import json


url = "http://172.18.90.8:8381/ZCAppcommon/admin/toLogin.do"
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Cookie":"JSESSIONID=72378A54CEA3392F2F99C72E0507FDED"  # Appcommon的token为30分钟
            }

"""用户登录"""
payload = {'loginName':'admin',
           'password':'12345678',
           'validateCode':'6233'}
r = requests.post(url=url,headers=headers,data=payload)
# 格式化接口返回的json数据
aaa = json.dumps(json.loads(r.text),ensure_ascii=False,sort_keys=True,indent=4,separators=('',':'))
print(aaa + "\n===========================================\n")


"""APP应用查询"""
app_url = "http://172.18.90.8:8381/ZCAppcommon/admin/appProject/showAppProjectPage.do"
payload1 = {'appName':'FlashPay',
           'appId':10000080,
           'status':1}
# 格式化接口返回的html数据
rr = requests.post(url=app_url,headers=headers,data=payload1)
b = BeautifulSoup(rr.content,'lxml')
print(b)

# 保存接口的返回数据到指定目录
with open(r".\html_damo.html","wb") as f:
    f.write(rr.content)

# 从返回的html数据中提取需要的数据
data_list = []
for i in b.find('input'):
    data_list.append(i[0])
print(data_list)

# 获取token
from requests import Session


session = Session.post("https://www.baidu.com/")
cookies = session.cookies()
print("resp: {}".format(session.json()))
print("cookies: {}".format(cookies))

