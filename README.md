# Riggu-2023
2023 Riggu 

Riggu is a autonomous mapping and navigation robot with additional human interface features. 
It has a  QT based GUI and voice recognition and speech functionality as well. It utilises gemini api for intelligence.  
</br>


<div align='center'>
    <img src="./riggu-body-img.jpeg">
    </br>
    map of robotics lab generated using gmapping package in ROS
    </br>
    <img src="./map-gen-img.jpeg">
    </br>
    Navigation of the robot visualised in RViz
    </br>
    <img src="./nav-img.jpeg">
</div>

# Built With

![ROS Noetic](https://github.com/ros-infrastructure/artwork/blob/master/ros_logo.svg)

# how to run riggu docker image

install docker using 

```bash
sudo apt install docker.io
```

cd into cloned directory
and build image using this command 

```bash
sudo docker build -t riggu_img .
```

to run the image w/o a gui
```bash
sudo docker run -it --net=host -v "$PWD":/ws  riggu_img
```
with display
```bash
xhost +local:root
```
```bash
sudo docker run -it --net=host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -v "$PWD":/ws  riggu_img
```
with devices
```bash
 sudo docker run -it --net=host \
 --env="DISPLAY" \
 --env="QT_X11_NO_MITSHM=1" \
 --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
 --privileged -v /dev/bus/usb:/dev/bus/usb \
 -v "$PWD":/ws  riggu_img
```

