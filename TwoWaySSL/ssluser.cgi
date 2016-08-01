#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>SERVER STATUS "
echo "</title></head><body>"

USER=`env | grep SSL_CLIENT_S_DN_CN | cut -f2 -d"=" ` 

echo "<pre>"

echo "USER is $USER"

echo " </pre>"

echo "</body></html>"
