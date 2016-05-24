"""
an English-Chinese dictionary module using iciba APIs.
"""
# -*- encoding:utf-8 -*-
import urllib.request as urlreq
import xml.etree.ElementTree as ET


class Entry:
    """
    class for a single dictionary entry, it's generaly
    a data structure for translation related parameters
    such as meaning, pronunciation, sample sentences....
    """

    def __init__(self, key_word, translation={}, phonetic_symbol='[]',
                 pron_file='', sample_sent=[]):
        self.__key_word = key_word
        self.__translation = translation
        self.__phonetic_symbol = phonetic_symbol
        self.__pron_file = pron_file
        self.__sample_sent = sample_sent

    def __str__(self):
        string = self.__key_word + '\n' if self.__key_word is not None else 'empty word\n'
        if len(self.__translation) == 0:
            string += '未查到该词的释义！'
        else:
            string += self.__phonetic_symbol + '\n'
            string += self.__pron_file + '\n'
            for key, value in self.__translation.items():
                string += key + ' ' + value + '\n' if key is not None else value + '\n'
            for sent in self.__sample_sent:
                string += sent + '\n'
        return string

    # getters
    def getKeyWord(self):
        return self.__key_word

    def getPhoneticSymbol(self):
        return self.__phonetic_symbol

    def getPronFile(self):
        return self.__pron_file

    def getTranslation(self):
        return self.__translation.copy()

    def getSampleSent(self):
        return self.__sample_sent.copy()

    # setters
    def setKeyWord(self, s):
        self.__key_word = s.strip()

    def setPhoneticSymbol(self, s):
        self.__phonetic_symbol = s.strip()

    def setPronFile(self, s):
        self.__pron_file = s.strip()

    def setTranslation(self, d):
        self.__translation = d.copy()

    def setSampleSent(self, l):
        self.__sample_sent = l.copy()


class Dictionary:
    """
    class for an English-Chinese dictionary using iciba APIs,
    Internet connection is required.
    """

    def __init__(self):
        self.__iciba_key = '93F4227FB49EDC3B86240A6C2DBF178D'

    def __parse_entry_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        key_word = root.find('key').text.strip()
        entry = Entry(key_word)
        ps = root.find('ps')
        entry.setPhoneticSymbol('[]' if ps is None else '[{}]'.format(ps.text.strip()))
        pf = root.find('pron')
        entry.setPronFile('' if pf is None else pf.text.strip())
        poses = root.findall('pos')
        transes = root.findall('acceptation')
        tmp_dict = {}
        for idi in range(len(poses)):
            tmp_dict['' if poses[idi].text is None else poses[idi].text.strip()] = transes[idi].text.strip()
        entry.setTranslation(tmp_dict)
        tmp_lst = []
        for sent in root.findall('sent'):
            orig = sent.find('orig').text.strip()
            trans = sent.find('trans').text.strip()
            tmp_lst.append('{}\n{}'.format(orig, trans))
        entry.setSampleSent(tmp_lst)
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
    dic = Dictionary()
    print(dic.lookup_online('d'))
