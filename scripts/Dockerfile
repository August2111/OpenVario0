FROM crops/poky:debian-11

USER root

COPY files/sources.list /etc/apt/sources.list

RUN apt-get update &&\
	apt-get install -y --no-install-recommends python3-dev imagemagick ffmpeg git curl rsync && apt-get clean

# Add gcc for XCSoar
RUN apt-get install --no-install-recommends -y gcc g++ && apt-get clean

# Add rsync for kernel build system
RUN apt-get install -y rsync
	
RUN git config --global user.email "build@no-domain"
RUN git config --global user.name "Buildrobot"
RUN git config --global color.ui false
