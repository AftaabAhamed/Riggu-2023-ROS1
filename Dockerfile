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


WORKDIR ${HOME}/ws
RUN echo "source /ws/devel/setup.bash" >> ~/.bashrc
RUN echo "catkin_make" >> ~/.bashrc
RUN echo "roslaunch joytf slam.launch" >> ~/.bashrc