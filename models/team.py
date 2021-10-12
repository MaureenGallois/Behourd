class Team :

    def __init__(self, listPlayer, avg):
        self.listPlayer = listPlayer
        self.avg = avg

    def __eq__(self, other) :
        i = 0
        isEquals = len(self.listPlayer) == len(other.listPlayer) and self.avg == other.avg
        while(isEquals and i != len(self.listPlayer)):
            isEquals = self.listPlayer[i].__eq__(other.listPlayer[i])
            i = i + 1
        return isEquals

    def __str__(self):
        line = ""
        for player in self.listPlayer :
            line = line + str(player) + " "
        return line + ", Average " + str(self.avg)