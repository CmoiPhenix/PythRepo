import random

from option import Fourre_Tout

class Entité():
  """definie les monstres est ce qu'il renferme"""

  def __init__(self,nom,pv_max,atk,exp,gold,habitat):
    self.nom = nom
    self.pv_max = pv_max
    self.pv = self.pv_max
    self.atk = atk
    self.exp = exp
    self.gold = gold
    self.habitat = habitat

  def Mort(self):
    if self.pv <=0:
      texte =(f"{self.nom} est mort!!!!!")
      Fourre_Tout.Narrateur("",texte)
      
  def Mob_Attaque(self,joueur):
    attaque = random.randint(1, self.atk)
    texte = (f"{self.nom} inflige {attaque} dommages")
    Fourre_Tout.Narrateur("",texte)
    joueur.pv -= attaque
    if joueur.pv < 0:
      joueur.pv = 0
    texte = (f"Votre PV: {joueur.pv}, PV du {self.nom}: {self.pv}")
    Fourre_Tout.Narrateur("",texte)
    
  
  def Mob_Drop(self,joueur):
    texte = (f"{self.nom} est mort!!!!!")
    Fourre_Tout.Narrateur("",texte)
    joueur.gold += self.gold
    joueur.exp += self.exp

"""création du bibliotheque de monstre
Entité(nom du monstre, point de vie,attaque,exp,or,habitat)"""

Mob=[
Entité("Poring", 50, 1,1,6,"foret"),
Entité("condor", 50, 4,2,8,"desert"),
Entité("pupa"  , 50, 3,1,7,"foret"),
]

