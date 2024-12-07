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

RUN apt-get -y install vim tmux

RUN git clone --recursive https://github.com/stevenlovegrove/Pangolin
WORKDIR /Pangolin/
RUN cmake -B build
RUN cmake --build build -j8
RUN cmake --install build

ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib/local"
RUN ldconfig

WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /ros2_ws/
COPY . /ros2_ws/src
WORKDIR /ros2_ws/
RUN bash /ros2_ws/src/build.sh

CMD /ros2_ws/src/run.sh
