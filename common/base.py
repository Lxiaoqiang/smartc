author = 'damao'

from config import config
from common import HTTP_requests


def get_url(api_path):
    """对接口测试地址封装"""
    host = config.url()
    interface_path = api_path  # 此为接口路径
    url = ''.join([host,interface_path])
    return url

def run_mothed(mothed,url,**item):
    """对HTTP请求封装"""
    if mothed == "get":
        res = HTTP_requests.HttpRequests().get(url=url,**item)
        return res
    else:
        res = HTTP_requests.HttpRequests().psot(url=url,**item)
        return res




