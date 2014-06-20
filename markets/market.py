import time
import urllib2
import config
import logging
from fiatconverter import FiatConverter


class Market(object):
    def __init__(self, currency):
        self.name = self.__class__.__name__
        self.currency = currency
        self.depth_updated = 0
        self.update_rate = 60
        self.fc = FiatConverter()
        self.fc.update()
        self.converted_depth = {'asks': [{'price': 0, 'amount': 0}], 'bids': [
            {'price': 0, 'amount': 0}]}

    def get_depth(self):
        # note that self.ask_update_depth converts the result to USD
        timediff = time.time() - self.depth_updated
        if timediff > self.update_rate:
            self.ask_update_depth()
        timediff = time.time() - self.depth_updated
        if timediff > config.market_expiration_time:
            logging.warn('Market: %s order book is expired' % self.name)
            self.depth = {'asks': [{'price': 0, 'amount': 0}], 'bids': [
                {'price': 0, 'amount': 0}]}
            self.converted = {'asks': [{'price': 0, 'amount': 0}], 'bids': [
                {'price': 0, 'amount': 0}]}
        return self.depth

    def get_converted_depth (self, currency="USD"):
        self.get_depth()
        self.convert_to_currency(currency)
        return self.converted_depth
    
    def convert_to_usd(self):
        if self.currency == "USD":
            return
        #dont get confused here, direction will take either "asks" or "bids"
        self.converted_depth = self.depth
        for direction in ("asks", "bids"):
            for order in self.converted_depth[direction]:
                order["price"] = self.fc.convert(order["price"], self.currency, "USD")
                
    def convert_to_currency(self, currency="USD"):
        if self.currency == currency:
            return
        #dont get confused here, direction will take either "asks" or "bids"
        self.converted_depth = self.depth
        for direction in ("asks", "bids"):
            for order in self.converted_depth[direction]:
                order["price"] = self.fc.convert(order["price"], self.currency, currency)
                           
    def ask_update_depth(self):
        try:
            self.update_depth()
            #self.convert_to_usd()
            self.depth_updated = time.time()
        
        #update urllib in original code to urllib2
        except (urllib2.HTTPError, urllib2.URLError) as e:
            logging.error("HTTPError, can't update market: %s" % self.name)
        except Exception as e:
            logging.error("Can't update market: %s - %s" % (self.name, str(e)))

    def get_ticker(self):
        depth = self.get_depth()
        res = {'ask': 0, 'bid': 0}
        if len(depth['asks']) > 0 and len(depth["bids"]) > 0:
            res = {'ask': depth['asks'][0],
                   'bid': depth['bids'][0]}
        return res
    
    def get_converted_ticker(self, currency = "USD"):
        depth = self.get_converted_depth(currency)
        res = {'ask': 0, 'bid': 0}
        if len(depth['asks']) > 0 and len(depth["bids"]) > 0:
            res = {'ask': depth['asks'][0],
                   'bid': depth['bids'][0]}
        return res

    ## Abstract methods
    def update_depth(self):
        pass

    def buy(self, price, amount):
        pass

    def sell(self, price, amount):
        pass
