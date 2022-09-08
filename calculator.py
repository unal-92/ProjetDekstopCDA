from kivy.uix.boxlayout import BoxLayout #librairie
from kivy.properties import StringProperty #librairie



class Calculator(BoxLayout):
    previous_value = StringProperty("") #variable / previous_value = propriété de la class
    
    def get_input(self, button): #self correspond a la class calculator / methode de class
        self.previous_value = f"{self.previous_value}{button.text}" #j'attribue une nouvelle valeur a previous_value qui est egale a / le boutton peut possder plusieurs propriétés 
        
        
    def resultat(self):
        self.previous_value = str(round(eval(self.previous_value),2)) #eval=fonction native qui permet de faire un calcule a partir d'une chaine de caractere
        
        
    def clear(self): #method
        self.ids.calc_input.text="0" #fonction qui permet de clear le resultat
        self.previous_value = "" #je laisse chaine de caractère vide pour que ça reste a 0
        
 
 