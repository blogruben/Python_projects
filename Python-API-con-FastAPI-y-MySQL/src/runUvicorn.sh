#!/bin/bash

# Install mysqladmin
echo "apt-get update 1> /dev/null && apt-get install -y mysql* 1> /dev/null"
apt-get update 1> /dev/null && apt-get install -y mysql* 1> /dev/null

# Wait until MySQL is up.
until mysqladmin -h mysql -u$MYSQL_USER -p$MYSQL_PASSWORD processlist 2> /dev/null | grep -q $MYSQL_USER
do
	echo " Waiting DB conection ..."
	sleep 2
done
echo "Connection establish."
mysqladmin -h mysql -u$MYSQL_USER -p$MYSQL_PASSWORD processlist


# Si existe la variable ENTORNO y es igual desarrollo levantamos
# el servidor en modo reload para cargar los cambios en caliente.
if [ -n "$ENTORNO" ] && [ "$ENTORNO" = desarrollo ]; then uvicorn main:app --host=0.0.0.0 --reload; fi
if [ -n "$ENTORNO" ] && [ "$ENTORNO" = produccion ]; then uvicorn main:app --host=0.0.0.0; fi