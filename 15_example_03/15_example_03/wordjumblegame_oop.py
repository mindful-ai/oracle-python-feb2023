import random

class wordjumblegame(object):

    def __init__(self, name, level) -> None:
        self.name = name
        self.points = 0
        self.level = level
        self.words = self.loadwords(self.level)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def banner(self):
        print("-------------------------------------------------------")
        print("            WELCOME TO WORD JUMBLE GAME                ")
        print("-------------------------------------------------------")
        print("          The computer presents a jumbled word.        ")
        print("                You need to guess it                   ")
        print("-------------------------------------------------------")
        print("NAME  :", self.name)
        print("LEVEL :", self.level)
        print("*******************************************************")
        print("\n")


    def loadwords(self, level):
        path = str(level) + ".txt"
        with open(path) as file:
            temp = file.readlines()
            return [s.strip() for s in temp]
        
    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        self.banner()
        random.shuffle(self.words)
        for word in self.words:
            jword = self.jumble(word)
            print("Jumbled Word -> ", jword)
            uword = input("Can you guess? ")
            if(uword == word):
                self.points += 1
                print("Correct!")
            else:
                print("Incorrect.")
            print("\n")
        self.printinfo()

    def score(self):
        return self.points

    def printinfo(self):
        print("*******************************************************")
        print("NAME   :", self.name)
        print("LEVEL  :", self.level)
        print("SCORE  :", self.points)
        if(self.points > 6):
            print("RESULT : Excellent Playing")
        elif(3 <= self.points <= 6):
            print("RESULT : Good Playing")
        else:
            print("RESULT : Needs Improvement")
        print("-------------------------------------------------------")
                

# --------------------------------------------------------

if __name__ == "__main__":


    # Inital test
    ''' 
    p = wordjumblegame("Anil", 2)
    print(getattr(p, "words"))
    p.run()
    print(p.score())
    '''


    # Multiplayer test
    D = {"Anil": 2, "Sunil": 1, "Ram": 1}
    players = [wordjumblegame(player, level) for player, level in D.items()]
    for player in players:
        player.run()

    results = {}
    for player in players:
        key = getattr(player, "name")
        score = player.score()
        level = getattr(player, "level")
        results[key] = {"score":score, "level":level}

    print(results)
