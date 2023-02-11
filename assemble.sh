#!/bin/bash
linking_c=false
while getopts 'cd:' OPTION; do
    case "$OPTION" in 
        c)
            linking_c=true
            ;;
            
        d)
            echo "$OPTARG"
            ;;
        ?)
            echo "Incorrect Flag";;
    esac
done
shift "$(($OPTIND -1))"
if [ -z $* ]; then
    echo "ERROR: Assembly File Not Found"
    exit
fi

if [ "$linking_c" = true ]; then
    aarch64-linux-gnu-as $* -o temp.o
    aarch64-linux-gnu-ld temp.o -lc
    qemu-aarch64 -L /usr/aarch64-linux-gnu/ a.out

    rm temp.o
    rm a.out
else
    aarch64-linux-gnu-as $* -o temp.o
    aarch64-linux-gnu-ld temp.o
    qemu-aarch64 a.out

    rm temp.o
    rm a.out
fi
