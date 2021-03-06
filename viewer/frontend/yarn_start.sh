docker rm -f concert-master_front
docker run -d \
    --name concert-master_front \
    -p 3000:3000 \
    -w /frontend \
    -v $PWD:/frontend \
    --restart="always" \
    node:13.6.0-slim \
    yarn start
docker logs -f concert-master_front 
