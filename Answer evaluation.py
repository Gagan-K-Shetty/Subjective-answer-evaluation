
from rake_nltk import Rake
import nltk
from nltk.corpus import wordnet
import PyDictionary
from nltk.stem import WordNetLemmatizer,PorterStemmer
from appJar import gui

app=gui("evaluation")
train_data=['the theory and development of computer systems able to perform tasks normally requiring human intelligence,' \
           'such as visual perception, speech recognition, decision-making, and translation between languages.' ,
           'Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve ' \
           'from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access ' \
           'data and use it learn for themselves.' ,
           'A genetic algorithm (GA) is a method for solving both constrained and unconstrained optimization problems ' \
           'based on a natural selection process that mimics biological evolution. The algorithm repeatedly modifies a population of individual ' \
           'solutions.' ,
           'the application of computational techniques to the analysis and synthesis of natural language and speech.' ,
           'the branch of technology that deals with the design, construction, operation, and application of robots.']
testlist=[]
trainlist=[]
i=999
def choice(btn):
    if btn=='1 question':
        app.addLabel(250,"what is AI?")
        i=0
        print(i)
        app.addLabelEntry("answer")
        app.addButtons(["submit","reset"],sub)
    elif btn=='2 question':
        app.addLabel(250,"what is Machine Learning?")
        i=1
        print(i)
        app.addLabelEntry("answer")
        app.addButtons(["submit","reset"],sub)
    elif btn=='3 question':
        app.addLabel(250,"what is Genetic Algorithm?")
        i=2
        print(i)
        app.addLabelEntry("answer")
        app.addButtons(["submit","reset"],sub)
    elif btn=='4 question':
        app.addLabel(250,"what is natural language processing?")
        i=3
        print(i)
        app.addLabelEntry("answer")
        app.addButtons(["submit","reset"],sub)
    elif btn=='5 question':
        app.addLabel(250,"what is robotics?")
        i=4
        print(i)
        app.addLabelEntry("answer")
        app.addButtons(["submit","reset"],sub)

def sub(btn):
    if btn=='submit':
        test=app.getEntry("answer")
        print(i)
        Extract(train_data[i],test,max_score,i)

    else:
        app.clearEntry("test_data")
def lematize(lista):
    w=WordNetLemmatizer()
    a=list(map(w.lemmatize,lista))
    return a
def stem(lista):
    s=PorterStemmer()
    a=list(map(s.stem,lista))
    return a
def break_phrases(list):
    a=[]
    for x in list:
        if len(x.split())==1:
            a.append(x)
        else:
            a.extend(x.split())
    return a
key=[{'human': 5, 'recognition': 5, 'computer': 5, 'able': 5, 'visual': 5, 'speech': 5, 'task': 5, 'translation': 5, 'making': 5,
       'perception': 5, 'language': 5, 'development': 5, 'perform': 5, 'normally': 5, 'intelligence': 5, 'decision': 5, 'system': 5,
       'theory': 8, 'requiring': 7},{'system': 5, 'experience': 5, 'learn': 5, 'automatically': 5, 'explicitly': 5, 'computer': 5, 'application': 5, 'program': 5,
       'intelligence': 5, 'access': 5, 'programmed': 5, 'artificial': 5, 'machine': 5, 'data': 5, 'improve': 5, 'ai': 5, 'without': 5,
       'focus': 3, 'ability': 2, 'development': 2, 'provides': 2, 'use': 3, 'learning': 3},{'process': 5, 'optimization': 5, 'genetic': 5,
        'modifies': 5, 'population': 5, 'method': 5, 'based': 5, 'selection': 5, 'solving': 5, 'solution': 5, 'individual': 5, 'natural': 5,
       'repeatedly': 5, 'algorithm': 5, 'mimic': 5, 'evolution': 5, 'constrained': 5, 'problem': 5, 'biological': 5, 'ga': 2, 'unconstrained': 3},
        {'language': 15, 'computational': 15, 'synthesis': 15, 'speech': 15, 'application': 10, 'natural': 10, 'technique': 10, 'analysis': 10},
        {'deal': 10, 'operation': 10, 'application': 10, 'design': 20, 'branch': 10, 'technology': 20, 'construction': 10, 'robot': 10}
]
def Extract(train_data,test_data,max_score,j,Enter_rank=True):
    train,test = Rake(),Rake()
    train.extract_keywords_from_text(train_data)
    test.extract_keywords_from_text(test_data)
    train_keywords=lematize(break_phrases(train.get_ranked_phrases()))
    test_keywords=lematize(break_phrases(test.get_ranked_phrases()))
    for x in test_keywords:
        print(x)
        testlist.append(x)
    result=0
    dict=key[j]
    print(dict)
    for x in testlist:


        if x in dict.keys():
            print(x)
            result=result+(dict[x]*max_score)/100
            print(result,dict[x])
        else:
            syn=PyDictionary.PyDictionary().synonym(trainlist[i])
            if syn==None:
                continue
            print(syn)
            for j in syn :
                if j in testlist:
                    print(trainlist[i],j)
                    print(dict)
                    dict[j]=(dict[x]*max_score)/100
                    result = result + dict[j] * max_score
                    matched.append(i)
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", result)
    app.stopSubWindow()

    app.addButton("get score",score)
def score(btn):
    app.showSubWindow("one")
max_score=10
app.setGeometry("fullscreen")
app.addLabel("50", "Welcome to Evaluation System")
app.addButtons(["1 question","2 question","3 question","4 question","5 question"],choice)

app.go()
