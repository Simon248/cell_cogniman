https://vimeo.com/showcase/9954564/video/767127300


 - [x] mettre les inerties (pas partout mais ca marche)
 - [ ] séparer le serveur visu du serveur simu dans gz
 - [ ] mettre des variable de lancement (if sim, if JSP_gui, if real robot)
 - [ ] chek le use sim time
 - [x] mettre color
 - [x] mettre en place le bridge ros-gz 
 - [x] mettre la variable d'environnement gzpathressources...



  

 - [] creer un script qui parce le csv et creer le modèle (un URDF + les mesh)
    - [] crer une BDD des modèles CAO pour creer les modèles
    - [] parser le csv obtenir positions et réf des pièces   ==> service string(le fichier) --> tableau couple mesh position  
    - [] créer la build plate (mesh)
    - [] creer l'urdf avec les meshpath et position

 - []creer un plugin qui transfére le joint de la build plate au gripper. 
 - [] supprimer la pièce de la Build plate dans le modèle de colision et la faire appariatre dans le gripper pour le modèle de collision et 



- [] revoir le launch et le parametrage du serveur.
         - Le serveur doit être autonome pour tourner dans un docker(est ce que c'es possible)
         - C'esrt surtout URDF et SRDF qui doivent être géré.
         - On peut imaginer que le serveur lors de son init attend ces paramètres
               il doit avoir acces au mesh aussi...
               Compliquer de le conteneuriser. il faut recupérer URDF, SRDF et Mesh.
               Il faudra un service qui gère tout ca dans le robot description.

                  parameters=[{
                'robot_description': robot_description_file,
                'robot_description_semantic':robot_description_semantic_file,
                'discrete_plugin': LaunchConfiguration('discrete_plugin'),
                'continuous_plugin': LaunchConfiguration('continuous_plugin'),
                'monitor_namespace': LaunchConfiguration('monitor_namespace'),
                'monitored_namespace': LaunchConfiguration('monitored_namespace'),
                'publish_environment': LaunchConfiguration('publish_environment'),
                'cache_size': LaunchConfiguration('cache_size'),
                'cache_refresh_rate': LaunchConfiguration('cache_refresh_rate'),
                'task_composer_config': LaunchConfiguration('task_composer_config')
            }]


         ==> pour l'instant faire simple: PAS DE DOCKER
         ==> 