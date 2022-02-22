from random import randint

def main():
    word = getword()

def openwordlist():
    f = open('words.txt', r)
    words = f.read()
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
    word = lower(words[index])
    return word

def guess(word):
    current = ['_','_','_','_','_','_','_']
    errors = True
    for i in range(0,7):
        while errors:
            print("enter your first attempt")
            guess = input()
            if len(guess) != 7:
                print("input must be 7 characters")
            elif not checkword(guess):
                print("word no in word list")
            else:
                errors = False
        if guess = word:
            print(f"woo! got it in {i}")
            exit(0)
        guess = guess.split()
        for l in range(len(guess)):
            if guess[l] == word[l]:
                current[l]=f"\033[1;32;40m{guess[l]}"
            elif guess[l] in word:
                current[l]=f'\033[1;33;40m{guess[l]}'
        print(current[l])
    print(f'todays word was {word}')
