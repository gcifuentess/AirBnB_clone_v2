#!/usr/bin/env bash
# install and configure nginx
SERVED_BY="a\\\tadd_header X-Served-By \"\$HOSTNAME\";"
LOCATION="hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}"

apt-get -y update
apt-get -y install nginx
sed -i "/listen \[::\]:80 default_server/ $SERVED_BY" /etc/nginx/sites-available/default
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /$LOCATION" /etc/nginx/sites-available/default
service nginx restart
