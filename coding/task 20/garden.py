import spacy                            # importing spacy 
nlp = spacy.load('en_core_web_sm')      # importing the english version

# making a list 
gardenpathSentences = ['I convinced her children are noisy', 'The complex houses married and single soldiers and their families.']
gardenpathSentences.append('Mary gave the child a band aid')
gardenpathSentences.append('That Jill is never here hurts')                       # adding to the end of the list 
gardenpathSentences.append('The cotton clothing is made of grows in Mississipi')

#using for loop
for sentence in gardenpathSentences :
    doc = nlp(sentence)       
    for token in doc :                       # tokenizing each sentence
        print(token, token.orth_, token.orth)
    #using an if statement to check if there are any named entities
        if token.ent_type_:
            print("ENTITY:", token.text, token.ent_type_)   # performing named entity recognition

# using the spacy.explain function to get the explanation of entities
entity_explain = spacy.explain("PERSON")
print(entity_explain)

# Two entities i looked up :
# GPE : it means countries cities and states and it did make sense with the words around it 
# PERSON : it means people including fictional and it did make sense with the words around it


    

      