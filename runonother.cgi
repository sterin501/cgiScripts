#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>RUN ON OTHER SERVER "
echo "</title></head><body>"
echo "<h4> current server is `hostname`  </h4>"


FILENAME=/tmp/cgi`date +%m%d%Y_%H%M%S` 

SERVERS="datanode.company.com "
# other server can be add by putting space

USR="hduser"

command="/home/hduser/getstatus.sh"

for host in $SERVERS

do



ssh  $USR@$host  $command   >> $FILENAME


done


echo "<pre>"
cat  $FILENAME
echo "</pre>"


echo "</body></html>"

