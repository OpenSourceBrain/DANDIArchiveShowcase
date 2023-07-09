docker build --network=host -t dandi_docker .
docker run -v /var/run/docker.sock:/var/run/docker.sock -d -t --name=da dandi_docker tail -f /dev/null

docker exec da docker --version
echo step1
docker exec da  docker container ps
echo step2
docker exec da  docker build -t nwbe OSBv2/applications/nwb-explorer/.
echo step3
docker run da
docker exec da docker run -dit --name=nwbe -v "$(pwd)"testing:/home/jovyan/nwb-explorer/testing nwbe
