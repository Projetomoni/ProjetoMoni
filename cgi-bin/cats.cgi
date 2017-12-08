#!/bin/bash
read SO
VAI=$(echo $SO | cut -d"=" -f2)
echo "content-type: text/html"
echo

um(){
	cat resto/arm_info
}

dois(){
	cat resto/arm_infolog
}

case $SO in

	"arm_info") um ;;
	"arm_infolog") dois ;;
	*) echo "<h1>Opção Inexistente</h1>"

esac
