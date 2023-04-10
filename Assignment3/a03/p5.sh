#! /bin/bash
if [ $# -lt 1 ]
then 
    echo "input directory is missing"
elif [ ! -d "$1" ]
then
    "the directory does not exist"
else
    cd $1

    echo "Current date and time: "$(date)
    echo "Current directory is: "$(pwd)
    echo ""
    echo "--- 10 most recently modified directories ---"
    echo "$(ls -l -t | head | grep ^d)"
    echo ""
    echo "--- 6 largest files ---"
    echo "$(ls -l -S -r | grep ^- | head -n 6)"
    echo ""
    echo "======================================================================"
fi

