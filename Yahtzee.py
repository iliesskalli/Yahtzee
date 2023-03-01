#Yahtzee/Main.py /
#@iliesskalli
#iliesskalli V.3
#Latest commit bc99016 6 minutes ago
#History
#1 contributor
#184 lines (117 sloc)  5.34 KB




#On définit la classe
#Définir les retours de scores
#Les combinaisons


class Yahtzee:
    
    
#-----------------------------1---------------------------------------------

    def ones(Liste_des_des):
        score = 0 
        for i in (Liste_des_des):
            if i == 1:
                score += 1
        print("Votre Score est : {}".format(score))
        return score



#-----------------------------2---------------------------------------------

    def twos(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            if i == 2:
                score += 2
        print("Votre Score est : {}".format(score))
        return score
    
    
#-----------------------------3---------------------------------------------


    def threes(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            if i == 3:
                score += 3
        print("Votre Score est : {}".format(score))
        return score



#-----------------------------4---------------------------------------------

    def fours(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            if i == 4:
                score += 4
        print("Votre Score est : {}".format(score))
        return score
    
    
#-----------------------------5---------------------------------------------


    def fives(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            if i == 5:
                score += 5
        print("Votre Score est : {}".format(score))
        return score
    
 
 
#-----------------------------6---------------------------------------------


    def sixes(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            if i == 6:
                score += 6
        return score
    

#-----------------------------Chance------------------------------------------


    def chance(Liste_des_des):
        score = 0
        for i in (Liste_des_des):
            score += i
        print("Votre Score est : {}".format(score))
        return score

#-----------------------------Yahtzee-----------------------------------------



    def yahtzee(Liste_des_des):
        des_prm = Liste_des_des[0]
        for des in Liste_des_des:
            if des_prm == des:
                score = 50
            else:
                score = 0
        print("Votre Score est : {}".format(score))
        return score
    
#-----------------------------3 identiques------------------------------------



    def three_of_a_kind(Liste_des_des):
        compte = 0
        des_prm = Liste_des_des[0]
        score = 0
        for des in Liste_des_des:
            if des_prm == des:
                compte += 1
            if compte == 3:
                score = sum(Liste_des_des)
            else:
                continue
        print("Votre Score est : {}".format(score))
        return score




#-----------------------------4 identiques------------------------------------

 

    def four_of_a_kind(Liste_des_des):
        compte = 0
        des_prm = Liste_des_des[0]
        score = 0
        for des in Liste_des_des:
            if des_prm == des:
                compte += 1
            if compte == 4:
                score = sum(Liste_des_des)
            else:
                continue
        print("Votre Score est : {}".format(score))
        return score
    
    


#-----------------------------Sequence de 4------------------------------------

    def smallstraight(Liste_des_des):
        score = 0
        compte = 0
        Liste_des_des.sort()
        for des in range(1, 4):
            if Liste_des_des[des]-1 == Liste_des_des[des-1]:
                compte += 1
            if compte == 3:
                score = 30
        print("Votre Score est : {}".format(score))
        return score
    
    
    
#-----------------------------Sequence de 5------------------------------------


    def largestraight(Liste_des_des):
        score = 0
        compte = 0
        Liste_des_des.sort()
        for des in range(1, 5):
            if Liste_des_des[des]-1 == Liste_des_des[des-1]:
                compte += 1
            if compte == 4:
                score = 40
        print("Votre Score est : {}".format(score))
        return score
    
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

    def fullhouse(Liste_des_des):
        compte = 0
        score = 0
        Liste_des_des.sort()
        des_prm = Liste_des_des[0]
        for des in Liste_des_des:
            if des_prm == des:
                compte += 1
                
            if compte == 3: 
                des_prm = Liste_des_des[3]
                for des in Liste_des_des:

                    if des_prm == des:
                        compte += 1
                        
                    if compte == 5:
                        score = 25
                    else:
                        continue
             
             
        print("Votre Score est : {}".format(score))
        return score
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