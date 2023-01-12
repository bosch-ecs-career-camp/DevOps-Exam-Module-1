# Task1 - Python

## A small local buisness is selling cars in the town. They came to us with a requirement for a Python program which can calculate their profit for given month.
## Please create class for a Carshop where you can create a car object with the following properties:
 - Brand: ("String")
 - Purchase date: (hint: use datetime() function for the date)
 - Price of the sold car: ("Int")
 
## Then there should be a a class method which is calcucalting the profit for a given month.

- For Example:

> The Company saled 3 cars through 2022 year.

1. The first sale was a BMW 320 vehicle saled on the 1st day of month 3(March) with a price tag of 50000.
```
carA_sale_date = dt.datetime(2022,3,1)
carA - ("BMW 320",carA_sale_date, "50000")
```

2. The second sale was a BMW 330 vehicle saled on the 10th day of month 3(March) with a price tag of 60000.
```
carB_sale_date = dt.datetime(2022,3,10)
carB - ("BMW 330",carB_sale_date, "60000")
```

3. The third sale was an Audi A4 vehicle saled on the 2nd day of month 4(April) with a price tag of 70000.
```
carC_sale_date = dt.datetime(2022,4,2)
carC - ("BMW A4",carC_sale_date, "70000")
```

## Then the Result of the calculating functiong should result in 110000 if month 3(March) is given or 70000 if the given month was 4(April)..
