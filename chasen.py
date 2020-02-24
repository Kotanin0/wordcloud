# coding: utf-8
import MeCab

file = open('kotanin.txt', 'r')
mecabTagger = MeCab.Tagger("-Ochasen /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
pf = mecabTagger.parse(file)

file.close()
print(pf)
