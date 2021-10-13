from pytest import *
from app.game import Game
from models.team import Team
from models.player import Player
import json

with open("player.json", "r") as players:
        data = json.load(players)

def test_init_category():
    listPlayers = [
        Player(data["players"][0]),
        Player(data["players"][1]),
        Player(data["players"][2]),
        Player(data["players"][3])
    ]

    game = Game(listPlayers)

    print(game.teamA.weight_category)
    print(game.teamB.weight_category)

    assert game.teamA.weight_category == "Lourds"
    assert game.teamB.weight_category == "Lourds"


def test_count_players() :

    listPlayers = [
        Player(data["players"][0]),
        Player(data["players"][1]),
        Player(data["players"][2]),
        Player(data["players"][3])
    ]

    game = Game(listPlayers)
    assert game.teamA.size() == game.teamB.size()

    listPlayers.append(Player(data["players"][4]))
    game.create(listPlayers)
    assert game.teamA.size()+1 == game.teamB.size() or game.teamA.size() == game.teamB.size() +1

def test_sort_teams() :

    listPlayers = [
        Player(data["players"][0]),
        Player(data["players"][1]),
        Player(data["players"][2]),
        Player(data["players"][3])
    ]

    game = Game(listPlayers)

    assert game.teamA.__eq__(Team([Player(data["players"][1]), Player(data["players"][0])]))
    assert game.teamB.__eq__(Team([Player(data["players"][2]), Player(data["players"][3])]))


def test_add_a_guest():

    listPlayers = [
        Player(data["players"][0]),
        Player(data["players"][1]),
        Player(data["players"][2]),
        Player(data["players"][3])
    ]
    game = Game(listPlayers)


    game.addAGuest(Player(data["players"][4]))

    assert game.teamA.__eq__(Team([Player(data["players"][1]), Player(data["players"][0]),Player(data["players"][4])]))
    assert game.teamB.__eq__(Team([Player(data["players"][2]), Player(data["players"][3])]))


    game.addAGuest(Player(data["players"][5]))

    assert game.teamA.__eq__(Team([Player(data["players"][1]), Player(data["players"][0]), Player(data["players"][4])]))
    assert game.teamB.__eq__(Team([Player(data["players"][2]), Player(data["players"][3]), Player(data["players"][5])]))

    game.addAGuest(Player(data["players"][6]))

    print(game.teamA)

    assert game.teamA.__eq__(Team([Player(data["players"][1]), Player(data["players"][0]), Player(data["players"][4]),Player(data["players"][6])]))
    assert game.teamB.__eq__(Team([Player(data["players"][2]), Player(data["players"][3]), Player(data["players"][5])]))



def test_delete_player():
    listPlayers = [
        Player(data["players"][0]),
        Player(data["players"][1]),
        Player(data["players"][2]),
        Player(data["players"][3])
    ]

    game = Game(listPlayers)

    game.deletePlayer(Player(data["players"][2]))

    assert game.teamA.__eq__(Team([Player(data["players"][0]), Player(data["players"][1]), Player(data["players"][3])]))


def test_equlibrate_team() :
    listPlayers = [
            Player(data["players"][0]),
            Player(data["players"][1]),
            Player(data["players"][2]),
            Player(data["players"][3])
        ]
    game = Game(listPlayers)

    assert game.teamA.__eq__(Team([Player(data["players"][1]), Player(data["players"][0])]))
    assert game.teamB.__eq__(Team([Player(data["players"][2]), Player(data["players"][3])]))
