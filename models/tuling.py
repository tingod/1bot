# coding: utf-8
from utils.utils import sj, s


def tuling(message, session):
    tm = Tuling()
    params = {
        'info': message.content,
        'userid': message.source
    }
    rtn = tm.fetch(params)
    if 'url' in rtn:
        """
        图灵用的是360搜索，在此取其json格式解析
        """
        _s = sj(url=rtn['url'], params={'a': 'jsonpview'})
        _j = _s['data']
        # print(_j)
        _l = []
        # _l.append(["title", "description", "img", "url"])
        for i in range(0, 8):
            # print(_j[i]['img_url'])
            _l.append([_j[i]['title'], _j[i]['site'], _j[i]['img_url'], _j[i]['purl']])
        # print(_l)
        return _l
    else:
        return rtn['text']


class Tuling(object):
    __URL = 'http://www.tuling123.com/openapi/api'
    __KEY = "f8d28b3c9d6048759f3bebc164dd8f02"

    def fetch(self, params):
        params['key'] = self.__KEY
        return sj(self.__URL, params)

    def text(self, params):
        r = self.fetch(params)
        return r['text']
