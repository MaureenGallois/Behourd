class Player:

    def __init__(self, json=None, name=None, surname=None, weight=None, subDate=None) :
        if json != None :
            self.init(json["nom"], json["prenom"], json["weight"], json["annee_inscription"])
        else :
            self.init(name, surname, weight, subDate)

    def init(self, name, surname, weight, subscriptionDate):
        self.name = name
        self.surname = surname
        self.weight = weight
        self.subscriptionDate = subscriptionDate

    def __eq__(self, other) :
        return self.name == other.name and self.surname == other.surname and self.weight == other.weight and self.subscriptionDate == other.subscriptionDate

    def __str__(self):
        return "Name : " + self.name + ", Surname "+ self.surname +", Weight " + str(self.weight) + ", Date " + str(self.subscriptionDate)
