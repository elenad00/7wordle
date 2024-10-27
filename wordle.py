from random import randint
from colorama import Fore as fore

def main():
    word = getword()
    print("Welcome to Wordle!")
    print("Enter your first word")
    guess(word)

def getwordlist() -> list:
    f = open('5words.txt', 'r')
    words = f.read()
    words = words.split()
    return words

def checkword(word) -> bool:
    words = getwordlist()
    return True if word in words else False

def getword() -> str:
    words = getwordlist()
    index = randint(0,len(words))
    word = words[index].lower()
    return word

def guess(word: str):
    used_letters = []
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
            print(f"woo! got it in {i}" + fore.RESET)
            exit(0)
        current = list(guess)
        for l in range(0,len(word)):
            if guess[l] == word[l]:
                current[l]=fore.GREEN + guess[l]
            elif guess[l] in word:
                current[l]=fore.YELLOW + guess[l]
            else:
                current[l]=fore.RESET + guess[l]
            if guess[l] not in used_letters:
                used_letters.append(guess[l])
        print(''.join(current) + fore.RESET)
        used_letters.sort()
        print(f"Letters used: {used_letters}")
    print(f'Todays word was: {word}')
    exit(0)

main()
