#!/usr/bin/env python3

import os
import subprocess

def install_docker():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

def start_jenkins():
    # Pull the Jenkins image from the Docker registry
    subprocess.run(["docker", "pull", "jenkins/jenkins:lts"])

    # Run the Jenkins image
    subprocess.run(["docker", "run", "-p", "8080:8080", "-p", "50000:50000", "jenkins/jenkins:lts"])

if __name__ == '__main__':
    install_docker()
    start_jenkins()
