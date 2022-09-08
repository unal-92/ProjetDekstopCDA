from kivy.app import App #j'importe le module de l'app kivy qui me permet de lancer l'app

from calculator import Calculator 

class MainApp(App): #mainApp herite de la classe app
    pass

if __name__ == '__main__': # le name s'appel main c'est le fichier d'entré/ permet de sécuriser l'appli lorsqu'on a plusieur appli
    MainApp().run() #MainApp est instancier 
    
