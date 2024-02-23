import json
from Personne import personne

dictio={"cahiers":123, "stylos":{"rouge":41,"bleu":74},"gommes":85}

fichier=open("founitures1.json","w")
ch=json.dumps(dictio)
fichier.write(ch)
fichier.close()

fichier=open("founitures1.json","r")
ch=fichier.read()
dict=json.loads(ch)
print(dict)
fichier.close()

"""
def __str__(self):
    return "{Nom:+self.nom+Prenom:+self.prenom+Age:+str(self.age)}"
"""

P1=personne("Ghali","Mohamed",11)
P2=personne("Maknassi","Salwa",18)
fichier=open("dictPers.json","w")
dictio={}
dictio.update({"Personne1":P1.__str__()})
dictio.update({"Personne2":P2.__str__()})

ch=json.dumps(dictio)
fichier.write(ch)
fichier.close()

