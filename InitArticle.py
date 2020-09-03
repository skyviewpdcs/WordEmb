from newspaper import Article
import Utility
import nltk
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

url = ''
content = ''
"Validating URL"
while True:
    url = input("Please enter valid Website for analyses ")
    if not Utility.validate_web_url(url):
        print("Error presented with the link; please try another")
    else:
        break

"Getting content of that given URL"
try:
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
except:
    print("Error found in link.")
    exit()

# sanitizing the unwanted words
raw = ' '.join(word_tokenize(content.lower()))

tokenizer = RegexpTokenizer(r'[A-Za-z]{2,}')
words = tokenizer.tokenize(raw)

# remove stopwords
stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

print(type(words))
print(type(content))
# count word frequency, sort and return just 20
counter = Counter()
counter.update(words)
most_common = counter.most_common(20)

# sort in-place from highest to lowest
most_common.sort(key=lambda x: x[1], reverse=True)
word = [x[0] for x in most_common]
count = [x[1] for x in most_common]
exitVal = True
while exitVal == True:
    choice = input('''
    Please type     1 ->   Print the Most Common Words

    Please type     2 ->   Bar Chart for Most Common Words

    Please type     3 ->   Pie Chart for Most Common Words

    Please type     4 ->   Word2Vec Analysis from the most Common words

    Please type     5 ->   Word2Vec analysis for any given word

    Please type     6->    Exit    

    ''')
    if choice == "1":
        "Print the Most Common Word"
        Utility.printMaxValue(count[0], most_common)
    elif choice == "2":
        "Bar Chart"
        ## Bar Graph
        word = [x[0] for x in most_common]
        count = [x[1] for x in most_common]
        x_pos = np.arange(len(word))
        # calculate slope and intercept for the linear trend line
        slope, intercept = np.polyfit(x_pos, count, 1)
        trendline = intercept + (slope * x_pos)
        plt.plot(x_pos, trendline, color='red', linestyle='--')
        plt.bar(x_pos, count, align='center')
        plt.xticks(x_pos, word)
        plt.ylabel('Popularity Score')
        plt.show()
    elif choice == "3":
        ###PIE Chart
        fig, ax = plt.subplots()
        ax.pie(count, labels=word, autopct=Utility.make_autopct(count))
        ax.axis('equal')
        ax.set_title('Website Word count')
        plt.show()
    elif choice == "4":
        try:
            top_value = Utility.getTopValue(count[0], most_common)
            Utility.wordToVec(top_value, content)
        except:
            print("Error detected")
    elif choice == "5":
        try:
            word2Check = input("Enter word to check word embedding similarities")
            Utility.wordToVec(word2Check, content)
        except:
            print("Error found; try another word")
    elif choice == "6":
        print("Exiting......")
        exitVal = False
    else:
        print("Option not valid; please select number from 1~6")


