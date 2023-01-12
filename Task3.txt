# Bash

For each and every new employee in Bosch, there must be an unique Bosch ID and email created. 
Bosch ID is a function of all three name, family name and region, following the pattern below:
First two characters from user's family name + first character from users' name + unique sequence number + region abbreviation which users' office belong to. 

So far our mighty administation team used to do it manually. Your goal is to help them out by automating the process.
For the sake of this you must create a script named user_list_update.bash which does the following: 
1. Reads an input from CLI getting Name, Surname and Region
2. Generates proper Bosch ID and email
3. It fills all the results into user_db.csv file. 

Constraints:
1. If region is Bulgaria, office is set to 'sf' , if region is Germany office is set to 'de', for all other locations office is set to 'eu' 
2. Name and surname inputs will be strings starting with capital letter and lowercase
3. Region input will be a string with both upper and lowercase   
4. Script must create user_db.scv file in case it doesn't exists. It must update the file in case it's present already
5. Resulting Bosch ID is always lowercase


Examples:
 
./user_list_update.bash
Name: Christo
Surname: Rodopov
Region: Bulgaria

cat user_db.csv
Name, Region, User, Email
Christo Rodopov, Bulgaria, roc1sf, roc1sf@bosch.com

./user_list_update.bash
Name: Hristo
Surname: Stoichkov
Region: Bulgaria

cat user_db.csv
Name, Region, User, Email
Christo Rodopov, Bulgaria, roc1sf, roc1sf@bosch.com
Hristo Stoichkov, Bulgaria, sth1sf, sth1sf@bosch.com

./user_list_update.bash
Name: Haralampi
Surname: Stoyanov
Region: Bulgaria

cat user_db.csv
Name, Region, User, Email
Christo Rodopov, Bulgaria, roc1sf, roc1sf@bosch.com
Hristo Stoichkov, Bulgaria, sth1sf, sth1sf@bosch.com
Haralampi Stoyanov, Bulgaria, sth2sf, sth2sf@bosch.com

./user_list_update.bash
Name: Christiano
Surname: Ronaldo
Region: Germany

cat user_db.csv
Name, Region, User, Email
Christo Rodopov, Bulgaria, roc1sf, roc1sf@bosch.com
Hristo Stoichkov, Bulgaria, sth1sf, sth1sf@bosch.com
Haralampi Stoyanov, Bulgaria, sth2sf, sth2sf@bosch.com
Christiano Ronaldo, Germany, roc1de, roc1de@bosch.com
