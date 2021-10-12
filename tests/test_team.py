from pytest import *
from app.game import Game
from models.team import Team
from models.player import Player


def test_init_category():
    listPlayers = [
        Player("GROS", "Paul", 134,	2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79,	1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]

    teamA, teamB = Game.create(listPlayers)

    assert teamA.weight_category == "Super-Lourds"
    assert teamB.weight_category == "Moyens"


def test_count_players() :

    listPlayers = [
        Player("GROS", "Paul", 134,	2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79,	1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]

    teamA, teamB = Game.create(listPlayers)
    assert len(teamA.listPlayer) == len(teamB.listPlayer)

    listPlayers.append(Player("DUTROU", "Jacques", 69, 1999))
    teamA, teamB = Game.create(listPlayers)
    assert len(teamA.listPlayer)+1 == len(teamB.listPlayer) or len(teamA.listPlayer) == len(teamB.listPlayer) +1

def test_sort_teams() :

    listPlayers = [
        Player("GROS", "Paul", 134,	2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79,	1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]

    teamA, teamB = Game.create(listPlayers)

    assert teamA.__eq__(Team([Player("GIRAUD", "Jean-Michel", 79, 1987), Player("GROS", "Paul", 134, 2006)]))
    assert teamB.__eq__(Team([Player("BLANC", "Louis", 47, 2020), Player("PÂRIS", "Théophile", 102, 2003)]))


def test_add_a_guest():

    listPlayers = [
        Player("GROS", "Paul", 134,	2006),
        Player("BLANC", "Louis", 47, 2020),
        Player("GIRAUD", "Jean-Michel", 79,	1987),
        Player("PÂRIS",	"Théophile", 102, 2003)
    ]

    teamA, teamB = Game.create(listPlayers)

    Game.addAGuest(teamA, teamB, Player("DUTROU", "Jacques", 80, 1999))

    assert teamA.__eq__(Team([Player("GIRAUD", "Jean-Michel", 79, 1987), Player("GROS", "Paul", 134, 2006),Player("DUTROU", "Jacques", 80, 1999)]))
    assert teamB.__eq__(Team([Player("BLANC", "Louis", 47, 2020), Player("PÂRIS", "Théophile", 102, 2003)]))


    Game.addAGuest(teamA, teamB, Player("DURAND", "Martin", 130, 1999))

    assert teamA.__eq__(Team([Player("GIRAUD", "Jean-Michel", 79, 1987), Player("GROS", "Paul", 134, 2006),Player("DUTROU", "Jacques", 80, 1999)]))
    assert teamB.__eq__(Team([Player("BLANC", "Louis", 47, 2020), Player("PÂRIS", "Théophile", 102, 2003), Player("DURAND", "Martin", 130, 1999)]))

    Game.addAGuest(teamA, teamB, Player("JEAN", "Arthur", 96, 1999))

    assert teamA.__eq__(Team([Player("GIRAUD", "Jean-Michel", 79, 1987), Player("GROS", "Paul", 134, 2006),Player("DUTROU", "Jacques", 80, 1999)]))
    assert teamB.__eq__(Team([Player("BLANC", "Louis", 47, 2020), Player("PÂRIS", "Théophile", 102, 2003), Player("DURAND", "Martin", 130, 1999),Player("JEAN", "Arthur", 96, 1999)]))




