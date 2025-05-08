
import re
from collections import Counter
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
    "quem", "que", "qual", "sim", "não", "com", "tem"
]

def index_collection():
    #first step: to index the collection we need to read it
    print('Método para indexar a coleção')


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
    print(dictionary)
    #para ver o dicionario formatado jogue o resultado do terminal nesse link: https://jsonformatter.curiousconcept.com/#

#def indexar(arrayComPalavrasRepetidas):

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
    dictionary = create_collection_dictionary()


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








