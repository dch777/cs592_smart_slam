FROM ros:humble

ENV DEBIAN_FRONTEND noninteractive
ENV NVIDIA_DRIVER_CAPABILITIES all
ENV TURTLEBOT3_MODEL waffle_pi

RUN apt-get -y update

RUN apt-get -y install python3-pip
RUN apt-get -y install xserver-xorg-video-nouveau

RUN apt-get -y install ros-humble-ros-gz
RUN apt-get -y install ros-humble-slam-toolbox
RUN apt-get -y install ros-humble-navigation2 ros-humble-nav2-bringup
RUN apt-get -y install ros-humble-turtlebot3*
RUN apt-get -y install ros-humble-dynamixel-sdk

RUN apt-get -y install libeigen3-dev
RUN apt-get -y install libepoxy-dev
RUN apt-get -y install libc++-dev
RUN apt-get -y install libegl1-mesa-dev
RUN apt-get -y install ninja-build
RUN apt-get -y install wayland-protocols
RUN apt-get -y install libxkbcommon-dev
RUN apt-get -y install libwayland-dev
RUN apt-get -y install libboost-python-dev
RUN apt-get -y install libunwind-dev
RUN apt-get -y install ros-humble-libg2o
RUN apt-get -y install ros-humble-pcl-ros
RUN apt-get -y install pcl-tools

RUN apt-get -y install vim tmux

ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib/local"
RUN ldconfig

RUN mkdir /ros2_ws/
WORKDIR /ros2_ws/

COPY build_deps.sh build_deps.sh
RUN bash /ros2_ws/build_deps.sh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt -v

COPY . /ros2_ws/src
RUN bash /ros2_ws/src/build.sh

CMD /ros2_ws/src/run.sh
