from urllib.request import urlopen
import gensim
import nltk
import re
from nltk.corpus import stopwords
from gensim.models import KeyedVectors

def validate_web_url(url="http://google"):
    try:
        urlopen(url)
        return True
    except:
        return False


def getTopValue(maxVal, most_common):
    topValue = []
    for x in most_common:
        try:
            if x[1] == maxVal:
                topValue.append(x[0])
            else:
                return topValue
        except:
            print("[!] Err in getting Top words")
            exit()


''' Method to print the given data '''


def printMaxValue(maxVal, most_common):
    print("~" * 25)
    print("Top Most used words in that file are ")
    for x in most_common:
        try:
            if x[1] == maxVal:
                print(x[0])
            else:
                print("~" * 25)
                return
        except:
            print("[!] Err in Handling Print Statement")
            exit()


''' Method to format PIE chart display format '''


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{v:d}'.format(p=pct, v=val)

    return my_autopct


def cleanText(sentence):
    # Cleaing the text
    processed_article = sentence.lower()
    processed_article = re.sub('[^a-zA-Z]', ' ', processed_article)
    processed_article = re.sub(r'\s+', ' ', processed_article)
    # Preparing the dataset
    all_sentences = nltk.sent_tokenize(processed_article)
    all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
    # Removing Stop Words
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]

    return all_words



def wordToVec(most_common, fullContent):
    word2Vec_model = gensim.models.Word2Vec(
        cleanText(fullContent),  # input sentences
        sg=1,  # use skip grams (0=CBOW). skip grams tend to work better on smaller corpora
        size=100,  # this is how many dimensions the vectors will be
        min_count=1  # how many times must a word appear
    )
    # we can update the model with train
    word2Vec_model.train(most_common,
                         total_examples=word2Vec_model.corpus_count,
                         epochs=word2Vec_model.epochs)

    print(f"Most Common words used for {most_common} are {word2Vec_model.wv.most_similar(most_common)}")
