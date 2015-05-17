# -*- coding: utf-8 -*-
'''
Created on 2015-5-16

@author: Nob
'''
import codecs
import os
import os.path


def setup(language=None):
    global __lines
    language = language or 'en_GB'
    langpath = os.path.join(os.path.dirname(__file__), language)
    __lines = {}
    for root, dirs, files in os.walk(langpath):
        for file in files:
            name, ext = file.split('.')
            if ext == 'py' and name != '__init__':
                ns = {}
                with codecs.open(os.path.join(langpath, file), "r", "utf-8") as f:
                    code = f.read()
                    exec code in ns
                    __lines[name] = ns['t']


def text(key, default=None, args=None):
    parts = key.split('.')
    if len(parts) == 2:
        name = parts[0]
        key = parts[1]
    if len(parts) == 1:
        name = 'global'
        key = parts.pop(0)

    t = __lines.get(name)
    if t:
        text = t.get(key, default)
        if text and args:
            text = text % args
    else:
        text = default
    return text