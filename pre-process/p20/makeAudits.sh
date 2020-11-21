#!/bin/bash


echo "Populating audit"



TRAIN_IMAGES="train/images/"
TRAIN_LABELS="train/labels/"

TRAIN_AUDITS="audit/"




# num_images= ls -1q $TRAIN_IMAGES | wc -l


for ((i=50; i<=63; i++)); do
        ~/Apps/ImageMagick/magick convert -delay 200 -loop 0 "${TRAIN_IMAGES}${i}.png" "${TRAIN_LABELS}${i}.png" "${TRAIN_AUDITS}${i}.gif"
    done

echo "Done"
# for file in ${TRAIN_IMAGES}*.png
# do
#   echo  $file
# done