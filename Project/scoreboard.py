def create():
    p_count = input("How many players?\n")
    players = {}
    i = 0
    while i < p_count:
        print "Player", i, "please enter your name: ",
        name = raw_input()
        players[name] = "alive"
        i+=1
    return players

def display(players):
    for k in players:
        print k, "-", players[k]

players = create()
display(players)
