ping -c1 -W1 -q $1 &>/dev/null
status=$( echo $? )
if [[ $status == 0 ]] ; then
     echo "UP"
else
     echo "DOWN"
fi
