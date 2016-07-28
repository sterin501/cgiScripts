#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>VM server Status "
echo "</title></head><body>"
echo "<h1>VM servers  </h1>"



echo ""


FILENAME=/tmp/cgi`date +%m%d%Y_%H%M%S` 

SERVERS="master.comapany.com datanode.company.com"
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

echo " <a href="http://IP/cgi-bin/vmserver.cgi">VNC PORT OF VM IMAGES  <a> "


echo " <pre>                            </pre>"

echo " <a href="http://IP/cgi-bin/serverping.cgi">PING SERVER  <a> "

echo "</body></html>"


