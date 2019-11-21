#!/bin/sh

if [ ! -z $1 ] ; then 
	curl --head --silent  $1 | grep -i location | cut -d " " -f 2
fi
