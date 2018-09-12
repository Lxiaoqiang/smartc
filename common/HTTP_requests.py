autthor = 'damao'

import requests
from config import config
from logs import my_logger

logger = my_logger.LogHandler('Http-Requests').getlog()

class HttpRequests(object):
    def __init__(self):
        self._url = config.url()
        logger.info("获取接口地址成功：{a}".format(a=self._url))

    @property
    def url(self):
        return self._url

    def get(self,url,**item):
        params = item.get('params')
        headers = item.get("header")
        try:
            res = requests.get(url=url,params=params,headers=headers,timeout=3,verify=False)
            text = res.json()
            logger.info("get请求发送成功！")
            # text = json.dumps(json.loads(res.text),ensure_ascii=False,sort_keys=True,indent=4,separators=(',',':'))
            return text
        except Exception as e:
            logger.error("get请求错误：{a}".format(a=e))

    def psot(self,url,**item):
        params = item.get('params')
        headers = item.get('headers')
        data = item.get('data')
        json = item.get('json')
        try:
            res = requests.post(url=url,params=params,headers=headers,data=data,json=json)
            text = res.json()
            logger.error("post请求发送成功！")
            # text = json.dumps(json.loads(res.text), ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
            return text
        except Exception as e:
            logger.error("post请求错误：{a}".format(a=e))




# class BaseRun(object):
#     def __init__(self):
#         self.url = config.url()
#
#     def test_requests(self,method,url,**item):
#         json = item.get('json')
#         params = item.get('params')
#         headers = item.get('headers')
#         data = item.get('data')
#         try:
#             res = requests.request(method=method,url=url,timeout=3,params=params,headers=headers,data=data,json=json,verify=False)
#             text = json.dumps(json.loads(res.text),ensure_ascii=False,sort_keys=True,indent=4,separators=(',',':'))
#             return text
#         except Exception as e:
#             print("请求错误：{a}".format(a=e))
