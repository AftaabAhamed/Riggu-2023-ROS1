# !! no longer in development ROS1 implentation !!
# Riggu-2023
2023 Riggu 

[Speech Recognition  :](riggu_speech/speech.md)

# how to run docker

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

