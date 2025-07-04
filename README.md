# Sistema de Recuperação de Informação

Este projeto implementa um sistema simples de recuperação de informação, capaz de indexar uma coleção de documentos, gerar vocabulário, criar matrizes de ocorrência e frequência, e realizar buscas utilizando os modelos Booleano e Vetorial.

## Como executar

1. **Pré-requisitos:**
   - Python 3.10 ou superior (devido ao uso do `match-case`)
   - Instale as dependências:
     ```bash
     pip install numpy pandas
     ```
2. **Execute o programa:**
   ```bash
   python main.py
   ```

3. **Siga o menu interativo** para acessar as funcionalidades.

## Estrutura dos Documentos
- Os arquivos de texto (`doc1.txt`, `doc2.txt`, ..., `doc360.txt`) devem estar na mesma pasta do `main.py`.

## Funcionalidades do Menu

- **1 - Indexar a coleção:**
  - Gera o índice invertido dos termos mais relevantes da coleção.
- **2 - Imprimir o vocabulário:**
  - Mostra os 50 termos mais frequentes da coleção.
- **3 - Imprimir a matriz de ocorrências:**
  - Exibe uma matriz indicando se cada termo aparece (1) ou não (0) em cada documento.
- **4 - Imprimir a matriz de frequências:**
  - Exibe a frequência de cada termo nos documentos.
- **5 - Aplicar o modelo booleano:**
  - Permite consultas usando operadores lógicos (AND, OR, NOT).
- **6 - Consulta para o modelo vetorial:**
  - Calcula a similaridade entre a consulta e os documentos usando TF-IDF e produto escalar.
- **0 - Sair:**
  - Encerra o programa.

## Explicação das Funções Principais

### 1. `extract_vocabulary(fileName)`
Lê um arquivo de texto, extrai palavras com mais de 2 caracteres que não sejam stopwords e retorna uma lista dessas palavras em minúsculo.

### 2. `create_dictionary(fileName)`
Cria um dicionário com a frequência de cada termo extraído de um arquivo.

### 3. `create_collection_dictionary()`
Cria um dicionário para toda a coleção, onde cada chave é o nome do documento e o valor é o dicionário de frequência de termos desse documento.

### 4. `get_most_relevant_terms()`
Gera um dicionário com os 50 termos mais frequentes em toda a coleção.

### 5. `index_collection(vocabulary)`
Cria um índice invertido: para cada termo do vocabulário, armazena a frequência total e um dicionário com a frequência em cada documento.

### 6. `bool_index(vocabulary)`
Gera uma matriz booleana indicando se cada termo aparece (1) ou não (0) em cada documento.

### 7. `boolean_model()`
Permite ao usuário fazer consultas booleanas (com AND, OR, NOT) sobre o vocabulário indexado, mostrando os documentos que satisfazem a consulta.

### 8. `vetorial_model(term1, term2)`
Calcula a similaridade entre a consulta (dois termos) e todos os documentos usando o modelo vetorial com TF-IDF e produto escalar, normalizando os resultados.

### 9. `menu()`
Exibe o menu interativo e chama as funções conforme a opção escolhida pelo usuário.

### 10. Funções auxiliares
- `words_in_vocabulary(words, vocabulary)`: Verifica se os termos da consulta estão no vocabulário.
- `calculate_result(wordsAndOperators, consult_boolean)`: Calcula o resultado de uma consulta booleana.
- `calculate_operator(consult, consult_boolean)`: Executa a operação booleana entre dois termos.

## Observações
- O código utiliza `match-case`, disponível apenas no Python 3.10+.
- As consultas booleanas aceitam até dois operadores (AND, OR, NOT).
- O modelo vetorial aceita apenas dois termos por consulta.

---

**Autores:** Leandro & Poliana 