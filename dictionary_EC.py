#-*- encoding:utf-8 -*-
"""
An English-Chinese dictionary module using iciba APIs.
"""

import urllib.request as urlreq
import xml.etree.ElementTree as ET


class Entry:
    """
    class for a single dictionary entry, it's generaly
    a data structure for translation related parameters
    such as meaning, pronunciation, sample sentences....
    """

    def __init__(self, key_word, translation={}, phonetic_symbol='',
                 pron_file='', sample_sent=[]):
        self.key_word = key_word
        self.translation = translation
        self.phonetic_symbol = phonetic_symbol
        self.pron_file = pron_file
        self.sample_sent = sample_sent

    def __str__(self):
        string = self.key_word + '\n' if self.key_word is not None else 'empty word\n'
        if len(self.translation) == 0:
            string += '未查到该词的释义！'
        else:
            string += '[' + self.phonetic_symbol + ']\n'
            string += self.pron_file + '\n'
            for key, value in self.translation.items():
                string += key + ' ' + value if key is not None else value
            for sent in self.sample_sent:
                string += sent
        return string


class Dictionary:
    """
    class for an English-Chinese dictionary using iciba APIs,
    Internet connection is required.
    """

    def __init__(self, iciba_key=None):
        self.__iciba_key = iciba_key

    def __parse_entry_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        key_word = root.find('key').text
        entry = Entry(key_word)
        ps = root.find('ps')
        entry.phonetic_symbol = '' if ps is None else ps.text
        pf = root.find('pron')
        entry.pron_file = '' if pf is None else pf.text
        poses = root.findall('pos')
        transes = root.findall('acceptation')
        for idi in range(len(poses)):
            entry.translation[poses[idi].text] = transes[idi].text
        for sent in root.findall('sent'):
            orig = sent.find('orig').text
            trans = sent.find('trans').text
            entry.sample_sent.append(orig + trans)
        return entry

    def lookup_online(self, key_word):
        if self.__iciba_key is None:
            raise Exception('iciba_key无效，无法在线查词')
        url = 'http://dict-co.iciba.com/api/dictionary.php?key=' \
            + self.__iciba_key \
            + '&w=' + key_word
        try:
            f = urlreq.urlopen(url)
            return self.__parse_entry_xml(f)
        except Exception as e:
            raise e


if __name__ == '__main__':
    ICIBA_KEY = '93F4227FB49EDC3B86240A6C2DBF178D'
    dic = Dictionary(ICIBA_KEY)
    print(dic.lookup_online(input()))
