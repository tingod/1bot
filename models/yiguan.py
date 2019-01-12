# coding: utf-8

from utils.utils import sj, get_random_user_agent



class YiGuan(object):
    # 106.75.217.231
    URL = "https://api.jijigugu.club/{}"

    def mood(self, mood_id="N3ZOwLQXplgEdW82v0Bn"):
        load_point = "/mood/listAll"
        # load_point = "/mood/listByDiary"
        # load_point = "/mood/detail"
        params = {
            "id": mood_id,
        }
        r = self._call_api(load_point, params=params)
        return r

    def tag(self, mood_id="N3ZOwLQXplgEdW82v0Bn"):
        # load_point = "/tag/listTop"
        load_point = "/tag/list"

        params = {
            "mid": mood_id,
        }
        r = self._call_api(load_point, params=params)
        return r

    def feed(self, mood_id="evwB0oDG7Rr739axJQ8n"):
        load_point = "/feed/list"
        # load_point = "/feed/listRecommend"

        params = {
            # "mid": "evwB0oDG7Rr739axJQ8n",
            # "mid": "Ar0Kkz1epbNp8JoG2j9V",
            # "mid": "N3ZOwLQXplgEdW82v0Bn",
            "mid": mood_id,
            # "age":"",
            # "gender":2,
            "last_score": ""
        }
        r = self._call_api(load_point, params=params)
        return r

    def diary(self, diary_id):
        # load_point = "/diary/detail"
        load_point = "/diary/listByUser"

        params = {
            "id": diary_id,
        }
        r = self._call_api(load_point, params=params)
        return r

    def comment(self, diary_id):
        load_point = "comment/list" #lastScore=6jRN4BEzQk8j9yKzV0m8
        params = {
            # "did":"9VNeGvpJKOXoV7gMYxd4", # for comment
            "did": diary_id
        }
        r = self._call_api(load_point, params=params)
        return r


    def sss(self):
        load_point = "/session/list" #lastScore=6jRN4BEzQk8j9yKzV0m8
        params = {
        }
        r = self._call_api(load_point, params=params)
        return r

    def user(self):
        # load_point = "/user/detail"
        load_point = "/user/wxLogin"
        params = {
            # "code": "081Vklid2qaEoE0OuUfd2h94id2Vklia"
        }
        r = self._call_api(load_point, params=params)
        return r

    def chat(self, s_id, content):
        load_point = "/chat/add"
        params = {
            "sid": s_id,
            "type": 1,
            "content": content,
        }
        r = self._call_api(load_point, params=params)
        return r


    def _call_api(self, load_point, params, **kwargs):
        p = {
            # "platform": "1",
            # "version": "1.3.0",
            # "os_version": "4.4.4",
            # "dist": "kuan",
            # "model": "Netease/MuMu",
            # "screen": "720*1280",
            # "deviceId": "d3238e1ddab12136f58374e5ae0bf21b",
            # "network": "2",
        }
        return sj(url=self.URL.format(load_point), params=dict(params, **p), **kwargs)


songs = YiGuan().feed()

print(songs)
