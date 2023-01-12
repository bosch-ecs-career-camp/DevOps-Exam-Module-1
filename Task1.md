# Task1 - Python Program for CarShop

A small local buisness is selling cars in the town. They came to us with a requirement for a Python program which can calculate their profit for given month.

1. Please create class for a CarShop where you can create a car object with the following properties:
 - Id                       "The id represents the number of sale, for example '1' "
 - Brand                    "The Brand represents the Car Model Name, for example 'BMW 320' "
 - PurchaseDate             "The purchase date represents the date when the car is sold, for example '2022/3/1'"
 - Price                    "The price of the sold car, for example '50000' "
 
2. Then there should be a class method which is calcucalting the profit for each month during the year and possibility to print to a file the profit for a given month.

3. Please create objects for the following sales over the year 2022.

- The sale with id 1 was a BMW 320 vehicle saled on day 1 of month 3(March) with a price tag of 50000.
- The sale with id 2 was a BMW 330 vehicle saled on day 10 of month 3(March) with a price tag of 60000.
- The sale with id 3 was an Audi A4 vehicle saled on day 2 of month 4(April) with a price tag of 70000.
- The sale with id 4 was an Audi A5 vehicle saled on day 5 of month 7(July) with a price tag of 75000.
- The sale with id 5 was an Audi A6 vehicle saled on day 7 of month 7(July) with a price tag of 90000.
- The sale with id 6 was an Audi A7 vehicle saled on day 15 of month 8(August) with a price tag of 120000.
- The sale with id 7 was an Mercedes CLS vehicle saled on day 2 of month 9(September) with a price tag of 150000.

4. Then the Result of the calculating function should result in 110000 if month 3(March) is given or 70000 if the given month was 4(April).

- calc_profit(3) -> 110000

5. The Program should be able to accept arguemnts from the command line ( Providing the month as a number in order to get the profit for a given month)

```sh
python main.py --month 3

Output:
For month 3(March): The profit of the CarShop is 110000
- ls: -> profit.txt
- cat profit.txt -> For month 3(March): The profit of the CarShop is 110000
```
