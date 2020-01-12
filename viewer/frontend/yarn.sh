docker run \
    --rm \
    -v $PWD:/frontend \
    -w /frontend \
    node:13.6.0-slim \
    /bin/bash -c "yarn;"
