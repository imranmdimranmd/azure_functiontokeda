#!/bin/bash
c=1
while [ $c -le 250 ]
do
	if curl "http://functiondemo.centralindia.cloudapp.azure.com/leave/api/MyLeaveDetails"; then
		echo "Campaigns website is up $c"
	else
		echo "Campaigns website is down $c"
	fi
	(( c++ ))
done

