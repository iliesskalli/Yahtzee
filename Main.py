#Yahtzee/Main.py /
#@iliesskalli
#iliesskalli V.3
#Latest commit bc99016 6 minutes ago
#History
#1 contributor
#184 lines (117 sloc)  5.34 KB

from Yahtzee import Yahtzee
import random


#Développement Data : Lancement du Jeu : Import + Random 
#Definition de la problématique
#Gestion des dès:
#Combinaisons : 13 
#Calculs : combinaisons
    


def game():
    VosDes = 5
    VosChoix = []
    Essai = 0
    
#--------------------------Penser au calcul différé --------------------------
    
    VosCombinaisons = [
        '[1]Ones',
        '[2]Twos', 
        '[3]Threes', 
        '[4]Fours', 
        '[5]Fives',
        '[6]Sixes',
        '[7]Three of a kind',
        '[8]Four of a kind',
        '[9]Full House',
        '[10]Small Straight',
        '[11]Large Straight',
        '[12]Chance',
        '[13]Yahtzee']
    
    
    #Une fois le calcul lancé, on définit le nombre d'essai pouvant être incrementé (3)

    #On définit donc 3 tentatives possibles : 
        
    while Essai <= 2:
        Essai += 1
        print("Vous êtes à votre essai numéro {} sur 3 \n".format(Essai))

#-----------------------------------------------------------------------------
        
        
    #Notification de l'utilisateur 
        print("Le programme lance les dès : ")
        des_encours = []


#-----------------------------------------------------------------------------

     #Random des
        for i in range(0, VosDes):
            Des_rndm = random.randint(1, 6)
            des_encours.append(Des_rndm)
            
#-----------------------------------------------------------------------------
           
    #Message lancement
        print("Vous lancez parmi : " + str(des_encours) + "\n")

    
#-----------------------------------------------------------------------------

        
        #Parcours 
        for i in range(0, len(des_encours)):
        #Choix
            print("Choisissez votre dès".format(i+1))
            
#-----------------------------------------------------------------------------

            
            choixdudes = input()
            
            if choixdudes != '':
                VosDes -= 1
                
                VosChoix += choixdudes
            if choixdudes == '':
                
                continue

        if len(VosChoix) != 5 and Essai == 3:
            for dice in des_encours:
                VosChoix.append(dice)
                
#-----------------------------------------------------------------------------          
                
                
                
        VosChoix = [int(dice) for dice in VosChoix]
        print("Vos Choix : {}".format(VosChoix))

    print('Choix de la combinaison, de ce choix dépend la manière dont sont calculés vos points :')
    for combination in VosCombinaisons:
        print(combination)
    combination_choice = int(input())
    
    
#-----------------------------------------------------------------------------


#Dans le cas ou l'utilisateur rentre une valeur supérieur à 13
    if combination_choice not in range(1, 14):
        while True:
            print("Erreur ! Le nombre de combinaison ne dépasse pas 13")
            combination_choice = int(input())
            if combination_choice in range(1, 14):
                break
            
            
#-------------------GESTION DES COMBINAISONS----------------------------------
            
    if combination_choice == 1:
        Yahtzee.ones(VosChoix)
        
#-----------------------------------------------------------------------------
       
    elif combination_choice == 2:
        Yahtzee.twos(VosChoix)
#-----------------------------------------------------------------------------
      
    elif combination_choice == 3:
        Yahtzee.threes(VosChoix)
#-----------------------------------------------------------------------------

    elif combination_choice == 4:
        Yahtzee.fours(VosChoix)
#-----------------------------------------------------------------------------

    elif combination_choice == 5:
        Yahtzee.fives(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 6:
        Yahtzee.sixes(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 7:
        Yahtzee.Three_of_a_kind(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 8:
        Yahtzee.four_of_a_kind(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 9:
        Yahtzee.fullhouse(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 10:
        Yahtzee.smallstraight(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 11:
        Yahtzee.largestraight(VosChoix)
        
#-----------------------------------------------------------------------------

    elif combination_choice == 12:
        Yahtzee.chance(VosChoix) 
        
#-----------------------------------------------------------------------------

    elif combination_choice == 13:
        
#-----------------------------------------------------------------------------

        Yahtzee.yahtzee(VosChoix)
    print('Fin du jeu')
#-----------------------------------------------------------------------------


if __name__ == '__main__':
    game()
#Footer
#© 2023 GitHub, Inc.
#Footer navigation
#Terms
#Privacy
#Security
#Status
#Docs
#Contact GitHub
#Pricing
#API
#Training
#Blog
#About
#Yahtzee/Yahtzee.cpython-37.pyc at master · iliesskalli/Yahtzee