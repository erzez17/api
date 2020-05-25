#! /bin/bash
erez=$(curl -s 'http://localhost:443/isalive')
if [ "$erez" = "true" ]
then
	echo "true"
else
	echo  "false"
fi 

