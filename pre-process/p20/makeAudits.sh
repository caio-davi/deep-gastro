#!/bin/bash


echo Populating audit



train="train/images/"



~/Apps/ImageMagick/magick convert -delay 200 -loop 0 "${TRAIN_PATH}.0png" train/labels/0.png audit/0.gif



# for file in $files
# do
#   echo $(basename $file)
# done