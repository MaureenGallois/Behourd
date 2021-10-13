from models.team import Team
from models.player import Player
import itertools

class Game:

    def __init__(self, listPlayer) :
        self.create(listPlayer)

    def create(self, listPlayer) :
        teamA = []
        teamB = []
        i = 1
        listPlayer = sorted(listPlayer, key= lambda p: p.weight)

        for player in listPlayer :
            if i%2 == 0:
                teamA.append(player)
            else :
                teamB.append(player)
            i += 1
        self.teamA = Team(teamA)
        self.teamB = Team(teamB)

    def addAGuest(self, guest):
        ##Dans le cas où les deux listes sont de même taille
        if(self.teamA.size() == self.teamB.size()):
            ##Dans le cas où les deux avg sont égaux on ajoute dans la team A par défaut
            if(self.teamA.avg == self.teamB.avg):
                self.teamA.append(guest)

            ##Dans le cas où l'average de la teamA est inférieur à celui de la teamB
            elif (self.teamA.avg < self.teamB.avg):
                ##Si l'average de la teamA et l'average de la teamB sont inférieur au poids de
                ##l'invité, on l'ajoute dans la teamB qui a le plus gros average
                if(self.teamA.avg <= guest.weight and self.teamB.avg <= guest.weight):
                    self.teamA.append(guest)

                ##Dans le cas où l'average de la team A et celui de la teamB sont supérieur ou égaux au
                ##poids l'invité, on l'ajoute dans la teamA qui à l'average le plus petit
                elif(self.teamA.avg >= guest.weight and self.teamB.avg >= guest.weight):
                    self.teamB.append(guest)

                ##Dans le cas où le poids de l'invité se situe entre les deux averages
                else :
                    ##Si la différence entre l'average de teamB et le poids de l'invité est supérieur a
                    ##celle du poids de l'invité et de l'average de teamA, on ajoute dans teamB
                    ##Sinon on ajoute dans teamA
                    if(self.teamB.avg - guest.weight > guest.weight - self.teamA.avg):
                        self.teamB.append(guest)
                    else :
                        self.teamA.append(guest)

            ##La même chose que le bloc d'avant mais en inversant les teams
            elif(self.teamB.avg < self.teamA.avg):
                if(self.teamB.avg < guest.weight and self.teamA.avg < guest.weight):
                    self.teamB.append(guest)

                elif(self.teamB.avg >= guest.weight and self.teamA.avg >= guest.weight):
                    self.teamA.append(guest)

                else :
                    if(self.teamA.avg - guest.weight > guest.weight - self.teamB.avg):
                        self.teamA.append(guest)
                    else :
                        self.teamB.append(guest)

        ##Dans le cas de teams non égales en taille on ajoute dans la plus petite
        elif(len(self.teamA.listPlayer) < len(self.teamB.listPlayer)):
                self.teamA.append(guest)
        else :
                self.teamB.append(guest)