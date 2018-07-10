# coding: utf-8
import logging
import random
import requests
import os

from config import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

# DATA_FOLDER = os.path.join(os.path.dirname(__file__), config.DATA_FOLDER)


def sj(url, params=None, headers=None, **kwargs):
    response = requests.get(url, params, headers=headers, **kwargs)
    # logger.info(response.content)
    return response.json()


def s(url, params=None, headers=None, **kwargs):
    response = requests.get(url, params, headers=headers, **kwargs)
    return response.content


def _get_data(filename, default=''):
    """
    Get data from a file
    :param filename: filename
    :param default: default value
    :return: data
    """
    user_agents_file = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(user_agents_file) as fp:
            data = [_.strip() for _ in fp.readlines()]
    except:
        data = [default]
    return data


def get_random_user_agent():
    """
    Get a random user agent string.
    :return: Random user agent string.
    """
    return random.choice(_get_data('user_agents.txt', config.DEFAULT_USER_AGENT))


