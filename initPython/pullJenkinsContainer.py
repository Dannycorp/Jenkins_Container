import subprocess

def start_jenkins():
    # Pull the Jenkins image from the Docker registry
    subprocess.run(["docker", "pull", "jenkins/jenkins:lts"])

    # Run the Jenkins image
    subprocess.run(["docker", "run", "-p", "8083:8080", "-p", "50000:50000", "jenkins/jenkins:lts"])

start_jenkins()