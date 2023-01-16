FROM jenkins/jenkins:lts

EXPOSE 8083
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

USER root
RUN apt-get update && apt-get install -y sudo
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins

CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
