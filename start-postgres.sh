#!/bin/bash
#creating volume
Volume='postgresVol'
if [ ! -n "`docker volume ls |grep -w ${Volume}`" ]; then
	docker volume create ${Volume}	
fi
echo "Running Postgres Instance $BUILD"
if [ ! -n "`docker ps|grep -w ${BUILD}`" ] ; then
	#docker run   -p 5432:5432 --detach -t postgress --name localPostgres 
	docker run  -v ${postgresVol}:${PGDATA } -p 5432:5432 --detach -t  ${BUILD}
else
	echo "Postgres already running"
fi
