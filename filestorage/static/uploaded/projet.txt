import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

class Tubercule():
    def __init__(self,localite):
        self.local = localite

class Igname(Tubercule):
    def __init__(self,localite,nomIgname,QtIgname,prixUnitaireIg):
        Tubercule.__init__(self,localite)
        self.nom = nomIgname
        self.QtIgname = QtIgname
        self.prixUnitaire = prixUnitaireIg
        self.localite = localite
        Igname.dico = {}
        Igname.dico["le nom est:"]=self.nom
        Igname.dico["la Quantité:"]=self.QtIgname
        Igname.dico["PrixUnitaire:"]=self.prixUnitaire
        Igname.dico["localite"]=self.localite

    def QR(self):
        import qrcode
        img = qrcode.make(Igname.dico)
        img.save("img.png")
        print("le qr code est généré")

    def AfficheIgname(self):
        image = mpimg.imread("img.png")
        plt.imshow(image)
        plt.show()

I1 = Igname("treichville","igname","12kg","100f")
I1.QR()
I1.AfficheIgname()

class PommedeTerre(Tubercule):
    def __init__(self,localite,nomPomme,QtPomme,prixUnitairePo):
        Tubercule.__init__(self,localite)
        self.nom = nomPomme
        self.Qt = QtPomme
        self.prixUnitaire = prixUnitairePo
        self.localite = localite
        PommedeTerre.dico = {}
        PommedeTerre.dico["le nom est:"]=self.nom
        PommedeTerre.dico["la Quantité:"]=self.Qt
        PommedeTerre.dico ["PrixUnitaire:"]=self.prixUnitaire
        PommedeTerre.dico ["localite"]=self.localite

    def QR(self):
        import qrcode
        img = qrcode.make(PommedeTerre.dico)
        img.save("img.png")
        print("le qr code est généré")
    
    def AffichePomme(self):
            image = mpimg.imread("img.png")
            plt.imshow(image)
            plt.show()

Po = PommedeTerre("treichville","Pomme","12kg","100f")
Po.QR()
Po.AffichePomme()



class Banane(Tubercule):
    def __init__(self,nomBanane,QtBanane,prixUnitaireBa):
        Tubercule.__init__(self,localite,nomBanane,QtBanane,prixUnitaireBa)
        self.nom = nomBanane
        self.Qt = QtBanane
        self.prixUnitaire = prixUnitaireBa
        self.localite = localite
        Banane.dico = {}
        Banane.dico["le nom est:"]=self.nom
        Banane.dico["la Quantité:"]=self.Qt
        Banane.dico ["PrixUnitaire:"]=self.prixUnitaire
        Banane.dico ["localite"]=self.localite
    
    def QR(self):
        import qrcode
        img = qrcode.make(Banane.dico)
        img.save("img.png")
        print("le qr code est généré")
    
    def AfficheBanane(self):
            image = mpimg.imread("img.png")
            plt.imshow(image)
            plt.show()


class Patate(Tubercule):
    def __init__(self,nomPa,QtPatate,prixUnitairePa):
        Tubercule.__init__(self,localite,nomPa,QtPatate,prixUnitairePa)
        self.nom = nomPatate
        self.Qt = QtPatate
        self.prixUnitaire = prixUnitairePa
        self.localite = localite

    def AfficheBanane(self):
            print(self.localite)

    
    




class Epice():
     def __init__(self,localite):
            self.local = localite

class Piment(Epice):
    def __init__(self,nomPi,QtPiment,prixUnitairePi):
        Epice.__init__(self,localite,nomPi,QtPiment,prixUnitairePi)
        self.nom = nomPi
        self.Qt = QtPiment
        self.prixUnitaire = prixUnitairePi
        self.localite = localite

    def AffichePiment(self):
        print(self.localite)

class Gengembre(Epice):
    def __init__(self,nomGen,QtGengembre,prixUnitaireGen):
        Epice.__init__(self,localite,nomGen,QtGengembre,prixUnitaireGen)
        self.nom = nomGenn
        self.Qt = QtGengembre
        self.prixUnitaire = prixUnitaireGen
        self.localite = localite

    def AfficheGengembre(self):
        print(self.localite)




    

class Legume():
    def __init__(self,localite):
            self.local = localite

class Tomate(Legume):
    def __init__(self,nomTo,QtTomate,prixUnitaireTo):
        Legume.__init__(self,localite,nomTo,QtTomate,prixUnitaireTo)
        self.nom = nomTo
        self.Qt = QtTomate
        self.prixUnitaire = prixUnitaireTo
        self.localite = localite

    def AfficheTomate(self):
        print(self.localite)

class Concombre(Legume):
    def __init__(self,nomCon,QtConcombre,prixUnitaireCo):
        Legume.__init__(self,localite,nomCon,QtConcombre,prixUnitaireCo)
        self.nom = nomCon
        self.Qt = QtConcombre
        self.prixUnitaire = prixUnitaireCo
        self.localite = localite

    def AfficheConcombre(self):
        print(self.localite)





class Fruit():
    pass


