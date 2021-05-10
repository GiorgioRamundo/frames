import sys
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus.reader.framenet import PrettyList
from operator import itemgetter
from pprint import pprint

# f = fn.frame_by_name('Medical_specialties')
# print(f)
# f = fn.frame_by_name('Perception')
# print(f)
# f = fn.frame_by_name('Complaining')
# print(f)
# print(fn.frames_by_lemma(r'(?i)epidemiol'))

# frame_list = PrettyList(fn.frames(r'(?i)crim'), maxReprSize=0, breakLines=True)
# frame_list.sort(key=itemgetter('ID'))
# for f in frame_list:
#     print('====================\nNAME ' + str(f.name))
#     print('====================\nDEF ' + str(f.definition))
#     print('====================\nFEs ' + str(f.FE))
#     print('====================\nLUs ' + str(f.lexUnit))

# f = fn.frame_by_id(256)
# print('NAME: {}[{}]\tDEF: {}'.format(f.name, f.ID, f.definition))
# print('\n____FEs____')
# FEs = f.FE.keys()
# # invece di listarli in maniera indistinta, li spacchettiamo per maneggiarli meglio
# for fe in FEs:
#     fed = f.FE[fe]
#     print('\tFE: {}\t DEF: {}'.format(fe, fed.definition))
# print('\n____LUs____')
# LUs = f.lexUnit.keys()
# for lu in LUs:
#     print(lu)

# # stampa del frame Revenge
# f = fn.frame('Revenge')
# print(f)
# print('==========================')
# # stampa dei frame elements che caratterizzano tale frame
# print(f.FE)
# print('==========================')
# # stampa della definizione associata a un certo FE
# print(f.FE['Injury'].definition)
# print('==========================')
# # accesso alle LUs presenti nel frame
# for k in f.lexUnit.keys():
#     print(k)
# print('==========================')
#
# for fe in fn.fes('location'):
#     print(fe.frame.name + '.' + fe.name)