
from coinbase.wallet.model import APIObject
from coinbase.wallet.client import Client
import time
import json
api_key = 'XXXXXXXX'
api_secret = 'XXXXXXXXXXX'
client = Client(api_key, api_secret)

account = client.get_primary_account()
print(account.native_balance.amount)
# payment_method = client.get_payment_methods()[0]

#(json.dumps(public_client.get_product_historic_rates('BTC-USD', granularity=3600)))

IsNextOperationBuy = True

#buy
UPWARD_TREND_THRESHOLD = 0.01
DIP_THRESHOLD = -0.02

#sell
PROFIT_THRESHOLD = 0.01
STOP_LOSS_THRESHOLD = -0.02



usd = 1000
btc = 0.5
num = 6

def getMarketPrice():
    return float(client.get_buy_price(currency_pair ='BTC-USD').amount)


lastOpPrice = getMarketPrice()

print getMarketPrice()

def AttemptToTrade():
    currentPrice = getMarketPrice()
    percentageDifference = ((currentPrice - lastOpPrice)*100)/lastOpPrice
    print("percentage difference = " +str(percentageDifference))
    if IsNextOperationBuy:
        tryToBuy(percentageDifference)
    else:
        tryToSell(percentageDifference)

def BuyLogAction(percentageDifference, usd, btc):
    print("bought at " + str(getMarketPrice()) + "USD")
    print("current usd -100")
    print("current usd: " + str(usd))
    print("current btc + " + str(100/getMarketPrice()))
    print("current btc: " + str(btc))
    print("")

def SellLogAction(percentageDifference, usd, btc):
    print("sold at " + str(getMarketPrice()) + "USD")
    print("current usd + " + str(getMarketPrice()/100))
    print("current usd " + str(usd))
    print("current btc -0.01")
    print("current btc " + str(btc))
    print("")




def tryToBuy(percentageDifference):
    if percentageDifference >= UPWARD_TREND_THRESHOLD or percentageDifference <= DIP_THRESHOLD:
        global usd
        usd = usd - 100
        global btc
        btc = btc + 100/getMarketPrice()
        # account.sell(amount='1', currency="BTC", payment_method = payment_method.id)

        BuyLogAction(percentageDifference, usd, btc)
        global IsNextOperationBuy
        IsNextOperationBuy = False
    else:
        print("No buy or sell")
        print("")

def tryToSell(percentageDifference):
    if percentageDifference >= PROFIT_THRESHOLD or percentageDifference <= STOP_LOSS_THRESHOLD:
        global usd
        usd = usd + getMarketPrice()/100
        global btc
        btc = btc - 0.01
        # account.buy(amount = '1', currency = "BTC", payment_method = payment_method.id)
        SellLogAction(percentageDifference, usd, btc)
        global IsNextOperationBuy
        IsNextOperationBuy = True
    else:
        print("No buy or sell")
        print("")

print(getMarketPrice())
initialamount = 1000 + 0.5*getMarketPrice()
print("total amount: " + str(initialamount))
print("")

def Trade():
    while num > 0:
        time.sleep(2)  # sleep for 1 second
        print(getMarketPrice())
        AttemptToTrade()
        num = num - 1
        if num == 0:
            print(usd)
            print(btc)
            finalamount = usd + btc*getMarketPrice()
            print("total amount: " + str(finalamount))
            print("profit: " + str(finalamount - initialamount))
