# Riggu-2023
2023 Riggu 
Riggu is a autonomous mapping and navigation robot with additional human interface features 
### Built With

*[https://img.shields.io/ros/v/noetic/moveit_msgs.svg)]

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

