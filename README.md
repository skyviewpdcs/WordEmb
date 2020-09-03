Starting with detecting the most used word on the chosen website, the page’s contents are tokenized, and any stop words are taken out. The data is now trained through Word2Vec, creating an output which not only provides a listing of all the terms synonymous to the most common word, but also stating how closely they relate. I would like to take this research further by comparing it with GLOVE & FastTest techniques.  

initArticle.py is the main python file
Utility.py is the supporting file which contains the functions

Please download the following python classes, in the python terminal:
pip install urllib.request
pip install gensim
pip install nltk
pip install re
pip install newspaper3k
pip install collections
pip install numpy
pip install matplotlib


import nltk
downlad nltk.download('punkt')
