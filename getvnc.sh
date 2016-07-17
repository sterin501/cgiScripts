IP=`ifconfig | grep 255.255.252.0 | awk '{print $2}' | cut -f2 -d":"`

echo "..................................................."
echo $IP
echo "..................................................."

for i in `ps -ef | grep vnc | grep -v grep | awk '{print $2}'`

do

#netstat -anp | grep $i | grep LISTEN | awk '{print $4}'

#echo " `ps -ef | grep $i | grep -v grep |  grep -oP "(?<=-domain-name )[^ ]+"`   `netstat -anp | grep $i | grep LISTEN | awk '{print $4}'` "

#echo "`netstat -anp | grep $i | grep LISTEN | awk '{print $4}'`  `ps -ef | grep $i | grep -v grep |  grep -oP "(?<=-domain-name )[^ ]+"`  "


echo "`netstat -anp | grep $i | grep LISTEN | awk '{print $4}' | sed 's/0.0.0.0/'$IP'/g' `  `ps -ef | grep $i | grep -v grep |  grep -oP "(?<=-domain-name )[^ ]+"` "

done
