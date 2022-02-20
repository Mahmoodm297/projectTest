#!/bin/bash

if [ ! -n "`docker ps|grep -w ${postgress}`" ] ; then
	#docker run   -p 5432:5432 --detach -t postgress --name localPostgres 
	docker run   -p 5432:5432 --detach -t  ${BUILD}
else
	echo "Postgres already running"
fi
