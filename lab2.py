from nltk.corpus import brown
import nltk
import pickle
from nltk.metrics import *
from nltk.tag import CRFTagger


brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents)*0.8)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

def unigram_tagger():
    unigram_tagger = nltk.UnigramTagger(train_sents)
    #print(unigram_tagger.evaluate(test_sents))
    store_pickle(unigram_tagger, 'unigram_tagger.pkl')

def tnt_tagger():
    tnt_tagger = nltk.tag.tnt.TnT()
    tnt_tagger.train(train_sents)
    store_pickle(tnt_tagger, 'tnt_tagger.pkl')

def perceptron_tagger():
    perceptron_tagger = nltk.tag.PerceptronTagger(load=False)
    perceptron_tagger.train(train_sents)
    store_pickle(perceptron_tagger, 'perceptron_tagger.pkl')

def crf_tagger():
    crf_tagger = CRFTagger()
    crf_tagger.train(train_sents,'model.crf.tagger')
    store_pickle(crf_tagger, 'crf_tagger.pkl')

def store_pickle(model, model_name):
    output = open(model_name, 'wb')
    pickle.dump(model, output, -1)
    output.close()

def retrieve(model_name):
    input = open(model_name, 'rb')
    tagger = pickle.load(input)
    input.close()
    return tagger

if __name__ =="__main__":
    print("unigram tagging")
    unigram_tagger()
    print("tnt tagging")
    tnt_tagger()
    print("perceptron tagging")
    perceptron_tagger()
    #print("crf tagging")
    #crf_tagger()
    print('tagging done.\n')
    
    tagger = retrieve('unigram_tagger.pkl')
    print('unigram:', tagger.evaluate(test_sents))

    tagger = retrieve('tnt_tagger.pkl')
    print('tnt:', tagger.evaluate(test_sents))

    tagger = retrieve('perceptron_tagger.pkl')
    print('perceptron:', tagger.evaluate(test_sents))

