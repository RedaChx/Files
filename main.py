from Personne import personne
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Nom=input("donner votre Nom")
    Prenom=input("denner votre Prenom")
    Age=input("Donner votre age")
    file=open("concour.txt","a")
    file.write(Nom+"  "+";"+"  "+Prenom+"  "+";"+"  "+ str(Age) +"\n")
    file.close()


    f=open("fileTXT.txt","w")

    P1=personne("Ghali","Mohamed",12)
    P2=personne("Maknassi","Salwa",18)
    f.write(P1.__str__())
    f.write(P2.__str__())
    f.close()

    f=open("fileTXT.txt","r")
    """
    ch=f.read()
    print(ch)

    c=f.read(12)
    print(c)

    h=f.readline()
    while h!="":
        print(h)
        h=f.readline()
    """


    L=f.readlines()
    print(len(L))
    print(L[1])
    maliste=L[1].split(";")
    print("age=",maliste[2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
