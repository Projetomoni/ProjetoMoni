#!/bin/bash
read POST
IP=$(echo $POST | cut -d"=" -f2)
echo "content-type: text/html"
echo
echo "<h1>POST: $POST</h1>"
echo "<h1>IP: $IP</h1>"
ping -W 1 -c 1 -i 1 $IP &> /dev/null
[[ $? == "0" ]] && echo "<h2>[$(date) ip:$IP]->UP</h2>" || echo "<h2>[$(date) ip:$IP]->DOWN</h2>"
