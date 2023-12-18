#!/bin/bash

touch default.txt

if [ "$#" -eq 0 ]; then
  echo -e "Usage ./install.sh [option] \nSet Default Color: \n\033[0;31m-r <red> \n\033[0;33m-o <orange> \n\033[0;33m-y <yellow> \n\033[0;32m-g <green> \n\033[0;36m-b <blue> \n\033[0;35m-p <purple> \n\033[0;37m-w <white>\n"
else
  while getopts ":roygbpw" opt; do
    case $opt in
      r)
        echo '\033[0;31m' > default.txt
        ;;
      o)
        echo '\033[0;33m' > default.txt
        ;;
      y)
        echo '\033[0;33m' > default.txt
        ;;
      g)
        echo '\032[0;32m' > default.txt
        ;;
      b)
        echo '\033[0;36m' > default.txt
        ;;
      p)
        echo '\033[0;35m' > default.txt
        ;;
      w)
        echo '\033[0;37m' > default.txt
        ;;
      \?)
        echo 'Invalid options: -$OPTARG'
        exit 1
        ;;
    esac
  done
  chmod +x calcmenu.sh
  shift $((OPTIND-1))
  echo "[*] Installation Complete"
fi  
