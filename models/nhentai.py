# coding: utf-8
import random
from utils.utils import s, sj, get_random_user_agent

class Nhentai():
    NHENTAI_HOME = "https://nhentai.net"
    NHENTAI_I = "https://i.nhentai.net"
    NHENTAI_T = "https://t.nhentai.net"


    HEADERS = {
        "User-Agent": get_random_user_agent(),
    }

    def fetch(self, url, point, params=None, headers=None):
        u = "{url}{point}".format(url=url, point=point)
        return sj(u, params, headers)


    def search(self, kw):
        url = self.NHENTAI_HOME
        point = "/api/galleries/search"
        params = {
            "query": kw,
            "page":1,
        }
        return self.fetch(url, point, params)

    def get_book(self, id):
        url = self.NHENTAI_HOME
        point = "/api/gallery/{book_id}".format(book_id=id)
        return self.fetch(url, point)

    def get_book_recommend(self, id):
        url = self.NHENTAI_HOME
        point = "/api/gallery/{book_id}/related".format(book_id=id)
        return self.fetch(url, point)

    def get_gallery(self, id):
        '''
        :param id: media_id
        :return:
        '''
        url = self.NHENTAI_I
        point = "/galleries/{gallery_id}".format(gallery_id=id)
        return self.fetch(url, point)

    def get_gallery_thumb(self, id):
        '''

        :param id: media_id
        :return:
        '''
        url = self.NHENTAI_T
        point = "/galleries/{gallery_id}".format(gallery_id=id)
        return self.fetch(url, point)

    def get_picture(self, id, pn=1, ft="jpg"):
        url = self.NHENTAI_I
        point = "/galleries/{gallery_id}/{page_num}.{file_type}".format(gallery_id=id, page_num=pn, file_type=ft)
        return self.fetch(url, point)

    def get_picture_thumb(self, id, pn="thumb", ft="jpg"):
        try:
            int(pn)
            pn = "{}t".format(pn)
        except:
            pass
        url = self.NHENTAI_T
        point = "/galleries/{gallery_id}/{page_num}.{file_type}".format(gallery_id=id, page_num=pn, file_type=ft)
        return self.fetch(url, point)






print(Nhentai().search('如月群真'))
# print(Nhentai().get_book('223498'))
# print(Nhentai().get_book_recommend('223498'))
# print(Nhentai().get_picture('1100293'))
# print(Nhentai().get_picture_thumb('1100293','cover'))

