https://vimeo.com/showcase/9954564/video/767127300


 - [x] mettre les inerties (pas partout mais ca marche)
 - [ ] séparer le serveur visu du serveur simu dans gz
 - [ ] mettre des variable de lancement (if sim, if JSP_gui, if real robot)
 - [ ] chek le use sim time
 - [x] mettre color
 - [x] mettre en place le bridge ros-gz 
 - [x] mettre la variable d'environnement gzpathressources...


 * Status:  
le modele avec inertie de gp7 genere plusieurs base link  --> pas solutioné, les inertie sont dans le model.
  

 - [] creer un script qui parce le csv et creer le modèle (un URDF + les mesh)
    - [] crer une BDD des modèles CAO pour creer les modèles
    - [] parser le csv obtenir positions et réf des pièces   ==> service string(le fichier) --> tableau couple mesh position  
    - [] créer la build plate (mesh)
    - [] creer l'urdf avec les meshpath et position

 - []creer un plugin qui transfére le joint de la build plate au gripper. 
 - [] supprimer la pièce de la Build plate dans le modèle de colision et la faire appariatre dans le gripper pour le modèle de collision et 

 5 11 28 31 34 37 40 43  
 5 joint ground plane  
 11 base link  
 28 link1  
 31 link2  
 34 link3  
 37 link4  
 40 link5  
 43 link6  

