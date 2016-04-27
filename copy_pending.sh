#!/bin/sh
#find -links 1
if [ $# -lt 2 ] 
	then 
	echo "Usage $0 src destination new_name args"
	echo 
	echo "Please don't use wildcards on params"
	exit -1
fi

SRC=$1
DST=$2

shift 2

find "$SRC" -maxdepth 1 -type f -links 1 -exec ln '{}' "$DST" \;
/sbin/series_renamer.py "$DST" "$@"
