#! /bin/bash
if [ $# -lt 1 ]
then 
    echo "score directory missing"
elif [ ! -d "$1" ]
then
    echo "$1 is not a directory"
else
    #do part 3
    for file in $1/*
    do
        awk -F'[,]' '
        FNR == 2 {
            id = $1
            sum = 0
            for(i=2;i<=NF;i++){
                sum+=$i
            } 
            sum*=2
            if (sum >= 93 && sum <= 100){
                print(id " : A")
            }else if (sum >= 80){
                print(id " : B")
            }else if (sum >= 65){
                print(id " : C")
            }else if (sum >= 50){
                print(id " : D")
            }else if (sum > 50){
                print(id " : F")
            }else{
                print("score not in range")
            }
        }
        ' $file
    done
fi

