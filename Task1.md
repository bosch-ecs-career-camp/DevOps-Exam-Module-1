# Task1 - Python Program for CarShop

A small local buisness is selling cars in the town. They came to us with a requirement for a Python program which can calculate their profit for given month.

1. Please create a python class for a CarShop where you can create a car object with the following properties:

| Property | Description |
| ----------- | ----------- |
| Id  | The id represents the number of sale, for example '1'  |
| Brand | The Brand represents the Car Model Name, for example 'BMW 320' |
| PurchaseDate  | The purchase date represents the date when the car is sold, for example '2022/3/1'  |
| Price | The price of the sold car, for example '50000' |
 
2. Then there should be a class method which is calcucalting the profit for each month during the year and possibility to print to a file the profit for a given month.

3. Please create objects for the following sales over the year 2022.

- The sale with id 1 was a BMW 320 vehicle saled on day 1 of month 3(March) with a price tag of 50000.
```
{
  "id": "1",
  "Brand": "BMW320",
  "PurchaseDate": "2022/3/1",
  "Price": "50000"
}
```

- The sale with id 2 was a BMW 330 vehicle saled on day 10 of month 3(March) with a price tag of 60000.
```
{
  "id": "2",
  "Brand": "BMW330",
  "PurchaseDate": "2022/3/10",
  "Price": "60000"
}
```

- The sale with id 3 was an Audi A4 vehicle saled on day 2 of month 4(April) with a price tag of 70000.
```
{
  "id": "3",
  "Brand": "AudiA4",
  "PurchaseDate": "2022/4/2",
  "Price": "70000"
}
```

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
