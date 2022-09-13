import random
height = int(input("Type a height:"))
width = int(input("Type a width:"))
tree = "T"
river = "-"
grass = " "
rock = "€"
size = height * width
tngs = [tree, grass]
treerandom = 0
rockrandom = 0
t = random.randrange(1, 15)
generations = int(input("How many generations you want?:"))

def generalas():
    for i in range(height):
        print("")
        for a in range(width):
            treerandom = random.randrange(1, 10)
            t = random.randrange(1, 10)
            rockrandom = random.randrange(1, 30)
            r = random.randrange(1, 30)
            if treerandom == t:
                print(tree, end="")
            else:
                if rockrandom == r:
                   print(rock, end="")
                else:
                    print(grass, end="")
    if generations > 1:
        print("")
        for e in range(width):
          print("-", end="")
          print("", end="")


for i in range(generations):
    generalas()
