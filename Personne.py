class personne:

    def __init__(self,nom1,prenom1,age1):
        self.Nom=nom1
        self.Prenom=prenom1
        self.Age=age1

    def __str__(self):
        return self.Nom+"  "+";"+"  "+self.Prenom+"  "+";"+"  "+str(self.Age)+" "+"\n"
