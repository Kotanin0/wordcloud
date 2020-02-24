#coding: utf-8
import csv
import re
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from PIL import Image

stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']

pattern = re.compile('[!-~]')

fpath = "~/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

with open('./words.txt','r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        text = row[0].split('http')
        texts.append(text[0])
print('----')
text = ' '.join(texts)
print(text)

wc = WordCloud(background_color="white", font_path=fpath,  
                            stopwords=set(stop_words))
wc.generate(text)

d = path.dirname(__file__)
wc.to_file(path.join(d, "pycloud.png"))

plt.imshow(wc)
plt.axis("off")
plt.figure()
