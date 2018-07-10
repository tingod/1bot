# coding: utf-8
from utils.utils import sj, get_random_user_agent


class Qiubai(object):
    __BASE_URL = 'http://m2.qiushibaike.com/article/list/{type}'
    __PARAMS = {
        'count':'20','page':'1',
    }
    __HEADERS = {
        "User-Agent": get_random_user_agent(),
    }

    # def __init__(self, type=None):
    #     if not type:
    #         type='hot'
    #         self.__BASE_URL = self.__BASE_URL.format(type=type)

    def fetch(self, _type):
        return sj(self.__BASE_URL.format(type=_type), params=self.__PARAMS, headers=self.__HEADERS)

    def text(self):
        return self.fetch('text')


    def image(self):
        items = self.fetch('image')['items']
        rtn = []
        for i in items:
            if 'image'==i['format']:
                ri = {}
                ri['content'] = i['content']
                ri['img_url'] = i['high_loc']
                ri['rank'] = i['votes']['up']
                ri['author'] = i['user']['login']
                rtn.append(ri)
        return rtn



    def video(self):
        return self.fetch('video')
