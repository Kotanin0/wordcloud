# -*- coding: utf-8 -*-
from wordcloud import WordCloud
with open("words.txt") as f:
    for words in f:
        stop_words = [u'ある', u'こと', u'これ']
        wordcloud = WordCloud(background_color="white", max_words=50, font_path="/Library/Fonts/tahoma.ttf",width=700,height=400,stopwords=set(stop_words)).generate(words)
wordcloud.to_file("./file.png")
