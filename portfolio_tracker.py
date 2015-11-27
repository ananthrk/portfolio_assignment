from yahoo_finance import Share
import re

class folio(object): 

    def __init__(self):
        self.open_portfolio = open('portfolio.txt', 'r')
        self.result = []
        self.li = []
    
    def get_portfolio_data(self):
        lineCount=0; 
        for line in self.open_portfolio:
            lineCount = lineCount+1
            self.li.append(line)
        #print self.li
        return self.li

    def get_stock_symbol_count_and_stock_value(self):
        #print 'Str: ', self.get_portfolio_data()
        for s in self.get_portfolio_data():
            #print s 
            self.matchObj = re.findall( r'\([a-zA-Z]+\s*,\s*[0-9]*\s*\)', s )
            totalcount = 0
            for tag in self.matchObj:
                stockSymbol = re.search( r'[a-zA-Z]+', tag)
                stockCount = re.search( r'[0-9]+', tag)            
                stock_price = Share(stockSymbol.group(0))                
                stock_value = stock_price.get_price() 
                if stock_value:
                    totalcount+=(float(stock_value)*float(stockCount.group(0)))
            self.result.append((s ,totalcount))
        return self.result
      
    def sort_portfolio_in_descending_order(self):
        self.sort_dec = sorted(self.get_stock_symbol_count_and_stock_value(), key=lambda t1: t1[1],reverse=True)
        for sortValue in self.sort_dec:
            print sortValue        


this = folio()
this.sort_portfolio_in_descending_order()







