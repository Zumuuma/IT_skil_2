#!/bin/sh

echo "___Start___"
BASE_DIR=$(pwd)
du -h -d 1 ./ | sort -k 1 -h -r | head -n 2 | tail -n 1
echo "___Finish___"

exit
