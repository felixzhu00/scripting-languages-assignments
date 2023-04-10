#! /bin/bash
if [ $# -lt 2 ]
then 
    echo "input file and dictionary missing"
elif [ ! -f "$1" ]
then
    echo "$1 is not a file"
elif [ ! -f "$2" ]
then
    echo "$2 is not a file"
else
    r=$(sed -e $'s/,/\\\n/g' $1 |
    awk -F'[\n ]+' '
        {
            for(i=1;i<=NF;i++)
                if(length($i) == 5){
                    print $i
                }
        }
    ')

    myArray=($r)

    for str in ${myArray[@]}; do 
        if ! grep -q $str $2;
            then echo $str
        fi
    done
fi