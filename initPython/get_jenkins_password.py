import subprocess

def get_jenkins_password():
    # Get the container ID of the Jenkins container
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    lines = output.split("\n")
    # The Jenkins container is the one with the IMAGE "jenkins/jenkins:lts"
    for line in lines:
        if "jenkins/jenkins:lts" in line:
            container_id = line.split()[0]
            break
    else:
        raise ValueError("Jenkins container not found")

    # Get the initial administrator password
    result = subprocess.run(["docker", "exec", container_id, "cat", "/var/jenkins_home/secrets/initialAdminPassword"], stdout=subprocess.PIPE)
    password = result.stdout.decode("utf-8").strip()
    return password

password = get_jenkins_password()
print(f"The initial administrator password is: {password}")
