# Space Invaders

## Description

Space Invaders est un jeu d'arcade classique où le joueur contrôle un vaisseau spatial pour défendre la Terre contre des vagues d'ennemis extraterrestres. Le but du jeu est de détruire tous les envahisseurs avant qu'ils n'atteignent le bas de l'écran.

## Fonctionnalités

- **Contrôle du vaisseau** : Utilisez par défaut les touches fléchées pour déplacer le vaisseau à gauche et à droite.
- **Tir** : Appuyez sur la barre d'espace pour tirer des projectiles et détruire les envahisseurs.
- **Keybinds** : Il est possible dans le menu de changer ses touches.
- **Cheats codes** : Il y a 4 touches qui ne peuvent pas être sélectionnées car elles sont utilisées pour les cheats codes:
    - *M : Tir rapide* : Permet de tirer plus rapidement.
    - *N : Tir normal* : Permets de revenir à la vitesse de tir normale.
    - *L : Gain de vie* : Permet de gagner une vie.
    - *P : Gain de Skill Point* : Permet de gagner un Skill Point.
- **Aliens** : Les aliens se déplacent de gauche à droite et de haut en bas. Ils tirent des projectiles qui se déplacent vers le bas de l'écran.
- **Alien bonus** : Un alien bonus apparaît à une fréquence aléatoire. Détruisez-le pour gagner un Skill Point et du score.
- **Protection** : 3 groupes de météors sont présents pour protéger le joueur des tirs ennemis. Si le joueur tir dans un météor son score diminue.
- **Score** : Accumulez des points en détruisant les envahisseurs. Le score est affiché en bas de l'écran.
- **Vies** : Le joueur commence avec 3 vies. Perdez une vie si le vaisseau est touché.
- **Niveaux** : Progressez à travers des niveaux de difficulté croissante. Les envahisseurs se déplacent plus rapidement et tirent plus fréquement à chaque niveau.
- **Upgrade** : Gagnez des Skill Points en finissant en stage ou en tuant un alien bonus pour acheter des améliorations pour votre vaisseau :
    - *Fréquence de tir* : Diminue le cooldown entre chaque tir. (Niveau max : 10)
    - *Nombre de tirs* : Augmente le nombre de tirs simultanés sur l'écran. (Niveau max : 10)
- **Leaderboard** : Un leaderboard est disponible pour voir les meilleurs scores. Lorsque vous finissez une partie, vous pouvez entrer votre pseudo et appuyer sur entrer pour enregistrer votre score dans le leaderboard. Vous pouvez accéder au leaderboard depuis le menu principal.
- **Rules** : Vous pouvez accéder aux règles du jeu depuis le menu principal.

## Déroulement du jeu

En bas se trouve une barre d'indormation avec au milieu le score, le nombre de vies restantes et le nombre de Skill Points. Sur la droite se trouve un bouton pour accéder au menu pricipal et sur la gauche un bouton Restart pour recommencer la partie au stage 1. En haut se trouve la bar de menu avec la section à propos quitter le jeu ou relancer une nouvelle partie.

Normalement il n'est pratiquement pas possible de dépasser le stage 20 (sans les cheats codes) où les aliens tirent à chaque frame. 

## Indormations supplémentaires

Assurez-vous d'avoir installé les modules suivants pour pouvoir jouer au jeu :
    - *Pillow* : `pip install Pillow`
    - *tkinter* : `pip install tk`

Lancez le jeu en exécutant le fichier `main.py`.

Nous avons fait nos commentaires en anglais afin de respecter les bonnnes pratiques. Nous avons aussi utilisé des noms de variables explicites pour faciliter la compréhension du code.

Nous avons codé sur Mac et nous avons testé le jeu sur Mac et Windows. Nous avons constaté que le jeu etait moins fluide sur windows que sur Mac, nous avons alors mis une vidéo (`DEMO.mp4`) du jeu en action sur Mac pour montrer le jeu dans les meilleures conditions.

Cependant toutes les fonctionalités sont présentes sur les deux plateformes.

Les boutons tkinter n'étant pas personnalisables sur Mac nous avons utilisé des Label pour les remplacer et immter le comportement d'un bouton stylisé. (class LabelButton)

Amusez-vous bien en jouant à Space Inviders et essayez de battre votre meilleur score !