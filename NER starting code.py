from nltk import ne_chunk, pos_tag, word_tokenize, sent_tokenize
from nltk.tree import Tree
import nltk

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    #print(chunked)
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk

with open('A High School Journalist Dug Into Suspensions of Black Students.txt', "r") as text_file:
    data = text_file.read()
print (get_continuous_chunks(data))


for sent in nltk.sent_tokenize(data):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if hasattr(chunk, 'label'):
         print(chunk.label(), ' '.join(c[0] for c in chunk))
print('Total sentences in data:', len(nltk.sent_tokenize(data)))

#Manually calculate the recall and precision for your results
#The number of names is 9, but is finds out 8 names, the rate of recall is 8/9=88.9%
#It finds out 8 names, but 3 of them are wrong, the final rate of precision is 5/8=62.5%

