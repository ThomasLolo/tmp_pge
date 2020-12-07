# Comment installer votre environnement

> Si vous ne travaillez pas dans catkin_ws à vous d'adapter votre chemin.

Tapez :

`cd ~/catkin_ws/src`

`catkin create pkg detect_rgb --catkin-deps rospy cv_bridge`

`cd detect_rgb`

`mkdir nodes`

Puis dans le fichier **nodes** vous ajoutez le fichier **main_detect.py**

> Si vous n'avez pas les droits :

`chmod u+x nodes/main_detect.py`

Construire le package

`catkin build`


>Si besoin : 
>`cd ~/catkin_ws/`
>`source devel/setup.bash`

**Pour tester l'ensemble :**

Terminale 1 `roscore`

Terminale 2 `rosbag play -l VotreRosbag.bag`

Terminale 3 `rosrun detect_rgb main_detect.py`

Vous pouvez coder dans le fichier main_detect.py
