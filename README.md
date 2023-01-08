# Jenkins_Container
Install a Jenkins Container/Docker 

You're going to need root privileges here: * don't forget about this

sudo groupadd docker - creates the docker group
sudo usermod -aG docker $USER - Adds your user to the docker group. (log out and in again)
newgrp docker - run this to activate the changes to groups if you want 
docker run hello-world - check if you can run docker commands without sudo.




Method:


install_docker.py   - First install Docker 

pullJenkinsContainer.py - this will output the temp pass if you're watching the logs

get_jenkins_password.py - You can run this to get the Jenkins initial password.


![jenkins_logo](https://user-images.githubusercontent.com/8779526/211195829-cd408dc7-7436-4eb6-b298-b40166564144.png)
