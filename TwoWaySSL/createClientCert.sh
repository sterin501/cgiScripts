mkdir $1
cd $1
cp ../ca.cer .
cp ../ca.key .
cp ../openssl.cnf .
openssl genrsa -out client.key 2048
openssl req -config ./openssl.cnf -new -key client.key -out client.req
openssl x509 -req -in client.req -CA ca.cer -CAkey ca.key -set_serial 101 -extfile openssl.cnf -extensions client -days 3650 -outform PEM -out client.cer
openssl pkcs12 -export -inkey client.key -in client.cer -out $1.p12
openssl verify -CAfile ca.cer client.cer
rm -f ca.cer ca.key client.key client.req client.cer

