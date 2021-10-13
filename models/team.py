class Team :

    WEIGHT_CATEGORIES = [
        ("Mouche", 52),
        ("Plumes", 57),
        ("Légers", 63),
        ("Welters", 69),
        ("Moyens", 75),
        ("Mi-Lourds", 81),
        ("Lourds", 91),
        ("Super-Lourds", 92)
    ]

    def __init__(self, listPlayer):
        self.listPlayer = listPlayer
        self.avg = self.average()
        self.weight_category = self.initCategory()

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
        return line + ", Average : " + str(self.avg) + ", Weight category : " + self.weight_category

    def average(self):
        avg = 0
        for p in self.listPlayer :
            avg += p.weight
        return avg/self.size()

    def initCategory(self):
        if (self.avg <= self.WEIGHT_CATEGORIES[0][1]):
            return "Mouche"

        if (self.avg >= self.WEIGHT_CATEGORIES[7][1]):
            return "Super-Lourds"
        last_category = self.WEIGHT_CATEGORIES[0]
        for category in self.WEIGHT_CATEGORIES:
            if (self.avg >= last_category[1] and self.avg <= category[1]):
                return category[0]
            last_category = category

    def append(self,guest) :
        self.listPlayer.append(guest)
        self.avg = self.average()
        self.weight_category =self.initCategory()

    def size(self) :
        return len(self.listPlayer)