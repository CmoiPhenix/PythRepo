import random

from monstre import Entité
from combat import combat
from option import Fourre_Tout

class Lieux():
  """definie les lieux est ce qu'il renferme"""
  def __init__(self):
    self.nom = "lieux"

  
class Foret(Lieux):
  """definie ce que contient la foret, en cas d''ajout d'action penser a ajuster la bibliotheque action et   la def faire_action"""
  
  actions = {
        '1': 'combattre',
        '2': 'Aller au village'
    }
  def __init__(self):
    self.nom = "la foret"
    self.habitat = "foret"

  def combattre(self,Monde):
    combat(self,Monde)
    
  def aller_au_village(self,Monde):
    texte=("tu te rend au village")
    Fourre_Tout.Narrateur("",texte)
    Monde.lieux_actuel = Monde.lieux[1]
    return

  def Faire_action(self, action,Monde):
    """sert a lancer la bonne action"""
    if action not in self.actions:
        texte = ('Action impossible')
        Fourre_Tout.Narrateur("",texte)
    if action == '1':
        self.combattre(Monde)
    elif action == '2':
        self.aller_au_village(Monde)




class Village(Lieux):
  """definie ce que contient le village, en cas d''ajout d'action penser a ajuster la bibliotheque d'action et la def faire_action()"""
  
  actions = {
      '1': 'Aller voir le pretre',
      '2': 'Aller dans la foret',
      '3': 'Rentrer dans la bibliotheque'
  }
  
  def __init__(self):
    self.nom = "le village"

  def Pretre(self,Monde):
    """action du pretre qui soigne et ressucite"""
    texte =(f"Prêtre: Bonjour, il te manque {Monde.joueur.pv_max - Monde.joueur.pv} Point de vie et tu as {Monde.joueur.gold} Po ")
    Fourre_Tout.Narrateur("",texte)
    Soin= input(f"Prêtre: {Monde.joueur.nom}, souhaite tu te soigner contre 50 Po?(y)/(N)").lower()
    
    if Soin == "y" and Monde.joueur.gold >= 50:
      Monde.joueur.gold -= 50
      Monde.joueur.pv += 100
      if Monde.joueur.pv > Monde.joueur.pv_max:
        Monde.joueur.pv = Monde.joueur.pv_max
      texte=(f"Tu te soignes aupres du prêtre,tu as {Monde.joueur.pv} Point de Vie")
      Fourre_Tout.Narrateur("",texte)
    else:
      texte=("Prêtre: Reviens une prochaine fois")
      Fourre_Tout.Narrateur("",texte)
  
  def aller_en_Foret(self,Monde):
      texte=("tu te rends dans la forêt")
      Fourre_Tout.Narrateur("",texte)
      Monde.lieux_actuel = Monde.lieux[0]

  def Bibliotheque(self,Monde):
    texte=("Bibliothecaire: Bonjour, Souhaitez vous consigné vos aventure dans mes registres?\n\
      Sauvegarder y/n:\n")
    Fourre_Tout.Narrateur("",texte)
    test = input().lower()
    
    if test == "y":
      texte=("test")
      Fourre_Tout.Narrateur("",texte)
      Monde.sauvegarder("{}.dat".format(Monde.joueur.nom))
      texte=("Bibliothecaire:Ton aventure a bien étais consigné")
      Fourre_Tout.Narrateur("",texte)
    else:
      texte=("Bibliothecaire: Au revoir!")
      Fourre_Tout.Narrateur("",texte)

  def Faire_action(self, action,Monde):
    """sert a lancer la bonne action"""
    if action not in self.actions:
      texte=('Action impossible')
      Fourre_Tout.Narrateur("",texte)
      return False
    if action == '1':
      self.Pretre(Monde)
    elif action == '2':
      self.aller_en_Foret(Monde)
    elif action == "3":
      self.Bibliotheque(Monde)
    return True