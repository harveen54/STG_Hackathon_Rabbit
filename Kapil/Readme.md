For installing darknet

git clone https://github.com/pjreddie/darknet
cd darknet
make



For Testing image

./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg
