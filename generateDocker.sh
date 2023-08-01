docker build --network=host -t dandi_docker .
docker volume create --name tmpf
docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/testing -v tmpf:/tmp -d --name=da dandi_docker tail -f /dev/null
docker exec da  docker build -t nwbe OSBv2/applications/nwb-explorer/.
docker run -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/home/jovyan/nwb-explorer/testing -v tmpf:/tmp -d --name=nwbe nwbe tail -f /dev/null
echo Completed!
