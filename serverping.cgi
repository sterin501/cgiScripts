#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>SERVER STATUS "
echo "</title></head><body>"
echo "<h1> SERVER PINGS   </h1>"



echo ""


#echo "             IP            HOSTNAME                        Machine     Owner   Location       Staus  "

FILENAME=/tmp/cgi`date +%m%d%Y_%H%M%S` 








cat /var/www/cgi-bin/hostlist.txt  | while read LINE

do

if echo   $LINE  | grep 10 > /tmp/null 

then


echo   $LINE   | cut -f1 -d" "  > /tmp/hosts  



#echo  "  $LINE "  

./pingserver.sh  ` cat  /tmp/hosts `  > /tmp/hostsStatus

echo  "  $LINE  `cat /tmp/hostsStatus ` "  >>  $FILENAME 

else

echo   $LINE  >>  $FILENAME

fi


done


echo "<pre>"
cat  $FILENAME
echo "</pre>"


echo " <a href="http://IP/cgi-bin/vmserver.cgi">VNC PORT OF VM IMAGES  <a> "

echo " <pre>                            </pre>"

echo " <a href="http://IP1/cgi-bin/serverping.cgi">PING SERVER  <a> "



echo "</body></html>"
