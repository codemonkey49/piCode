#!/bin/bash

echo "running"
curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add-
sudo apt-get install uv4l uv4l-raspicam
sudo apt-get install uv4l-raspicam-extras
echo "done"
sleep 40
sudo apt-get update
sudo apt-get upgrade