import markets
print "Hello World"

 
access_key="3c0b4ae9-339a-420b-aa22-aaedbb518669"
secret_key="203bd973-f83a-4b0a-8038-388a897a9a74"
 
bc = btcchina.BTCChina(access_key,secret_key)
bc.demo_method()
#result = bc.get_market_depth()
#print result
bc.update_depth()