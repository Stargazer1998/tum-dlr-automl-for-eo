#!/bin/bash

# create the required directory for data storage on the temporary but super fast file tmpfs filesystem
mkdir -p /dev/shm/hai_nasb_eo/data

# Copy the data to the target storage directory
cp /p/project/hai_nasb_eo/data/*h5 /dev/shm/hai_nasb_eo/data

# Run the container with support for nvidia and cuda
module load Stages/2022  Apptainer-Tools/2022 GCCcore/.9.3.0

#apptainer pull docker://dockiron/mdsi2022-automl-torch1.9:latest
# `--nv` option enables nvidia support.
# apptainer run --nv mdsi2022-automl-torch1.9_latest.sif
apptainer exec --nv mdsi2022-automl-torch1.9_latest.sif python3 ./scripts/training_torchlightning.py --arch $1
