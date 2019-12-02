
def get_max_profit(stockprice):
    maxProfit=-1000000000
    maxTime= 0
    minTime = 0


    if((stockprice.index(min(stockprice)) - stockprice.index(max(stockprice)))<0):

        for i, x in enumerate(stockprice):
            print("outer loop ", i)
            for j, y in enumerate(stockprice[i+1:]):
                print("inner loop ", j)
                if (y-x > maxProfit):
                    minTime = i
                    maxTime = i + j + 1
                    maxProfit = y-x


    else:
        maxProfit = max(stockprice) -min (stockprice)
        minTime = stockprice.index(min(stockprice))
        maxTime =stockprice.index(max(stockprice))
        # print(stockprice.index(max(stockprice)), " ", stockprice.index(min(stockprice))


    return maxProfit, maxTime, minTime


# def get_max_profit(stock_prices):
#     current_price = stock_prices[0]

#     minPrice = current_price

#     maxProfit = 0

#     for price in stock_prices:
#         if stock_prices.index(price) <  0:
#             pass
#         else:
#             #see what our profit would be if we bought
#             #at the min price and sold at the current price
#             potential_profit = price - minPrice

#             #update max profit if we can do better
#             maxProfit = max(maxProfit, potential_profit)

#         #Ensure min price is the lowest price we've seen so far

#         minPrice = min(minPrice, price)


#     return maxProfit



def main():
    stock_prices = [10, 7, 5, 8, 11, 9]
    [maxProfit, maxTime, minTime] = get_max_profit(stock_prices)

    print(maxProfit, minTime, maxTime)


if __name__ == "__main__":
    main()