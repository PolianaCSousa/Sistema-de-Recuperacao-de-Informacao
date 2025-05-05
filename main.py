
def index_collection():
    #first step: to index the collection we need to read it
    print('Método para indexar a coleção')
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
    menu()









