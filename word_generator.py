from PyDictionary import PyDictionary #used for synonyms
from itertools import permutations    #gives all possible words starting with diff. letter
from itertools import combinations_with_replacement
import enchant
dic = PyDictionary()
c = enchant.Dict('en_US')
print("enter any number of alphabets(gibberish is fine)")
s = input()
ar = []
n = len(s)
b = list(s)
j = 0
count = 0
for j in range(3,n+1):
  p = permutations(b,j)
  for i in list(p):
    g = list(set(combinations_with_replacement(i,j)))
    for k in g:
        st = ''.join(k)
        ar.append(st)
#print(ar)
ar = set(ar)#removes the repeated elements
for m in ar:
    if(c.check(m)):
            if(dic.synonym(m)):
                count += 1
                print('->',m.upper(),', '.join(dic.synonym(m)))
            else:
                count += 1
                print('->',m.upper())
