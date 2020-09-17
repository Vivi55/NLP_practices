from nltk.corpus import wordnet,stopwords,brown
from nltk.stem import WordNetLemmatizer
import os
import os.path
from lxml import etree
import nltk
import datetime
import time
from collections import Counter
from pickle import dump,load


def readByfilter(path):
    alllist, maleslist, femalelist, ageunder20, ageover20, noFilter = [], [], [], [], [], []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.split(".")[-1] == 'xml'):
                alllist.append(file)
                if (file.split(".")[1] == 'male'):
                    maleslist.append(file)
                else:
                    femalelist.append(file)
                if (int(file.split(".")[2]) <= 20):
                    ageunder20.append(file)
                else:
                    ageover20.append(file)
    # print('femalelist_Length', len(femalelist))
    # print('maleslist_Length', len(maleslist))
    # print('alllist_Length', len(alllist))
    # print('ageunder20_Length', len(ageunder20))
    # print('ageover20_Length', len(ageover20))

    return alllist, maleslist, femalelist, ageunder20, ageover20

def readXml(path):
    filedata = ''
    dateInfo, yearlist = [], []
    # f = open("/Users/molly/Downloads/blogs/5114.male.25.indUnk.Scorpio.xml", 'r', encoding='ISO-8859-1')
    f = open(path, 'r', encoding='ISO-8859-1')
    str = f.read()
    parser = etree.XMLParser(recover=True)  # recover from bad characters.
    root = etree.fromstring(str, parser=parser)
    for sub_node in root:
        if (sub_node.tag == "post"):
            filedata = filedata + sub_node.text.strip()
        if sub_node.tag == 'date':
            date = sub_node.text
            dateInfo.append(date)
            year = date[-1]
            yearlist.append(year)

    # print('number of blogs in 2001', yearlist.count('1'))
    # print('number of blogs in 2002', yearlist.count('2'))
    # print('number of blogs in 2003', yearlist.count('3'))
    # print('number of blogs in 2004', yearlist.count('4'))

    return filedata,dateInfo,yearlist

def stopwords_remove(text):
    stopword = stopwords.words("english") + ['Thing','thing','I','i', 'time', 'life', 'people', 'what', 'lots', 'urlLink', 'who', 'is', 'a', 'at', 'is', 'he', ',', '/',
                 'to', 'the', 'and', 'of', 'as', '>>', '*', 'r', 'x', '..', '....', 'Im', ']', 'bt', 'Haha']
    stopword = set(stopword)
    print(stopword)
    querywords = text.split(' ')
    resultwords = [word.lower() for word in querywords if word not in stopword]
    results = ' '.join(filter(str.isalnum, resultwords))
    # print('word length before remove : ', len(text))
    # print('word length after remove: ', len(results))
    return results

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_text(data):
    tagged_sent = nltk.pos_tag(nltk.word_tokenize(data))
    wnl = WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))
    lemmas_result = ' '.join(lemmas_sent)
    return lemmas_result

def train(xml_list, path):
    start = datetime.datetime.now()
    nouns,common_words = [],[]

    for i in xml_list:
        rawdata, dateInfo, yearlist = readXml(path + "/" + i)
        data = stopwords_remove(rawdata)
        # print("data:",data)
        lemmas_sent = lemmatize_text(data)
        # print("lemmas_sent:", lemmas_sent)
        # finaldata = stopwords_remove(rawdata)
        # print("finaldata:",finaldata)
        tagwords = nltk.pos_tag(nltk.word_tokenize(lemmas_sent))
        # print(tagwords)
        for item in tagwords:
            if item[1] in ["NNP", "NN", "NNS", "NNPS"]:  # find all the nouns in the article and save as list
                nouns.append(item[0])
    dict = Counter(nouns)  # Append all the nouns into a dictionary
    # print(dict.most_common(10))
    for wordtuple in dict.most_common(10):
        common_words.append(wordtuple[0])
    print(common_words)
    end = datetime.datetime.now()
    print('Time taken', end - start)


path = r"/Users/molly/Downloads/blogs test"
alllist, maleslist, femalelist, ageunder20, ageover20 = readByfilter(path)
train(maleslist,path)


