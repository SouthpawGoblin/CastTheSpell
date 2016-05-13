#-*- encoding:utf-8 -*-
"""
An English-Chinese dictionary module using iciba APIs.
"""

import urllib
import urllib2
import xml.etree.ElementTree as ET
import time
import mp3play

class SingleEntry:
    """
    class for a single dictionary entry, it's generaly
    a data structure for translation related parameters
    such as meaning, pronunciation, sample sentences....
    """
    def __init__(self, key_word, translation={}, phonetics='', pron_file='', sample_sent=[]):
        self.key_word = key_word
        self.translation = translation
        self.phonetics = phonetics
        self.pron_file = pron_file
        self.sample_sent = sample_sent

if __name__ == '__main__':
    et = SingleEntry('hello', {'你好':'v.'})
    print et.key_word, et.translation.keys()[0]
    print '人们'
