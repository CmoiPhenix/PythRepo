#https://docs.python.org/fr/3/tutorial/classes.html

from lieux import Foret, Lieux, Village
from monstre import Entité
from players import Joueur
from option import Fourre_Tout
import pickle


class Monde:
  """definie le monde et ce qu'il renferme"""

  def __init__(self,nom):
    self.nom = nom
    self.entité = Entité("test",1,1,1,1,"habitat")
    self.lieux = [Foret() ,Village()]
    self.joueur = Joueur()
    self.lieux_actuel = self.lieux[0]
    
  def Nommer_monde(self):
    """permet de changer le nom du monde"""
    nom = input()
    return nom

  def Demarrer_Aventure(self,joueur):
    """introduction de l'aventure"""
    texte = ("Voix: Bonjour héros,comment tu t'appelles?:")
    Fourre_Tout.Narrateur("",texte)
    self.joueur.nom = joueur.Nommer_Heros(self)
    texte =("Voix: Et comment s'appelles le monde dans lequel tu viens d'arriver?: ")
    Fourre_Tout.Narrateur("",texte)
    self.nom = self.Nommer_monde()
    texte = ("Bienvenue {}, dans {}\n".format(self.joueur.nom, self.nom))
    Fourre_Tout.Narrateur("",texte)

  def Charger_ancien_monde(self, nom_fichier):
    try:
      with open(nom_fichier, 'rb') as fichier:
        partie = pickle.load(fichier)
        return partie
    except AttributeError:
      return None
    except Exception as e:
      return None
      
  def sauvegarder(self, nom_fichier):
    with open(nom_fichier, 'wb') as fichier:
        pickle.dump(self, fichier)
      
  def quitter(self):
    texte = ("Au revoir !")
    Fourre_Tout.Narrateur("",texte)
    quit()
    
  def Menu(self):
    """menu d'entrée de jeu permet au joueur de choisir ce qu'il compte faire"""
    texte = ("Choississez ce que vous souhaitez faire:")
    Fourre_Tout.Narrateur("",texte)
    while True:
      texte =("\n\
      1 - Commencer une aventure:\n\
      2 - Reprendre une sauvegarde:\n\
      3 - nous quitter:\n")
      Fourre_Tout.Narrateur("",texte)
      choix =input()
      if choix == "1":
        self.Demarrer_Aventure(Joueur)
        return
      elif choix == "2":
        texte = ("Entree le nom de votre sauvegarde(nom de votre personnage) a charger:")
        Fourre_Tout.Narrateur("",texte)
        Save=input()
        sauvegarde_chargee = self.Charger_ancien_monde("{}.dat".format(Save))
        if sauvegarde_chargee is not None:
          self.__dict__.update(sauvegarde_chargee.__dict__)
          texte = ("Rebienvenue {}".format(self.joueur.nom))
          Fourre_Tout.Narrateur("",texte)
        else:
          texte = ("Je suis désolé mais ce n'est pas cette sauvegarde que vous recherchez")
        Fourre_Tout.Narrateur("",texte)
        return
      elif choix == "3":
        self.quitter()
      else:
        texte = ("Veuillez entrer un nombre valide.")
        Fourre_Tout.Narrateur("",texte)

        


  