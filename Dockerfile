# This is an auto generated Dockerfile for ros:robot
# generated from docker_images/create_ros_image.Dockerfile.em
FROM osrf/ros:noetic-desktop-focal

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-desktop-full=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*
# RUN sudo apt-get install ros-noetic-laser_pipeline

# RUN /bin/bash -c "apt-get install ros-${ROS_DISTRO}-geometry2"

WORKDIR ${HOME}/ws/src
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash"
WORKDIR ${HOME}/ws
# CMD catkin_make
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install libsdl-image1.2-dev
RUN apt-get -y install libsdl-dev
RUN rosdep install --from-paths ./src --ignore-src
RUN apt-get -y install ros-noetic-openslam-gmapping
RUN apt-get -y install ros-noetic-move-base
RUN apt-get -y install ros-noetic-joy
RUN apt-get -y install python3-serial
RUN apt-get -y install python3-pip

RUN pip install -q -U google-generativeai
RUN pip install SpeechRecognition
RUN pip install PyQt5
RUN pip install pygame

RUN pip install pvrecorder
RUN pip install pvporcupine

RUN pip install deepface
RUN pip install opencv-contrib-python-headless==4.1.2.30
RUN pip install numpy==1.24.3
RUN pip install keras==2.13.1
RUN pip install gTTS

RUN apt-get -y install bc
RUN apt-get install -y wmctrl
# WORKDIR ${HOME}/ws/deepface
# # RUN touch hi.txt
# RUN pip install -e .

WORKDIR ${HOME}/ws
RUN echo "catkin_make" >> ~/.bashrc
# RUN echo "export ROS_MASTER_URI=http://10.42.0.1:11311" >> ~/.bashrc
# RUN echo "export ROS_IP=10.42.0.154" >> ~/.bashrc

RUN echo "source /ws/devel/setup.bash" >> ~/.bashrc
RUN echo "roslaunch joytf slam.launch" >> ~/.bashrc
