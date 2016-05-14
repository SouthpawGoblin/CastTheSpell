#-*-coding: utf-8-*-
import urllib
import urllib2
import xml.etree.ElementTree as ET
import time
import mp3play
import pyqt5_installer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# ICIBA_KEY = '93F4227FB49EDC3B86240A6C2DBF178D'

# url = 'http://dict-co.iciba.com/api/dictionary.php?key=' + ICIBA_KEY + '&w='
# word = 'english'
# print url + word
# f = urllib2.urlopen(url + word)
# tree = ET.parse(f)
# root = tree.getroot()
# key = root.find('key')
# print key.tag, key.text
# for ps in root.findall('ps'):
#     print ps.tag, ps.text

# pron = root.find('pron')
# urllib.urlretrieve(pron.text, r'D:\GitClonePath\CastTheSpell\1.mp3')
# snd = mp3play.load('1.mp3')
# snd.play()
# time.sleep(snd.seconds())