#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>VM server Status "
echo "</title></head><body>"
echo "<h1>VM servers  </h1>"



echo ""


FILENAME=/tmp/cgi`date +%m%d%Y_%H%M%S` 

SERVERS="10.184.36.29 10.184.36.139 10.184.36.133 10.184.36.127 10.184.36.148"
USR="root"



command="/root/getvnc.sh"



# connect each host and pull up user listing
for host in $SERVERS

do

echo "      " >> $FILENAME

#echo " $host "  >> $FILENAME

ssh  $USR@$host  $command   >> $FILENAME


done


echo "<pre>"
cat  $FILENAME
echo "</pre>"

echo " "

echo " <a href="http://10.184.36.141/cgi-bin/vmserver.cgi">VNC PORT OF VM IMAGES  <a> "


echo " <pre>                            </pre>"

echo " <a href="http://10.184.36.141/cgi-bin/serverping.cgi">PING SERVER  <a> "

echo "</body></html>"


