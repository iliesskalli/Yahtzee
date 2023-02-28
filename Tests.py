#Import 
#Yahtzee/Main.py /
#@iliesskalli
#iliesskalli V.3
#Latest commit bc99016 6 minutes ago
#History
#1 contributor
#184 lines (117 sloc)  5.34 KB


from Yahtzee import Yahtzee
import unittest


#Classe de test 
#On teste indépendement chaque cas possible  
#
 
#-----------------------------------------------------------------------------

class TestYahtzee(unittest.TestCase):
    

#-----------------------------------------------------------------------------

    
#Le cas UN : Il faut avoir autant de 1 que possible
#La somme vaut le nombre de 1 x 1




    def test_ones(self):
        Array_1 = [1, 1, 1, 6, 5]
        assert Yahtzee.ones(Array_1) == 3
        
        
        
#-----------------------------------------------------------------------------

#Les 5 prochains cas suivent tous la règle du cas UN

    def test_twos(self):
        Array_2 = [5, 5, 2, 2, 4]
        assert Yahtzee.twos(Array_2) == 4
        
        
#-----------------------------------------------------------------------------
       
    
    def test_threes(self):
        Array_3 = [1, 4, 3, 5, 3]
        assert Yahtzee.threes(Array_3) == 6
        
        
#-----------------------------------------------------------------------------


    def test_fours(self):
        Array_4 = [4, 4, 4, 6, 4]
        assert Yahtzee.fours(Array_4) == 16
        
        
#-----------------------------------------------------------------------------


    def test_sixes(self):
        Array_6 = [6, 2, 6, 6, 6]
        assert Yahtzee.sixes(Array_6) == 24
        
        
#-----------------------------------------------------------------------------


    def test_fives(self):
        Array_5 = [5, 6, 5, 5, 1]
        assert Yahtzee.fives(Array_5) == 15
    
        
#-----------------------------------------------------------------------------


    def test_three_of_a_kind(self):
        Array_three_Of_A_Kind = [3, 3, 3, 4, 1]
        assert Yahtzee.three_of_a_kind(Array_three_Of_A_Kind) == sum(Array_three_Of_A_Kind)
        
        
#-----------------------------------------------------------------------------

   
    def test_chance(self):
        Array_chance = [6, 5, 6, 6, 4]
        sum = 0
        for i in Array_chance:
            sum += i
        assert Yahtzee.chance(Array_chance) == 27
        
        
#-----------------------------------------------------------------------------



#Tous les nombres identiques : 50 points : Win

    def test_yahtzee(self):
        Array_yahtzee = [6, 6, 6, 6, 6]
        assert Yahtzee.yahtzee(Array_yahtzee) == 50
        

#-----------------------------------------------------------------------------


    def test_fullhouse(self):
        Array_fullhouse = [3, 3, 3, 6, 6]
        assert Yahtzee.fullhouse(Array_fullhouse) == 25


#-----------------------------------------------------------------------------


    def test_largestraight(self):
        Array_largestraight = [1, 2, 3, 4, 5]
        assert Yahtzee.largestraight(Array_largestraight) == 40
   
#-----------------------------------------------------------------------------



    def test_smallstraight(self):
        Array_smallstraight = [3, 4, 5, 6, 1]
        assert Yahtzee.smallstraight(Array_smallstraight) == 30


#-----------------------------------------------------------------------------



    def test_four_of_a_kind(self):
        Array_four_Of_A_Kind = [5, 5, 5, 5, 6]
        assert Yahtzee.four_of_a_kind(Array_four_Of_A_Kind) == sum(Array_four_Of_A_Kind)
        
        
#-----------------------------------------------------------------------------


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