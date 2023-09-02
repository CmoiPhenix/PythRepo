
def creer_nouveau_monde():
  Monde = Jeux()
  Monde.joueur.nom = input("Voix: Bonjour héros,comment tu t'appelles?: ")
  Monde.nom = input(
      "Voix: Et comment s'appelles le monde dnas lequel tu viens d'arriver?: ")
  print("Bienvenue {}, dans {}\n".format(Monde.joueur.nom, Monde.nom))
  return Monde


def charger_ancien_monde():
  print("non disponible pour le moment")


def menu():
  print("Choississez ce que vous souhaitez faire:")
  while True:
    try:
      choix = int(
          input("\t1 - Commencer une aventure:\n\
      2 - Reprendre une sauvegarde:\n\
      3 - nous quitter:\n"))

      if choix == 1:
        Monde = creer_nouveau_monde()
        return Monde
      elif choix == 2:
        charger_ancien_monde()
      elif choix == 3:
        print("Au revoir !")
        quit()
      else:
        print("Veuillez entrer un nombre valide.")
    except ValueError:
      print("Veuillez entrer un nombre valide.")


def action(Monde):
  #Monde.lieux.menu_lieu_actuel(Monde)
  print(f"Vous êtes actuellement dans {Monde.Lieux_actuel.nom}")


Monde = menu()
action(Monde)





class Lieux:
  """definie le monde est ce qu'il renferme"""
  def __init__(self,Jeux):
    self.Jeux = Jeux
    
  def menu_lieu_actuel(self,Monde):
      print(f"Vous êtes actuellement dans {Monde.Lieux_actuel.nom}")
      if Monde.Lieux_actuel.nom == "la foret":
          input("Que voulez-vous faire?:\n\
          1 - Combattre \n\
          2 - Aller au village\n")
        
      elif Monde.Lieux_actuel.nom =="le village":
          input("Que voulez-vous faire?:\n\
          1 - Voir le Prêtre \n\
          2 - Aller dans la forêt\n")
      else:
          print("Lieu non reconnu")


  """
Quand tu définis une nouvelle classe, essaye de te créer les fonctions qui te permettent de lire/modifier les différents attributs de ta classe, exemple :

class Joueur:
  def __init__(self,pseudo,Pv=250,Potion=2,):
    print("Création d'un Joueur....")
    self.pseudo = pseudo
    self.Pv = Pv
    self.Potion = Potion
    self.action= [attaque,stun,potion]

#Liste les actions que tu peux faire sur un pseudo :
  def Pseudo(self)
    Return self.pseudo
    # print(Joueur_1.Pseudo)

  def Modifier_Pseudo(self, Nouveau_Pseudo)
    self.pseudo = Nouveau_Pseudo
    # Appel de ta fonction dans ton main :
      # Joueur_1.Modifier_Pseudo("Bernard")
      # Joueur_2.Modifier_Pseudo("Claude")

#Liste les actions que tu peux faire sur les PV :
  def PV(self)
    #Te donne le nb de pv de ton joueur
    return self.Pv
    
  def Modifier_PV(Self, Nouveau_PV)
    self.Pv = Nouveau_PV
    # Appel de ta fonction dans ton main :
      # Joueur_1.Modifier_PV(50)
      #
      # Joueur_2.Modifier_PV(Joueur_1.PV-Joueur_1.Modifier_PV(50))

  def Retirer_PV(Self, PV_A_Retirer)
    self.Pv = self.Pv - PV_A_Retirer
    #Joueur_1.Retirer_PV(50)
 
"""

def combattre(self,Monde):
    ennemi = random.choice(self.monstres)
    Combattant = Monde.joueur
    print(f"Un {ennemi.nom} sauvage apparaît")
    while Combattant.pv > 0 and ennemi.pv > 0:
      time.sleep(2)
      clear()
      Combattant.Attaque(ennemi)
      ennemi.Mob_Attaque(Combattant)