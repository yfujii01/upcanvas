FROM selenium/standalone-chrome:3.12

ENV HOME=/home/seluser
WORKDIR ${HOME}
COPY . ${HOME}

# install python3
RUN sudo apt-get update
RUN sudo apt-get install -y apt-file
RUN sudo apt-file update
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository -y ppa:jonathonf/python-3.6
RUN sudo apt-get update
RUN sudo apt-get install -y python3.6
RUN sudo apt-get install -y python3.6-dev
RUN sudo apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py

RUN sudo python3.6 get-pip.py
RUN sudo pip install pipenv
RUN pipenv install --skip-lock

RUN sudo apt-get install -y zip
RUN wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d ~/bin/
