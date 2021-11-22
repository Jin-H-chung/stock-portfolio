
class portfolio:
    def __init__(self):
        self._stocks = []   #store in the list. what is public and private??

    def buy(self, name, shares, price):
        self._stocks.append((name, shares, price)) #tuple

    def cost(self): # multiplay shares and price. loop over and that sharesxprice and add 
        return sum(shares * price for _, shares, price in self._stocks)  #_ means I dont care anything locted here. I can use name here, but I dont need it for calculation. anyway I need to unpack tuple so I need 3 elements either _ or name

