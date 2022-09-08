 (utiliser gitbash)

python -m pip install --upgrade pip setuptools virtualenv = PERMET DE METTRE A JOUR LE PACKAGE MANAGER ET PERMET D'INSTALLER LE MODULE VIRTUALE VENV QUI PERMET DE CREER L'ENVIRONNEMENT 
plus besoin de le faire a chaque fois


python -m virtualenv kivy_venv = PERMET DE CREER LE VIRTUAL ENV


source kivy_venv/Scripts/activate = PERMET D'ACTIVER L'ENVIRONNEMENT VIRTUEL a activer a chaque fermeture de VsCode (pas toujours)


python -m pip install "kivy[base]" kivy_examples = PERMET D'INSTALLER L'ENVIRONNEMENT KIVY UNIQUEMENT DANS LE PROJET cross platforme /windows/linux/max


python main.py = permet de lancer l'appli