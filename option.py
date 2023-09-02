
import time
from clear import clear
#pip install clear


class Fourre_Tout:
  """option ou je ne savait pas ou mettre"""
  def __init__(self):
    pass

  def Transition(self,temps):
    """fonction pour faire une pause et nettoyer l ecran"""
    time.sleep(temps)
    clear()

  def Narrateur(self,texte):
    """permet d'afficher le texte, utile si implantation visuel"""
    print(texte)