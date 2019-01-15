# coding: utf-8
import random
from utils.utils import sj, get_random_user_agent


class Qiubai(object):
    __BASE_URL = 'http://m2.qiushibaike.com/article/list/{type}'
    __PARAMS = {
        'count':'20','page':'1',
    }

    __LIST_KEY = 'items'
    __HEADERS = {
        "User-Agent": get_random_user_agent(),
    }

    # def __init__(self, type=None):
    #     if not type:
    #         type='hot'
    #         self.__BASE_URL = self.__BASE_URL.format(type=type)

    def fetch(self, _type, _params=None):
        _params = {
            'count':'1',
            'page':str(random.randint(1, 1000)),
        }
        if not _params:
            _params = self.__PARAMS
        return sj(self.__BASE_URL.format(type=_type), params=_params, headers=self.__HEADERS)

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
        items = self.fetch('video')['items']
        rtn = []
        for i in items:
            if 'video'==i['format']:
                ri = {}
                ri['content'] = i['content']
                ri['url'] = i['high_loc']
                ri['rank'] = i['votes']['up']
                ri['author'] = i['user']['login']
                rtn.append(ri)
        return rtn

