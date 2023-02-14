#! /bin/bash

# it checks if resulting csv file is present. In case not, it creates it with initial row of the table
export DB=user_db.csv
[[ ! -f $DB ]] && echo "Name, Region, User, Email" > $DB

# read input from user. 
# just an example of a validation in case of empty input from user. Not needed according to the assignment
while [ -z $NAME ]
do 
    read -p "Name: " NAME
done

while [ -z $SURNAME ]
do 
    read -p "Surname: " SURNAME
done

while [ -z $RG ]
do 
    read -p "Region: " RG
done

# sets proper location as per user input. According to assignment is not clear if input is upper or lower case thus it must be handled properly
case $RG in
    [Bb][uU][Ll][gG][Aa][Rr][iI][Aa] ) export OFFICE=sf
        ;;
    [Gg][eE][Rr][Mm][Aa][Nn][yY] ) export OFFICE=de 
        ;;
    *) export OFFICE=eu
        ;;
esac

# those below used for checking if an ID is already in use
export RES=0
export CNT=1

while [  $RES == 0 ]
do
    export BOSCH_ID=${SURNAME:0:2}${NAME:0:1}$CNT${OFFICE}
    grep -i $BOSCH_ID $DB
    RES=$?
    let CNT++
done 

# stores and sets ID to lower case. It store mail as well 
BOSCH_ID=${BOSCH_ID,,}
MAIL=$BOSCH_ID@bosch.com

# adds the result to DB file
echo $NAME, $SURNAME, $BOSCH_ID, $MAIL >> $DB

# below was not needed but I usually set something at the end of the script notifying we are all done.
echo ""
echo "Done and done! "

# last but not least. According to the assignment we haven't expecting any logging but keep in mind that this is so useful that it's almost mandatory ;) 


