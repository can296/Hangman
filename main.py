from random import randint
from time import time
from os import system
from termcolor import colored

print(".\n\n\nDifficulty: with 'easy' u will have to guess short and common words while with 'hard' u will have to guess longer and harder words. With extreme option you will have 4 consecutives words with more than 13 letters each one. Good Luck!. If u write anything else u will have automatically 'easy' mode:\n 'easy'/'hard'/'extreme':")

dificil=str(input())
system("clear")
word=[None]
letras_disponibles=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]

def cambiar_letra():
    with open("text.txt","r") as archivo:
        x=randint(1,62)
        i=1
        for linea in archivo:
            if i==x:
                word[0]=linea
                i+=1
            else:
                i+=1
        word[0]=word[0].replace("\n","")
        x=randint(1,62)
        i=1
        archivo.close()
    return word[0]


def cambiar_letra_hard():
    with open("hard.txt","r") as archivo:
        x=randint(1,59)
        i=1
        for linea in archivo:
            if i==x:
                word[0]=linea
                i+=1
            else:
                i+=1
        word[0]=word[0].replace("\n","")
        x=randint(1,59)
        i=1
        archivo.close()
    return word[0]


def cambiar_letra_extreme():
    with open("extreme.txt","r") as archivo:
        x=randint(1,93)
        i=1
        for linea in archivo:
            if i==x:
                word[0]=linea
                i+=1
            else:
                i+=1
        word[0]=word[0].replace("\n","")
        x=randint(1,93)
        i=1
        archivo.close()
    return word[0]

if dificil=="Unit 6":
    palabra=cambiar_letra_hard()
elif dificil=="extreme":
    palabra=cambiar_letra_extreme()
else:
    palabra=cambiar_letra()

    
espacios=""
game_is_over=False
for i in range(len(palabra)):
    espacios=espacios+"_"

hangman=["","            \n            \n            \n             \n            \n      \n   ______","            \n     |      \n     |      \n     |       \n     |      \n     |\n   ______","     -------\n     |      \n     |      \n     |       \n     |      \n     |\n   ______","     -------\n     |     |\n     |      \n     |       \n     |      \n     |\n   ______","     -------\n     |     |\n     |     0\n     |       \n     |      \n     |\n   ______","     -------\n     |     |\n     |     0\n     |     | \n     |      \n     |\n   ______","     -------\n     |     |\n     |     0\n     |    -| \n     |      \n     |\n   ______","     -------\n     |     |\n     |     0\n     |    -|-\n     |      \n     |\n   ______","     -------\n     |     |\n     |     0\n     |    -|-\n     |     ^\n     |\n   ______"]

count_hang=0
won=False

while game_is_over == False:
    print("Guess the word by trying letters!\n->",end=" ")
    for espacio in espacios:
        print(colored(espacio,"green"),end=" ")
    print("\n")
    print(colored(hangman[count_hang],"red"))
    
    print("\nAvailable letters:\n")
    for i in range(len(letras_disponibles)):
        print(letras_disponibles[i],end=" ")
    print("\n\nWrite 1 letter:")
    letra=str(input())
    while(len(letra))==0 or (len(letra))>1:
        print("U can only type 1 letter:")
        letra=str(input())
    for k in range(len(letras_disponibles)-1):
        if(letra==letras_disponibles[k]):
            letras_disponibles.pop(k)
    system("clear")
    
    contador=1
    posiciones=[]
    for letras in palabra:
        if letra==letras:
            posiciones.append(contador)
        contador=contador+1
    if len(posiciones)==0:
        count_hang+=1
        if count_hang>8:
            game_is_over=True
    else:
        list_palabra=list(palabra)
        list_espacios=list(espacios)
        for j in range(len(posiciones)):
            list_espacios[posiciones[j]-1]=list_palabra[posiciones[j]-1]
        espacios="".join(list_espacios)
        if espacios==palabra:
            system("clear")
            print("You found the word!\n",colored(palabra,"green"))
            game_is_over=True
            won=True
            
if won==False:
    system("clear")
    print("You failed, the word was",colored(palabra,"red"),". Try again!")