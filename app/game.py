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

    def create(listePlayer) :
        teamA, teamB = []
        listePlayer.sort(key= lambda p: p.get("weight"))
        for i, player in listePlayer :
            if i%2:
                teamA.append(player)
                avgA = avgA + player.weight
            else :
                teamB.append(player)
                avgB = avgB + player.weight
        avgA = avgA / len(teamA)
        avgB = avgB / len(teamB)

        return Team(teamA, avgA), Team(teamB, avgB)