#!/bin/bash
c=1
while [ $c -le 250 ]
do
	if curl -v "http://functiondemo.centralindia.cloudapp.azure.com/demo/api/helloworld" 2>&1 | grep -w "200\|301"; then
		echo "Campaigns website is up $c"
	else
		echo "Campaigns website is down $c"
	fi
	(( c++ ))
done

