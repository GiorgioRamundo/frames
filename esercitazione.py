import nltk

from utils import getFrameSetForStudent
from nltk.corpus import framenet as fn
from nltk.corpus import treebank
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer


def get_sentence_list(s):
    elements = s.split('_')
    list = []
    for element in elements:
        list.append(element + ' ')
    return list

def reggente(s):
    lemmatizer = WordNetLemmatizer()
    if 'IED' in s:
        return lemmatizer.lemmatize('IED')
    elif 'process' in s:
        return lemmatizer.lemmatize('process')
    elif 'Convoy' in s:
        return lemmatizer.lemmatize('Convoy')
    elif 'Food' in s:
        return lemmatizer.lemmatize('Food')
    elif 'Publishing' in s:
        return lemmatizer.lemmatize('Publishing')
    return ''

def word_set(f):
    s = set()
    FEs = f.FE.keys()
    LUs = f.lexUnit.keys()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    for fe in FEs:
        fed = f.FE[fe]
        word_tokens = word_tokenize(fed.definition)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        for w in filtered_sentence:
            s = s | {lemmatizer.lemmatize(w.lower())}
        s = s | {fed.name}
    for lu in LUs:
        s = s | {lemmatizer.lemmatize(lu.lower())}
    return s


def fn_disambiguation_context(f,r):
    ctx_w = set()
    ctx_w = ctx_w | {r.lower()}
    ctx_w = ctx_w | word_set(f)
    ctx_s = set()
    ctx_max = set()
    m = 0
    s_max = []
    stop_words = set(stopwords.words('english'))

    for s in wn.synsets(r):
        for e in s.examples():
            e = nltk.word_tokenize(e)
            filtered = [w for w in e if not w in stop_words]
            for w in filtered:
                ctx_s = ctx_s | {w.lower()}
        for hn in s.hyponyms():
            for lemma in hn.lemmas():
                split_lemma = lemma.name().split('_')
                for word in split_lemma:
                    ctx_s = ctx_s | {word.lower()}
        for hy in s.hypernyms():
            for lemma in hy.lemmas():
                split_lemma = lemma.name().split('_')
                for word in split_lemma:
                    ctx_s = ctx_s | {word.lower()}
        ctx_i = ctx_s & ctx_w
        v = len(ctx_i) + 1
        if v > m:
            ctx_max = ctx_i
            m = v
            s_max = s
        ctx_s = set()
    return s_max





ids = getFrameSetForStudent('Ramundo')
for i in ids:
    f = fn.frame_by_id(i)
    print('*********SYNSETS FOR {}************'.format(f.name))
    sentence = str(f.name).split('_')
    r = reggente(sentence)
    print('Synset for {} is {}'.format(r,fn_disambiguation_context(f,r)))
    FEs = f.FE.keys()
    for fe in FEs:
        fes = fe.replace('_', ' ')
        print('Synset for {} is {}'.format(fes,fn_disambiguation_context(f, fes)))
    LUs = f.lexUnit.keys()
    for lu in LUs:
        lus = lu.split('.')
        print('Synset for {} is {}'.format(lus[0],fn_disambiguation_context(f, lus[0])))