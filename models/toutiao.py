# coding: utf-8
from utils.utils import sj, get_random_user_agent


class Toutiao(object):
    __BASE_URL = 'https://m.toutiao.com/list/?format=json_raw'
    __PARAMS = {
        # 'ac':'wap',
        'count':'20',
        # 'as':'A1A59982B911729',
        # 'cp':'5929E12752796E1',
        # 'min_behot_time':'0',
    }
    __HEADERS = {
        "User-Agent": get_random_user_agent(),
    }

    def __init__(self, tag=None):
        if tag:
            self.__PARAMS['tag'] = tag

    def fetch(self, tag):
        self.__PARAMS['tag'] = tag
        return sj(self.__BASE_URL, params=self.__PARAMS, headers=self.__HEADERS)

