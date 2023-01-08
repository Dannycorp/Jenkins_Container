#!/usr/bin/env python3

import os

def install_docker():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

if __name__ == '__main__':
    install_docker()
