import csv
from Personne import personne
fichier=open("annuaire.csv","w")
ecrivainCSV=csv.writer(fichier,delimiter=";")
ecrivainCSV.writerow(["Nom","Prenom","Telephone"])
ecrivainCSV.writerow(["Dubois","Marie","0198549372"])
ecrivainCSV.writerow(["Duval","Julien","0399741052"])
ecrivainCSV.writerow(["Jacquet","Bernard","0200749685"])
ecrivainCSV.writerow(["Martin","Julie","0399731590"])
fichier.close()


file=open("annuaire1.csv","w")
ecrivainCSV=csv.writer(file,delimiter=";")

P0=personne("NOM","PRENOM","AGE")
P1=personne("Ghali","Mohamed",11)
P2=personne("Maknassi","Salwa",18)
L0=P0.__str__().split(";")
L1=P1.__str__().split(";")
L2=P2.__str__().split(";")
ecrivainCSV.writerow(L0)
ecrivainCSV.writerow(L1)
ecrivainCSV.writerow(L2)
file.close()

file2=open("annuaire.csv","r")
lecteurCSV=csv.reader(file2,delimiter=";")
for ligne in lecteurCSV:
    print(ligne)
file2.close()

file3=open("annuaire.csv","r")
lecteurCSV=csv.DictReader(file3,delimiter=";")
for ligne in lecteurCSV:
    print(ligne)
file3.close()
