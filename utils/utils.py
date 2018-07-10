# coding: utf-8
import logging

import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


def sj(url, params=None, headers=None, **kwargs):
    response = requests.get(url, params, headers=headers, **kwargs)
    return response.json()


def s(url, params=None, headers=None, **kwargs):
    response = requests.get(url, params, headers=headers, **kwargs)
    return response.content
