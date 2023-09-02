import random
from option import Fourre_Tout
from monstre import Mob


def combat(self,Monde):
    ennemi_potentiel=[]
    for mob in Mob:
      if mob.habitat == Monde.lieux_actuel.habitat:
        ennemi_potentiel.append(mob)
    ennemi = random.choice(ennemi_potentiel)
    Combattant = Monde.joueur
    texte = (f"Un {ennemi.nom} sauvage apparaît")
    Fourre_Tout.Narrateur("",texte)
    while Combattant.pv > 0 and ennemi.pv > 0:
      Fourre_Tout.Transition("",temps = 1)
      texte= "\n".join(f"{index} - {action}" for index, action in Combattant.actions.items())
      Fourre_Tout.Narrateur("",texte)
      choix=input().lower()
      test = Combattant.Faire_action(choix,ennemi)
      if test == "fuir":
        break
      else:
        Fourre_Tout.Transition("",temps = 1)
        if ennemi.pv > 0:
          ennemi.Mob_Attaque(Combattant)
          Fourre_Tout.Transition("",temps = 1)
          if Combattant.pv <= 0:
            Combattant.pv = 0
            ennemi_potentiel.clear()
            Combattant.mort(ennemi,Monde)
            break  
    else:
      ennemi_potentiel.clear()
      ennemi.Mob_Drop(Combattant)