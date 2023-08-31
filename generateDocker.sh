#!/bin/bash
set -ex

# Clean up if previously run
docker stop nwbe || echo Docker container nwbe not running
docker rm nwbe || echo Docker container nwbe not running
docker stop da || echo Docker container da not running
docker rm da || echo Docker container da not running

docker build --network=host -t dandi_docker .
docker volume create --name tmpf
docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/testing -v tmpf:/tmp --memory="8g" -e PYTHONBUFFERED=1 --oom-kill-disable -d --name=da dandi_docker tail -f /dev/null
docker exec da  docker build -t nwbe OSBv2/applications/nwb-explorer/.
docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/home/jovyan/nwb-explorer/testing -v tmpf:/tmp --memory="8g" -e PYTHONBUFFERED=1 -d --name=nwbe nwbe tail -f /dev/null
echo Completed!
