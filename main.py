
import re
from collections import Counter
from itertools import islice
from time import sleep

#O QUE PRECISAMOS FAZER:
# Implementar o modelo booleano
# Fazer o menu funcionar
# Salvar as informações em arquivos
# Verificar se o arquivo existe antes de extrair o vocabulário
# Tratar as stopwords




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

    #print(bool)
    return bool
#Lê o arquivo e extrai o vocabulário colocando em um array.
# O vocabulário é toda palavra com mais de 2 caracteres que não sejam stopwords  (pronomes, caracteres especiais, não, sim, e etc.)


#OPERADORES: AND, OR e NOT
'''
ideia: primeiro passo é pegar termo por termo da consulta (separar os termos dos operadores)
ex: doce AND mel
[doce, AND, mel]

'''
operators = ['and', 'or', 'not']
def boolean_model():
    #wordsAndOperators is the consult
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_* CONSULTA *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n'
          '-*- INSTRUÇÕES -*-\n'
          'Para realizar a consulta você pode utilizar os operadores AND, OR ou NOT.\n'
          'Para cada consulta você pode usar no máximo dois operadores.\n')
    words = input('Informe a consulta: ')

    wordsAndOperators = list(map(str.lower, words.split())) #é a consulta separada em uma lista

    #Verifica se o usuario digitou um operador
    if len(wordsAndOperators) == 3:
        if not wordsAndOperators[1] in operators:
           return print('Não há operadores na frase!')
    elif len(wordsAndOperators) == 5:
        if (not wordsAndOperators[1] in operators) and (not wordsAndOperators[3] in operators):
            return print('Não há operadores na frase!')
        elif (not wordsAndOperators[1] in operators) or (not wordsAndOperators[3] in operators):
            return print('Está faltando um operador!')

    vocabulary = get_most_relevant_terms()
    #Verifica se o usuario fez uma consulta que contém termos indexados
    consult_boolean = words_in_vocabulary(wordsAndOperators, vocabulary)
    if consult_boolean == -1:
        print('Os termos da consulta não estão no vocabulário. Tente fazer uma consulta diferente!')
    else:
        #lógica para calcular o documento retornado
        calculate_result(wordsAndOperators, consult_boolean)
        print(f'retorno: {consult_boolean}')
        pass


""" antes
    def calculate_result(wordsAndOperators,consult_boolean):

    if len(wordsAndOperators) == 3: #temos apenas um operador para calcular
        calculate_operator(wordsAndOperators,consult_boolean)
        pass
    else: #temos 2 operadores para calcular
        pass """

def calculate_result(wordsAndOperators, consult_boolean):
    if len(wordsAndOperators) == 3:  # temos apenas um operador para calcular
        calculate_operator(wordsAndOperators, consult_boolean)
    else:  # temos 2 operadores para calcular
        partial_result = calculate_operator(wordsAndOperators[0:3], consult_boolean)
        new_consult = [partial_result] + wordsAndOperators[3:]
        calculate_operator(new_consult, consult_boolean)



#vou fazer o metodo sempre receber apenas dois termos e um operador
def calculate_operator(consult, consult_boolean):

    docs = list(next(iter(consult_boolean.values())).keys())

    if consult[1] == 'and':
        result = {}
        for doc in docs:
            result[doc] = consult_boolean[consult[0]][doc] & consult_boolean[consult[2]][doc]
        print(f'\nResultado da operação AND: {result}')
        return result

    if consult[1] == 'or':
        result = {}
        for doc in docs:
            result[doc] = consult_boolean[consult[0]][doc] | consult_boolean[consult[2]][doc]
        print(f'\nResultado da operação OR: {result}')
        return result

    if consult[1] == 'not':
        result = {}
        for doc in docs:
            result[doc] = int(not consult_boolean[consult[2]][doc])
        print(f'\nResultado da operação NOT: {result}')
        return result






def words_in_vocabulary(words,vocabulary):

    boolean_index = bool_index(vocabulary)
    consult_boolean_index = dict()

    for i in range(0,len(words), 2): #gera índices pares, ou seja, ele vai de 2 em 2. Ex: se words tiver 5 elementos, i será: 0, 2, 4. Fiz isso pois os termos sempre estarão em índices pares e são eles que estamos analisando nesse método
        for key, value in boolean_index.items():
            if words[i] == key:
                consult_boolean_index[key] = value

    if not consult_boolean_index: #se o dicionario for vazio quer dizer que o usuário não informou nenhum termo que faz parte do vocabulário
        return -1
    else:
        return consult_boolean_index









def extract_vocabulary(fileName):
    try:
        file = open(fileName, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'Arquivo {fileName} não encontrado.')
        return []

    vocabulary = []
    for line in file:
        strings = re.findall(r'\b[^\W\d_]{3,}\b', line, re.UNICODE)
        lower_strings = list(map(str.lower, strings))
        filtered = [s for s in lower_strings if s not in stopWords]
        vocabulary = vocabulary + filtered

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
              "********** 5 - PARA APLICAR O MODELO BOOLEANO ****************\n"
              "********** 0 - SAIR ******************************************\n"
              "**************************************************************\n"
              "DIGITE A OPÇÃO DESEJADA: "))


        match option:
            case 1:
                vocabulary = get_most_relevant_terms()
                index = index_collection(vocabulary)
                print('\nColeção indexada com sucesso!')

            case 2:
                vocabulary = get_most_relevant_terms()
                print('\nVOCABULÁRIO (20 termos mais frequentes):')
                for word, freq in vocabulary.items():
                    print(f'{word}: {freq}')

            case 3:
                vocabulary = get_most_relevant_terms()
                matrix = bool_index(vocabulary)
                print('\nMATRIZ DE OCORRÊNCIAS (0 = não aparece, 1 = aparece):')
                for word, docs in matrix.items():
                    print(f'{word}: {docs}')

            case 4:
                vocabulary = get_most_relevant_terms()
                matrix = index_collection(vocabulary)
                print('\nMATRIZ DE FREQUÊNCIAS:')
                for word, data in matrix.items():
                    print(f'{word}: {data[1]}')

            case 5:
                boolean_model()

            case 0:
                break



if __name__ == "__main__":
    #boolean_model()
    # menu()
    #vocabulary = extract_vocabulary('doc1.txt')
    # result = get_most_relevant_terms() #menu 2
    #print(result)

    # index = bool_index(result)

    menu()

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








