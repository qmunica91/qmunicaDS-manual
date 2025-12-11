#!/usr/bin/env bash

while getopts r:t:m: option
do
 case "${option}"
 in
 r) TAG=${OPTARG};;
 t) TEMPLATE=${OPTARG};;
 m) MODE=${OPTARG};;
 esac
done

if [ -z "$MODE" ]
then
      MODE="public"
fi

if [ -z "$TEMPLATE" ]
then
      TEMPLATE="qmunica"
fi

# 1. Run the scan to ensure config is up to date
echo "Scanning content..."
php scan_content.php

# 2. Build Public
echo "Building PUBLIC version..."
php generate.php $TEMPLATE public

# 3. Build Full
echo "Building FULL version..."
php generate.php $TEMPLATE full

# 4. Merge and Cleanup
echo "Merging FULL version into Public/Full..."
mkdir -p output/public/full
cp -R output/full/* output/public/full/
rm -rf output/full

echo "Done! ALL content is now in: output/public"
echo "  - Public web: output/public"
echo "  - Intranet:   output/public/full"
