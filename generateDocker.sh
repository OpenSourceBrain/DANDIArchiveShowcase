docker build --platform linux/amd64 --network host -t dandi_docker .
docker run --privileged -v "$(pwd)":/testing --network=host -dit --name=da dandi_docker 
docker start da
echo done
docker exec da /bin/sh -c 'docker build -t nwbe OSBv2/applications/nwb-explorer/.'
echo on last
docker exec da /bin/sh -c 'docker run -dit --name=nwbe -v "$(pwd)"testing:/home/jovyan/nwb-explorer/testing nwbe'
