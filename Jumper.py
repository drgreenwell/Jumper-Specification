import random

class List:
    def __init__(self): 
        # This currently does nothing.
        pass
        
    def get_word(self): 
        # This returns a word randomly selected from the list. 
        # Feel free to add more words if you want. Code is dynamic enough to adjust to needs.
        wordList = ['beaver', 'cougar', 'donkey', 'ferret', 'lizard', 'monkey', 'parrot', 'rabbit', 'spider']
        return random.choice(wordList)
        

class Jumper:
    # Currently does nothing except print an image of our jumper man.
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
    # This currently does nothing.
    pass

class Continue:
    # This currently does nothing.
    pass

def main():
    # Calls Jumper class to display Jumper Man!
    Jumper()
    # Ties List class to list for use of functions within the class.
    list = List()

    # Runs get_word function within the List class and prints out the result.
    # Remember to get rid of this when we finally get the game put together.
    print(list.get_word())

if __name__ == "__main__":
    main()
