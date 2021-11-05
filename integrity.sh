for FILE in training/$1/*.pdf
do
    if [ $(head -c 4 "$FILE") != "%PDF" ]; then
        echo "ERROR" $FILE
    fi
done
