docker build --build-arg DOCKER_GID=$(awk -F: '$1=="docker" {print $3}' /etc/group) -t dandi_docker .
docker run --privileged -v "$(pwd)":/testing --network=host -dit --name=da dandi_docker 
docker start da
echo step1
docker exec da /bin/sh -c 'sudo usermod -aG docker $USER'
echo step2
docker exec da /bin/sh -c 'sudo systemctl status docker'
echo step3
docker exec da /bin/sh -c 'sudo systemctl start docker'
echo step4
docker exec da /bin/sh -c 'sudo docker container ps'
echo step5
docker exec da /bin/sh -c 'sudo docker build -t nwbe OSBv2/applications/nwb-explorer/.'
echo on6
docker exec da /bin/sh -c 'sudo docker run -dit --name=nwbe -v "$(pwd)"testing:/home/jovyan/nwb-explorer/testing nwbe'
