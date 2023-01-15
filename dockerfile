FROM jenkins/jenkins:lts-alpine
EXPOSE 8083

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# later for plugins
# COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

USER root
RUN apk update && apk add --no-cache sudo
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins

CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
