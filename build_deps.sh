#!/bin/bash
mkdir -p /lib
cd /lib

git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
git checkout ad8b5f83
sed -i -e "193,198d" ./src/utils/file_utils.cpp
cmake -B build -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PANGOLIN_DEPTHSENSE=OFF \
    -DBUILD_PANGOLIN_FFMPEG=OFF \
    -DBUILD_PANGOLIN_LIBDC1394=OFF \
    -DBUILD_PANGOLIN_LIBJPEG=OFF \
    -DBUILD_PANGOLIN_LIBOPENEXR=OFF \
    -DBUILD_PANGOLIN_LIBPNG=OFF \
    -DBUILD_PANGOLIN_LIBREALSENSE=OFF \
    -DBUILD_PANGOLIN_LIBREALSENSE2=OFF \
    -DBUILD_PANGOLIN_LIBTIFF=OFF \
    -DBUILD_PANGOLIN_LIBUVC=OFF \
    -DBUILD_PANGOLIN_LZ4=OFF \
    -DBUILD_PANGOLIN_OPENNI=OFF \
    -DBUILD_PANGOLIN_OPENNI2=OFF \
    -DBUILD_PANGOLIN_PLEORA=OFF \
    -DBUILD_PANGOLIN_PYTHON=OFF \
    -DBUILD_PANGOLIN_TELICAM=OFF \
    -DBUILD_PANGOLIN_TOON=OFF \
    -DBUILD_PANGOLIN_UVC_MEDIAFOUNDATION=OFF \
    -DBUILD_PANGOLIN_V4L=OFF \
    -DBUILD_PANGOLIN_VIDEO=OFF \
    -DBUILD_PANGOLIN_ZSTD=OFF \
    -DBUILD_PYPANGOLIN_MODULE=OFF
cmake --build build -j8

cd /lib
rosdep update
git clone --recursive --depth 1 https://github.com/stella-cv/stella_vslam.git
rosdep install -y -i --from-paths /lib
cd /lib/stella_vslam
mkdir -p /lib/stella_vslam/build
cd /lib/stella_vslam/build
source /opt/ros/humble/setup.bash
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make -j8
sudo make install

# When building with support for PangolinViewer
cd /lib
git clone --recursive https://github.com/stella-cv/pangolin_viewer.git
mkdir -p pangolin_viewer/build
cd pangolin_viewer/build
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make -j8
sudo make install
