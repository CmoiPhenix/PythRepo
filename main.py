from pickle import NONE
from option import Fourre_Tout
from monde import Monde

if __name__ == '__main__':
  monde = Monde("midgard")
  
  monde.Menu()
  Fourre_Tout.Transition("",temps = 2)
  while True:
    texte= ("Tu te trouves actuellement dans {}".format(monde.lieux_actuel.nom))
    Fourre_Tout.Narrateur("",texte)
    texte= "\n".join(f"{index} - {action}" for index, action in monde.lieux_actuel.actions.items())
    Fourre_Tout.Narrateur("",texte)
    choix=input()
    monde.lieux_actuel.Faire_action(choix,monde)
    Fourre_Tout.Transition("",temps = 2)   

#TestGit