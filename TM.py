import nltk

def parseSentences(fileName):
    news = open(fileName,"r")
    sent = news.read()
    taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
    #grammar = "NP: {<DT>?<JJ>*<NN>}"
    #cp = nltk.RegexpParser(grammar)
    #result = cp.parse(taggedS)
    #add all definite nouns into a list
    definiteNouns = []
    countList = []
    for word in taggedS:
        if isDefinite(word,taggedS):
            definiteNouns.append(word[0])
    #count all definite nouns and turn into tuple
    countset = set(definiteNouns)
    for i in countset:
        countList.append((i,definiteNouns.count(i)))
    #sort the list with the number of an item
    countList.sort(key = takeSecondItem)
    print(countList)
    #result.draw()
    news.close()
def takeSecondItem(item):
    return item[1]
def isDefinite(word_pos: tuple, wordList: list) -> bool:
    if word_pos[1] in ["NN", "NNS"]:
        position = wordList.index(word_pos)
        if position != 0 & wordList[position - 1][0] in ["the", "The"]:
            return True
    return False

if __name__ == '__main__':
    parseSentences("news.txt")
