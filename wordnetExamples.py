from nltk.corpus import wordnet as wn
print(wn.synsets('dog'))
print(wn.synset('dog.n.01').definition())