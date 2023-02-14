# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:25:54 2023

@author: CHZ1SF
"""

import sys
import datetime
import argparse

class CarShop():

    def __init__(self, id, cBrand, cPurchaseDate, cPrice):
     
        self._year = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        self._id = id
        self._cBrand = cBrand
        self._cPurchaseDate = cPurchaseDate
        self._cPrice = cPrice
        self._profit = {}
        
    def get_year_map(self):
        
        return self._year

    def get_total_profit(self):
        
        return self._profit

    def search_month_profit(self,searchedMonth):
        
        if self._profit != {}:
            for month,profit_value in self._profit.items():
                if searchedMonth == month:
                    return profit_value

    def add_carshop_profit(self, _id, _cBrand, _cPurchaseDate, _cPrice):

        if _id != None and _cBrand != None and _cPurchaseDate != None and _cPrice != None:
            
            saledCars = CarShop(_id,_cBrand,_cPurchaseDate,_cPrice)
            
        if saledCars != None:

            monthOfPurchase = str(_cPurchaseDate).split("-")[1]
            priceOfPurchase = int(_cPrice)

            current_profit_for_month = self.search_month_profit(monthOfPurchase)
            if current_profit_for_month != None:
                priceOfPurchase += int(current_profit_for_month)

            self._profit[monthOfPurchase] = priceOfPurchase
        
    def write_total_profit(self):
    
        with open("profit.txt","w+",encoding="utf-8") as profit_file:
            try:
                for monthNumber,monthName in self.get_year_map().items():
                    carShopProfit = self.search_month_profit(monthNumber)
                    profit_file.write("For Month %s The Profit of the CarShop is %s\n" % (monthName,carShopProfit))

            except KeyError as e:
                pass

def main(month):

    try:
        saledCars = CarShop("","","","")
        saledCars.add_carshop_profit(1,"Audi", datetime.datetime(2023,1,1), "100000")
        saledCars.add_carshop_profit(2,"BMW", datetime.datetime(2023,2,1), "50000")
        saledCars.add_carshop_profit(3,"BMW2", datetime.datetime(2023,3,11), "100000")
        saledCars.add_carshop_profit(4,"BMW3", datetime.datetime(2023,3,12), "50000")
        saledCars.add_carshop_profit(5,"BMW4", datetime.datetime(2023,3,17), "50000")
        
        saledCars.add_carshop_profit(6,"Audi", datetime.datetime(2023,4,2), "100000")
        saledCars.add_carshop_profit(7,"BMW", datetime.datetime(2023,5,17), "50000")
        saledCars.add_carshop_profit(8,"BMW2", datetime.datetime(2023,6,11), "10000")
        saledCars.add_carshop_profit(9,"BMW3", datetime.datetime(2023,7,12), "50000")
        
        saledCars.add_carshop_profit(10,"Audi", datetime.datetime(2023,8,2), "100000")
        saledCars.add_carshop_profit(11,"BMW", datetime.datetime(2023,9,17), "50000")
        saledCars.add_carshop_profit(12,"BMW2", datetime.datetime(2023,10,11), "10000")
        saledCars.add_carshop_profit(13,"BMW3", datetime.datetime(2023,11,12), "50000")
        #saledCars.add_carshop_profit(14,"BMW3", datetime.datetime(2023,12,13), "50000")
        saledCars.add_carshop_profit(14,"BMW2", datetime.datetime(2023,3,11), "100000")
    
        saledCars.write_total_profit()

        return saledCars.search_month_profit(month)
    
    except Exception as e:
        raise Exception(f'Caught Exception: {e}')

if __name__ == "__main__":
    
    try:
        if (len(sys.argv) > 1):
            parser = argparse.ArgumentParser(description='Process Arguments')
            parser.add_argument('--month', '-m', type=str, help='The month for profit')
            args = parser.parse_args()
            month = args.month
        else:
            month = "03"
            
    except BaseException as e:
        raise BaseException(f'Caught BaseException Exception: {e}')
        
    print("The Profit for Month March is: %s" % main(month))
    
