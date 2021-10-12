from models.team import Team
from models.player import Player

class Game:

    def __init__(self) :
        pass

    def create(listPlayer) :
        teamA = []
        teamB = []
        i = 1
        j = len(listPlayer)
        listPlayer = sorted(listPlayer, key= lambda p: p.weight)

        for player in listPlayer :
            if i%2 == 0:
                teamA.append(player)
            else :
                teamB.append(player)
            i += 1

        return Team(teamA), Team(teamB)

    def addAGuest(teamA, teamB, guest):
        ##Dans le cas où les deux listes sont de même taille
        if(len(teamA.listPlayer) == len(teamB.listPlayer)):
            ##Dans le cas où les deux avg sont égaux on ajoute dans la team A par défaut
            if(teamA.avg == teamB.avg):
                teamA.append(guest)

            ##Dans le cas où l'average de la teamA est inférieur à celui de la teamB
            elif (teamA.avg < teamB.avg):
                ##Si l'average de la teamA et l'average de la teamB sont inférieur au poids de
                ##l'invité, on l'ajoute dans la teamB qui a le plus gros average
                if(teamA.avg <= guest.weight and teamB.avg <= guest.weight):
                    teamA.append(guest)

                ##Dans le cas où l'average de la team A et celui de la teamB sont supérieur ou égaux au
                ##poids l'invité, on l'ajoute dans la teamA qui à l'average le plus petit
                elif(teamA.avg >= guest.weight and teamB.avg >= guest.weight):
                    teamB.append(guest)

                ##Dans le cas où le poids de l'invité se situe entre les deux averages
                else :
                    ##Si la différence entre l'average de teamB et le poids de l'invité est supérieur a
                    ##celle du poids de l'invité et de l'average de teamA, on ajoute dans teamB
                    ##Sinon on ajoute dans teamA
                    if(teamB.avg - guest.weight > guest.weight - teamA.avg):
                        teamB.append(guest)
                    else :
                        teamA.append(guest)

            ##La même chose que le bloc d'avant mais en inversant les teams
            elif(teamB.avg < teamA.avg):
                if(teamB.avg < guest.weight and teamA.avg < guest.weight):
                    teamB.append(guest)

                elif(teamB.avg >= guest.weight and teamA.avg >= guest.weight):
                    teamA.append(guest)

                else :
                    if(teamA.avg - guest.weight > guest.weight - teamB.avg):
                        teamA.append(guest)
                    else :
                        teamB.append(guest)

        ##Dans le cas de teams non égales en taille on ajoute dans la plus petite
        elif(len(teamA.listPlayer) < len(teamB.listPlayer)):
                teamA.append(guest)
        else :
                teamB.append(guest)