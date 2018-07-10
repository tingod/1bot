# coding: utf-8
from utils.utils import sj


class Tuling(object):
    __URL = 'http://www.tuling123.com/openapi/api'
    __KEY = "f8d28b3c9d6048759f3bebc164dd8f02"

    def fetch(self, params):
        params['key'] = self.__KEY
        return sj(self.__URL, params)

    def text(self, params):
        r = self.fetch(params)
        return r['text']
