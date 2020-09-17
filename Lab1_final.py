
# Question 2
# ShiftReduceParser

# Question 3
import nltk
from nltk import CFG

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" 
  NP -> "I" | "boy" | Det N | Det N PP
  Det -> "a" | "the"
  N -> "telescope" | "park"
  P -> "in" | "with"
  """)

sent = "I saw a boy in the park with a telescope".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)   # interpret the sentence on the basis of grammar
for tree in rd_parser.parse(sent):
    print(tree)     # output the interpreted result
    tree.draw()     # output the grap

# Question 4

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "found" 
  NP -> "I" | "Tommy" | Det N | Det N PP
  Det -> "a" | "the"
  N -> "hat" | "bus" 
  P -> "on" | "with" 
  """)

sent = "I found Tommy on the bus with a hat".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for t in rd_parser.parse(sent):
    print(t)
    t.draw()


# Question 5, 6, 7, 8

f = open("/Users/zhiling/Desktop/Nznews.txt", "r")    # open the file with only reading right
st = f.read()        # read the file
print(type(st))
print(st)            # print all the file
tokens = nltk.word_tokenize(st)   # tokenize the words
a = ([tokens[offset+1] for offset in [i for i, x in enumerate(tokens) if x == 'the']])   # find the words which are follwed by the
print(sorted(a))   # print the words in an ascending order
print(string.count(sorted(a)))   # print the numbers of each words
f.close()    # close the file



