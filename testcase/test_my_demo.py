author = 'damao'

import unittest
from common import base
import json
from ddt import ddt,data,unpack
from logs import my_logger

logger = my_logger.LogHandler("damao").getlog()

@ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        interface_path = 'get'
        self.url = base.get_url(interface_path)
        logger.info("接口地址：{a}".format(a=self.url))

    # @data({'a': 1},123,{'c': 1},1,233)
    @data(2,'httpbin.org')
    def test_get(self,a):
        """接口测试用例"""
        params = {'c': 1}
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                    }
        res = base.run_mothed(url=self.url,params=params,headers=headers,mothed='get')
        logger.info('请求体参数：params:{a}'.format(a=params))
        logger.info('请求头参数：header:{b}'.format(b=headers))
        print(json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':')))
        # 断言
        result = res.get('headers').get('Host')
        if self.assertEqual(result,a) is True:
            logger.info("断言正确，用例执行成功！")
        else:
            logger.info("断言失败，用例执行成功！")

        # logger.info("断言结果：{a}".format(a=bool(rult)))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()



