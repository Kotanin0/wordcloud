#coding:utf-8
import csv
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

with open('./words.txt','r') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        text = row[0].split('http')
        texts.append(text[0])
text = ' '.join(texts)
fpath = "~/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
wordcloud = WordCloud(background_color="white", regexp="[\w']+",repeat=True,collocations=False, font_path=fpath, width=900, height=500, max_words=180).generate(text)

plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
