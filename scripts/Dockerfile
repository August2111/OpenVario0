FROM crops/poky:ubuntu-18.04

USER root

RUN apt-get update &&\
	apt-get install -y  python-dev imagemagick ffmpeg repo git

# Add gcc8 for XCSoar
RUN apt-get install -y gcc-8 g++-8
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8

# Add rsync for kernel build system
RUN apt-get install -y rsync
	
RUN git config --global user.email "build@no-domain"
RUN git config --global user.name "Buildrobot"
RUN git config --global color.ui false
