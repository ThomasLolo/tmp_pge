# Comment installer votre environnement

> Si vous n'avez pas les droits le fichier **main_detect.py**

`chmod u+x nodes/main_detect.py`

Construire le package 

`catkin build`

**Pour tester l'ensemble :**

Terminale 1 `roscore` 

Terminale 2 `rosbag play -l VotreRosbag.bag`

Terminale 3 `rosrun detect_rgb main_detect.py`

Vous pouvez coder dans le fichier main_detect.py
