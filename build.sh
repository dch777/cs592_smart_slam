#!/bin/bash

git clone https://github.com/stevenlovegrove/Pangolin
cd Pangolin
./scripts/install_prerequisites.sh --dry-run recommended # Check what recommended softwares needs to be installed
./scripts/install_prerequisites.sh recommended # Install recommended dependencies
cmake -B build
cmake --build build -j4
sudo cmake --install build

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/local
sudo ldconfig

cd ..
colcon build --symlink-install
