FROM ros:humble

ENV DEBIAN_FRONTEND noninteractive
ENV NVIDIA_DRIVER_CAPABILITIES all
ENV TURTLEBOT3_MODEL waffle_pi

RUN apt-get -y update

RUN apt-get -y install python3-pip
RUN apt-get -y install xserver-xorg-video-nouveau
RUN apt-get -y install libeigen3-dev

RUN apt-get -y install ros-humble-ros-gz
RUN apt-get -y install ros-humble-slam-toolbox
RUN apt-get -y install ros-humble-navigation2 ros-humble-nav2-bringup
RUN apt-get -y install ros-humble-turtlebot3*
RUN apt-get -y install ros-humble-dynamixel-sdk

COPY . /ros2_ws/
WORKDIR /ros2_ws/

RUN pip3 install -r requirements.txt
RUN bash /ros2_ws/build.sh

CMD /ros2_ws/run.sh
