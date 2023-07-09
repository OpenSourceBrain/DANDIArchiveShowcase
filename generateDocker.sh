docker build -t dandi_docker .
docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock -d --name=da dandi_docker 
echo step1
docker exec da  docker container ps
echo step2
docker exec da  docker build -t nwbe OSBv2/applications/nwb-explorer/.
echo step3
docker exec da docker run -dit --name=nwbe -v "$(pwd)"testing:/home/jovyan/nwb-explorer/testing nwbe
