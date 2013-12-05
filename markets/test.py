#!/usr/bin/python
# -*- coding: utf-8 -*-
#API Access Key : 3c0b4ae9-339a-420b-aa22-aaedbb518669
#API Secret Key : 203bd973-f83a-4b0a-8038-388a897a9a74 
import btcchina
import cavirtex
access_key="3c0b4ae9-339a-420b-aa22-aaedbb518669"
secret_key="203bd973-f83a-4b0a-8038-388a897a9a74"
 
china = btcchina.BTCChina(access_key,secret_key)
china.demo_method()
#result = bc.get_market_depth()
#print result
#china.update_depth()

canada = cavirtex.Cavirtex()
#canada.update_depth()
#print (canada.get_depth())
#print (china.get_depth())
print (canada.get_converted_depth("USD"))

#########These methods have no arguments
#result = bc.get_account_info()
#print result
#result = bc.get_market_depth()
#print result
 
# NOTE: for all methods shown here, the transaction ID could be set by doing
#result = bc.get_account_info(post_data={'id':'stuff'})
#print result
 
#########buy and sell require price (CNY, 5 decimals) and amount (BTC, 8 decimals)
#result = bc.buy(500,1)
#print result
#result = bc.sell(500,1)
#print result
 
#########cancel requires id number of order
#result = bc.cancel(2)
#print result
 
#########request withdrawal requires currency and amount
#result = bc.request_withdrawal('BTC',0.1)
#print result
 
#########get deposits requires currency. the optional "pending" defaults to true
#result = bc.get_deposits('BTC',pending=True)
#print result
 
#########get orders returns status for one order if ID is specified
#########otherwise returns all orders, the optional "open_only" defaults to true '''
#result = bc.get_orders(2)
#print result
#result = bc.get_orders(open_only=True)
#print result
 
''' get withdrawals returns status for one transaction if ID is specified,
    if currency is specified it returns all transactions,
    the optional "pending" defaults to true '''
#result = bc.get_withdrawals(2)
#print result
#result = bc.get_withdrawals('BTC',pending=True)
#print result