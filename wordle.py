from random import randint
from colorama import Fore as fore

def main():
    word = getword()
    guess(word)

def getwordlist():
    f = open('5words.txt', 'r')
    words = f.read()
    words = words.split()
    return words

def checkword(word):
    words = getwordlist()
    if word in words:
        return True
    else:
        return False

def getword():
    words = getwordlist()
    index = randint(0,len(words))
    word = words[index].lower()
    return word

def guess(word):
    for i in range(0,len(word)):
        errors = True
        while errors:
            guess = input()
            if len(guess) != len(word):
                print(f"input must be {len(word)}characters")
            elif not checkword(guess):
                print("word not in word list")
            else:
                errors = False
        if guess == word:
            print(fore.GREEN + guess)
            print(f"woo! got it in {i}")
            exit(0)
        current = list(guess)
        for l in range(0,len(word)):
            if guess[l] == word[l]:
                current[l]=fore.GREEN + guess[l]
            elif guess[l] in word:
                current[l]=fore.YELLOW + guess[l]
            else:
                current[l]=fore.RESET + guess[l]
        print(''.join(current) + fore.RESET)
    print(f'todays word was {word}')
    exit(0)

main()
