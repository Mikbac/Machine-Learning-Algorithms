# Normalization and n-grams
## Normalization
* getExperimentalNormalization(string n, int nGram)
    ##### Example:
    In:
    ```
    ('Givennn, an array arr[] of size N [...] is 256', 1)
    ```
    Out:
    ```
    ['givennn', 'array', 'arr', 'size']
    ```
  
* getHandmadeNormalization(string n, int nGram)
    ##### Example:
    In:
    ```
    ('Givennn, an array arr[] of size N [...] is 256', 1)
    ```
    Out:
    ```
    ['givennn', 'an', 'array', 'arr', 'of', 'size', 'n', 'is']
    ```

* getNLTKNormalization(string n, int nGram)
    ##### Example:
    In:
    ```
    ('Givennn, an array arr[] of size N [...] is 256', 1)
    ```
    Out:
    ```
    ['givennn', 'array', 'arr', 'size', 'n']
    ```
## n-grams
* getNGramTuples(string_List words, int nGram)
    ##### Example:
    In:
    ```
    (['aaa', 'bbb', 'ccc'], 2)
    ```
    Out:
    ```
    [('aaa', 'bbb'), ('bbb', 'ccc'), 'aaa', 'bbb', 'ccc']
    ```
 * getNGramList(string_List words, int nGram)
     ##### Example:
     In:
     ```
     (['aaa', 'bbb', 'ccc'], 2)
     ```
     Out:
     ```
     [['aaa', 'bbb'], ['bbb', 'ccc'], 'aaa', 'bbb', 'ccc']
     ```