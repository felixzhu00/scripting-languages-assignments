#! /bin/bash
if [ ! -f "$1" ]
then
    #input file not found
    echo "$1 not found"
elif [ $# -lt 2 ]
then
    #either the data file or the output file path is not provided
    echo "data file or output file not found"
else
    #do part 2
    awk -F'[,;:]' '{for(i=1;i<=NF;i++)$i=(a[i]+=$i)} END{for(j=1;j<=NF;j++){print ("Col "j" : "$j)}}' $1 > $2
fi