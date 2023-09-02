
import random

from monstre import Entité
from option import Fourre_Tout

class Joueur(Entité):

  actions = {
        'a': 'attaquer',
        'f': 'fuir'
    }
  
  """definie le joueur est ce qu'il renferme"""
  def __init__(self):
    #Entité(nom , point de vie,attaque,exp,or,habitat)
    Entité.__init__(self,"Héros",150,10,0,10,None)
    self.pv = 1 #self.pv_max
    self.level = self.exp // 10

  def Attaque(self,monstre):
    attaque = random.randint(1, self.atk)
    texte =(f"{self.nom} inflige {attaque} dommages")
    Fourre_Tout.Narrateur("",texte)
    monstre.pv -= attaque
    if monstre.pv < 0:
      monstre.pv = 0
    texte =(f"Votre PV: {self.pv}, PV du {monstre.nom}: {monstre.pv}")
    Fourre_Tout.Narrateur("",texte)
  
  def Fuir(self,Monde):
    print("Tu Fuis lachement le combat")

  def Faire_action(self, action,monstre):
    """sert a lancer la bonne action"""
    if action not in self.actions:
        texte =('Action impossible')
        Fourre_Tout.Narrateur("",texte)
    if action == 'a':
        self.Attaque(monstre)
    elif action == 'f':
        self.Fuir(self)
        return("fuir")

  def mort(self,ennemi,Monde):
    """definie les conditions de mort"""
    texte =("le {}, Vous a vaincu!!!\n\
    Vous vous voyez flotter au dessus de votre corps qui est transporter".format(ennemi.nom))
    Fourre_Tout.Narrateur("",texte)
    Fourre_Tout.Transition("",temps = 1)
    self.Resurrection(Monde)
    
  def Resurrection(self,Monde):
    texte =("Vous voyez, une personne vous faire les poches et trouver votre bourse")
    Fourre_Tout.Narrateur("",texte)
    Fourre_Tout.Transition("",temps = 1)
    if self.gold>=100:
      self.gold -=100
      texte =("d'un sourire ravit, il empoche des pieces et fait une incantation")
      Fourre_Tout.Narrateur("",texte)
      self.pv = self.pv_max
      texte =("Votre esprit est attiré par votre corps, vous vous reveillez dans une rue en pleine forme")
      Fourre_Tout.Narrateur("",texte)
      Fourre_Tout.Transition("",temps = 1)
      Monde.lieux_actuel = Monde.lieux[1]
      return
    else:
      texte =("Decut,vous le voyez prendre votre corps et le jeter au cochon, vous êtes mort{}".format(Monde.joueur.nom))
      Fourre_Tout.Narrateur("",texte)
      Monde.Charger_ancien_monde()

  
  def Nommer_Heros(self):
    """permet de renommer le heros"""
    nom = input().capitalize()
    return nom