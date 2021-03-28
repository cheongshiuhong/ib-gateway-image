FROM python:3.8-slim-buster

# install dependencies
RUN  apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y wget unzip xvfb libxtst6 libxrender1 python3.7-dev build-essential net-tools

# set environment variables
ARG TWSUSERID
ENV TWS_INSTALL_LOG=/root/Jts/tws_install.log \
    ibcIni=/root/ibc/config.ini \
    ibcPath=/opt/ibc \
    javaPath=/opt/i4j_jres \
    twsPath=/root/Jts \
    twsSettingsPath=/root/Jts \
    TWSUSERID=${TWSUSERID} \
    TWSPASSWORD=${TWSPASSWORD}

# make dirs
RUN mkdir -p /tmp && mkdir -p ${ibcPath} && mkdir -p ${twsPath}

# download IB TWS
RUN wget -q -O /tmp/ibgw.sh https://download2.interactivebrokers.com/installers/ibgateway/stable-standalone/ibgateway-stable-standalone-linux-x64.sh
RUN chmod +x /tmp/ibgw.sh

# download IBC
RUN wget -q -O /tmp/IBC.zip https://github.com/IbcAlpha/IBC/releases/download/3.8.2/IBCLinux-3.8.2.zip
RUN unzip /tmp/IBC.zip -d ${ibcPath}
RUN chmod +x ${ibcPath}/*.sh ${ibcPath}/*/*.sh

# install TWS, write output to file so that we can parse the TWS version number later
RUN yes n | /tmp/ibgw.sh > ${TWS_INSTALL_LOG}

# remove downloaded files
RUN rm /tmp/ibgw.sh /tmp/IBC.zip

# copy IBC/Jts configs
COPY ibc/config.ini ${ibcIni}
COPY ibc/jts.ini ${twsPath}/jts.ini

# setup python
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# cd into home directory to setup
WORKDIR /home

# copy app and lib
COPY ./app.py app.py
COPY ./py py 

# copy entrypoint script
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh


# set display environment variable (must be set after TWS installation)
ENV DISPLAY=:0

CMD bash entrypoint.sh

# CMD tail -f /dev/null