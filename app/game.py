from models.team import Team
from models.player import Player

class Game:

    WEIGHT_CATEGORIES = [
        {"Mouche" : 52},
        {"Plumes" : 57},
        {"Légers" : 63},
        {"Welters" : 69},
        {"Moyens" : 75},
        {"Mi-Lourds" : 81},
        {"Lourds" : 91},
        {"Super-Lourds" : 92}
    ]

    def __init__(self) :
        pass

    def create(listPlayer) :
        teamA = []
        teamB = []
        avgA = 0
        avgB = 0
        i = 1
        j = len(listPlayer)
        listPlayer = sorted(listPlayer, key= lambda p: p.weight)
        for player in listPlayer :
            if i%2 == 0:
                teamA.append(player)
                avgA = avgA + player.weight
            else :
                teamB.append(player)
                avgB = avgB + player.weight
            i += 1
        avgA = avgA / len(teamA)
        avgB = avgB / len(teamB)

        return Team(teamA, avgA), Team(teamB, avgB)