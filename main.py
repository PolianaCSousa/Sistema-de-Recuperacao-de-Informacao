
import re
from collections import Counter
from itertools import islice
from time import sleep

#palavrasParaRetirar
stopWords = [
    "eu", "tu", "ele", "ela", "nós", "vocês", "eles", "elas",
    "me", "te", "se", "nos", "vos", "lhe", "lhes",
    "meu", "minha", "meus", "minhas",
    "seu", "sua", "seus", "suas",
    "nosso", "nossa", "nossos", "nossas",
    "esse", "essa", "isso", "este", "esta", "isto",
    "aquele", "aquela", "aquilo",
    "quem", "que", "qual", "sim", "não", "com", "tem", "yes", "not"
]

def index_collection(vocabulary):

    collection = create_collection_dictionary()

    # index = list() [0 = para, 1 = que, 2 = arquivos, ... etc.]
    # aux = 0
    index = dict()

    for vocabulary_key, total_freq in vocabulary.items():
        index[vocabulary_key] = [total_freq,
                                 {}]  # começa com uma lista contendo a frequência total e um dicionário vazio

        for doc_name, terms in collection.items():
            if vocabulary_key in terms:
                freq = terms[vocabulary_key]
                index[vocabulary_key][1][doc_name] = freq  # adiciona ao dicionário de documentos

       # print(index[vocabulary_key])
    return index

def bool_index(vocabulary):
    collection = create_collection_dictionary()
    #print(collection)
    bool = dict()

    for word, total_freq in vocabulary.items():
        bool[word] = {}
        for doc_name, doc_value in collection.items():
            if word in doc_value:
                bool[word][doc_name] = 1;
            else:
                bool[word][doc_name] = 0;

    print(bool)
#Lê o arquivo e extrai o vocabulário colocando em um array.
# O vocabulário é toda palavra com mais de 2 caracteres que não sejam stopwords  (pronomes, caracteres especiais, não, sim, e etc.)
def extract_vocabulary(fileName):
    file = open(fileName, 'r', encoding='utf-8')
    vocabulary = [];
    for line in file:
        strings = re.findall(r'\b[^\W\d_]{3,}\b', line, re.UNICODE)
        lower_strings = list(map(str.lower, strings))
        #filtered = [s for s in strings if s and len(s) > 2 and not s.isdigit()]
        vocabulary = vocabulary + lower_strings

    file.close()

    return vocabulary

def create_dictionary(fileName):

    vocabulary = extract_vocabulary(fileName)
    counter = Counter(vocabulary)
    """for k,v in counter.items():
        print(k,v)"""
    #print(counter)
    return dict(counter)

def create_collection_dictionary():

    dictionary = dict()
    qtd_files = 3

    for i in range(1, qtd_files + 1): #o range é exclusivo no final, entao para chegar até o 2 precisa adicionar mais um. Ex, se for range(1,5) ele vai do 1 ao 4
        dictionary['doc'+str(i)+'.txt'] = create_dictionary('doc'+str(i)+'.txt')

    return dictionary
    #print(dictionary)
    #para ver o dicionario formatado jogue o resultado do terminal nesse link: https://jsonformatter.curiousconcept.com/#

#def indexar(arrayComPalavrasRepetidas):

def get_most_relevant_terms():

    dictionary = create_collection_dictionary()
    vocabulary = dict()

    for key, value in dictionary.items():
        for key, v in value.items():
            if key in vocabulary:
                vocabulary[key] = vocabulary[key] + v
            else:
                vocabulary[key] = v
   # print(vocabulary)
    sorted_vocabulary = dict(sorted(vocabulary.items(),key=lambda word: word[1], reverse=True))

    vocabulary_50 = dict(islice(sorted_vocabulary.items(), 20))


    #print(vocabulary_50)
    return vocabulary_50

def menu():

    while True:
        option = int(input("\n\n******** TRABALHO DE RECUPERAÇÃO DE INFORMAÇÃO **************\n"
              "**************************************************************\n"
              "******** ALUNOS: LEANDRO & POLIANA ***************************\n"
              "**************************************************************\n"
              "********************** MENU **********************************\n"
              "********** 1 - PARA INDEXAR A COLEÇÃO ************************\n"
              "********** 2 - PARA IMPRIMIR O VOCABULÁRIO *******************\n"
              "********** 3 - PARA IMPRIMIR A MATRIZ DE OCORRÊNCIAS *********\n"
              "********** 4 - PARA IMPRIMIR A MATRIZ DE FREQUENCIAS *********\n"
              "********** 0 - SAIR ******************************************\n"
              "**************************************************************\n"
              "DIGITE A OPÇÃO DESEJADA: "))


        match option:
            case 1:
                index_collection()

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 0:
                break



if __name__ == "__main__":
    # menu()
    #vocabulary = extract_vocabulary('doc1.txt')
    result = get_most_relevant_terms() #menu 2
    #print(result)

    index = bool_index(result)

    '''
    vocabulary2 = create_dictionary('doc2.txt')
    vocabulary1 = create_dictionary('doc1.txt')
    
    arquivos["doc1.txt"] = vocabulary1
    arquivos["doc2.txt"] = vocabulary2
    '''


    '''for fileName in arquivos:
        print(arquivos[fileName]['doce'])
        break
        #print(arquivos)
    '''








