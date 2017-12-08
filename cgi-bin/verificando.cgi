#!/bin/bash
read OP
echo "content-type: text/html"
echo
PO=$(echo $OP | cut -d"=" -f2)

echo "<html>"
 um(){
	./ciclo_ping.cgi
	echo "	
}
echo "</html>"
