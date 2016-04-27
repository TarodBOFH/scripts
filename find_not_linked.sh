#!/bin/sh
#find -links 1
#find -mindepth 2 -links 2 -exec find -L . -maxdepth 1 -samefile '{}' \;
if [ $# -eq 0 ] 
	then 
	echo "Finds files in subdirectories with two links which only exists on that directory tree."
	echo "Example: some_file -> ./some_folder/some_file"
	echo
	echo "Used to find files with links in Downloads that have not been linked to plex"
	echo 
	echo "Usage $0 destination pattern "
	echo 
	exit -1
fi
DST=$1
find $1 -mindepth 2 -type f -links 2 -exec find -L $1 -maxdepth 1 -type f -samefile '{}' \;
