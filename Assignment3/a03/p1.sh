#! /bin/bash
if [ ! -d "$2" ]
then 
    #source directory not found
    echo "$2 not found" 
    exit 0
elif [ $# -ne 3 ]
then
    #missing input or more than required
    echo "USAGE: p1.sh <extension> <src_dir> <dst_dir>"
else
    #do part 1
    for file in `find $2 -name *$1`
    do
        #relative path to file base on old dir
        rpath=${file#$2}

        #filename by itself
        filename="$(basename "$file")"
        
        #old dir to file
        dir=${rpath%$filename}

        #location to be moved to
        loc="$3$dir"

        #make directory file will be moved to
        mkdir -p $loc

        #move file from current to new dir
        mv $file $loc
    done
fi
