import config
import api_binance
from pytz import utc
from datetime import datetime
from termcolor import colored
from apscheduler.schedulers.blocking import BlockingScheduler

def lets_make_some_money():
    for i in range(len(config.pair)):
        pair = config.pair[i]
        leverage = config.leverage[i]
        quantity = config.quantity[i]

        print(pair)
        response = api_binance.position_information(pair)

        if api_binance.LONG_SIDE(response) == "NO_POSITION" and api_binance.SHORT_SIDE(response) == "NO_POSITION":
            # if response[0].get('marginType') != "isolated": api_binance.change_margin_to_ISOLATED(pair)
            if response[0].get('marginType') != "cross": api_binance.change_margin_to_CROSSED(pair)
            if int(response[0].get("leverage")) != leverage: api_binance.change_leverage(pair, leverage)
            api_binance.market_hedge_open(pair, quantity)

        if api_binance.LONG_SIDE(response) == "LONGING":
            unrealizedPnL = float(response[1].get('unRealizedProfit')) / (float(response[1].get('entryPrice')) * abs(float(response[1].get('positionAmt'))) / int(response[2].get('leverage'))) * 100
            if unrealizedPnL < -85 or unrealizedPnL > config.take_profit_percentage: api_binance.market_close_long(pair, response)
            else: print(colored("_LONG_SIDE : HOLDING_LONG", "green"))

        if api_binance.LONG_SIDE(response)  == "LONGING"  and api_binance.SHORT_SIDE(response) == "NO_POSITION" : print("SHORT_SIDE : 🐺 WAIT 🐺")
        if api_binance.SHORT_SIDE(response) == "SHORTING" and api_binance.LONG_SIDE(response)  == "NO_POSITION" : print("_LONG_SIDE : 🐺 WAIT 🐺")

        if api_binance.SHORT_SIDE(response) == "SHORTING":
            unrealizedPnL = float(response[2].get('unRealizedProfit')) / (float(response[2].get('entryPrice')) * abs(float(response[2].get('positionAmt'))) / int(response[2].get('leverage'))) * 100
            if unrealizedPnL < -85 or unrealizedPnL > config.take_profit_percentage: api_binance.market_close_short(pair, response)
            else: print(colored("SHORT_SIDE : HOLDING_SHORT", "red"))

        print("Last action executed @ " + datetime.now().strftime("%H:%M:%S") + "\n")
    
print(colored("LIVE TRADE IS ENABLED\n", "green")) if config.live_trade else print(colored("THIS IS A SHOWCASE\n", "red")) 

scheduler = BlockingScheduler()
scheduler.add_job(lets_make_some_money, 'cron', second='0', timezone=utc)
scheduler.start()
