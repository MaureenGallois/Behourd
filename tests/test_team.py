from pytest import *
from models.team import Team
from models.player import Player

def count_players() :
    playerList = [
        Player("GROS", "Paul", 134,	2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79,	1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]
    teamA, teamB = Team.create(playersList)
    assert len(teamA) == len(teamB)

    playersList.append("DUTROU", "Jacques", 69, 1999)
    teamA, teamB = Team.create(playersList)
    assert len(teamA)+1 == len(teamB) or len(teamA) == len(teamB) +1

def sort_teams() :
    playerList = [
        Player("GROS", "Paul", 134, 2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79, 1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]
    teamA, teamB = Team.create(playersList)

    assert teamA.equals([Player("GROS", "Paul", 134, 2006),
                        Player("BLANC", "Louis", 47, 2020)])
    assert teamB.equals([Player("GIRAUD", "Jean-Michel", 79, 1987),
                        Player("PÂRIS",	"Théophile", 102, 2003)])