#!/bin/sh
#
# LaunchBar Action Script
#

cd /Users/apple/Library/Rime
echo "$# arguments passed"
for ARG in "$@"; do
    LOWERCASE=$(echo $ARG | tr '[A-Z]' '[a-z]')
    echo "$ARG $LOWERCASE" >> luna_pinyin.extended.dict.yaml
done

