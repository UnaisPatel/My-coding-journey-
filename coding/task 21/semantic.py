import spacy 
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word1.similarity(word1))

tokens = nlp('car fuel grape tea ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# cat and monkey are more similar than cat and banana or monkey and banana because they are both animals. 
# However, monkey and banana are more similar than cat and banana maybe because monkeys eat bananas.

# when you use en_core_web_sm it shows that all the words are more similar
    