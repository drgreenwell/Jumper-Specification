import random

class List:
    def __init__(self):
        # This function sets up our word list
        wordList = []
        
    def get_word(self):
        wordList = ['beaver', 'cougar', 'donkey', 'ferret', 'lizard', 'monkey', 'parrot', 'rabbit', 'spider']
        return random.choice(wordList)
        

class Jumper:
    def __init__(self):
        print("  ___  ")
        print(" /___\ ")
        print(" \   / ")
        print("  \ /  ")
        print("   0   ")
        print("  /|\  ")
        print("  / \  ")
        print("")
        print("^^^^^^^")

class Letters:
    pass

class Continue:
    pass

def main():
    Jumper()
    list = List()

    print(list.get_word())

if __name__ == "__main__":
    main()
