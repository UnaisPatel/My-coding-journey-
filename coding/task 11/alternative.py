# This program asks a user to enter a word and then makes alternate character in to capital and the other alternate in to lowercase

sentence = ("Hello world ")
new_sentence = ""
for i, char in enumerate(sentence) :       # using a for loop to go through each character in the word and index it
    if i % 2 == 0 :                        # using modulo 2 so only the even numbers return to an uppercase
        new_sentence += char.upper()       #This makes the character uppercase
    else :
        new_sentence += char.lower()
print (new_sentence)


#This program turns words in to lowercase and the alternate words in to uppercase

sentence_2 = (" i am learning to code ")

alternate_word = sentence_2.split()             # Turns the string in to a list

for i in range(len(alternate_word)):            # iterates through each word in the list. 
    if i % 2 == 0:                              # using modulo 2 again
        alternate_word[i] = alternate_word[i].lower()       # all the words which hold even indexes will be a lowercase
    else:
        alternate_word[i] = alternate_word[i].upper()       # the other words will be uppercase

new_sentence_2 = " ".join(alternate_word)               # joins the list back up in to a string

print(new_sentence_2)

    
    
    

