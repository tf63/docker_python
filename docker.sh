#!/bin/bash
# code from https://github.com/RUB-SysSec/GANDCTAnalysis/blob/master/docker.sh
# Copyright (c) 2021 Chair for Sys­tems Se­cu­ri­ty, Ruhr University Bochum

# usage ----------------------------------------------
# bash docker.sh build  # build image
# bash docker.sh shell  # run container as user
# bash docker.sh root  # run container as root
# ----------------------------------------------------

DATASET_DIRS="$HOME/dataset"
DATA_DIRS="$HOME/data"

build()
{
    docker build . -f docker/Dockerfile --build-arg USER_UID=`(id -u)` --build-arg USER_GID=`(id -g)` -t tf63/python
}

shell() 
{
    docker run --rm --user user --shm-size=16g -it -v $(pwd):/app -v $DATASET_DIRS:/dataset -v $DATA_DIRS:/data tf63/python /bin/bash
}

root()
{
    docker run --rm --user root --shm-size=16g -it -v $(pwd):/app -v $DATASET_DIRS:/dataset -v $DATA_DIRS:/data tf63/python /bin/bash
}

if [[ $1 == "build" ]]; then
    build
elif [[ $1 == "shell" ]]; then
    shell 
elif [[ $1 == "root" ]]; then
    root
else
    echo "error: invalid argument"
fi
