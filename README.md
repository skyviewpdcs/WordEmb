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


When you run the initArticle.py
it will prompt for the Website:
Please enter valid Website for analyses https://www.cnn.com/2020/08/30/politics/trump-russia-investigation-rod-rosenstein/index.html
    Please type     1 ->   Print the Most Common Words

    Please type     2 ->   Bar Chart for Most Common Words

    Please type     3 ->   Pie Chart for Most Common Words

    Please type     4 ->   Word2Vec Analysis from the most Common words

    Please type     5 ->   Word2Vec Analysis for any given word

    Please type     6->    Exit   
    
    If you entered "https://www.cnn.com/2020/08/30/politics/trump-russia-investigation-rod-rosenstein/index.html" the above site & pressed "1" you would probably get the following results:
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    Top Most used words in that file are 
    former
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    if you choose option "2":
      It will display a bar chart
    if you choose option "3":
      It will display a PIE chart
    if you choose option "4":
      Most Common words used for ['former'] are [('likely', 0.22271528840065002), ('final', 0.18102650344371796), ('fbi', 0.17665429413318634), ('opened', 0.17363959550857544), ('revelation', 0.16882628202438354), ('examine', 0.1487174928188324), ('took', 0.14706338942050934), ('special', 0.11645396798849106), ('robert', 0.1104341372847557), ('links', 0.10966995358467102)]     
     if you choose option "3":
      It will prompt for "Enter word to check word embedding similarities " russian
Most Common words used for russian are [('enforcement', 0.34288784861564636), ('justice', 0.240381121635437), ('cnn', 0.19349274039268494), ('possible', 0.19332095980644226), ('president', 0.1820136159658432), ('told', 0.1752942055463791), ('privately', 0.13251204788684845), ('march', 0.12562121450901031), ('newspaper', 0.12348045408725739), ('campaign', 0.11969958245754242)]
for any other options it will say "Option not valid; please select number from 1~6"


