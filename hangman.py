import random

with open("library.txt","r")as f:
    word=f.readlines()
word=random.choice(word)[:-1]

guesses=[]
allowed_error=5
correct=False

while not correct:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")    
    print(" ") 
  
    guess=input(f"Allowed errors left {allowed_error},next guess:") 
    guesses.append(guess.lower()) 
    if guess.lower()not in word.lower():
        allowed_error -=1
        if allowed_error==0:
            break

    correct=True
    for letter in word:
        if letter.lower()not in guesses:
            correct=False

if correct:
    print(f"You find the word!it was{word}!")  
else:
    print(f"Game over! The word was {word}!")              

 










