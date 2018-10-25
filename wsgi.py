# -*-coding: utf-8 -*-
__author__ = 'fansly'

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from crypticlog import create_app

app = create_app('production')