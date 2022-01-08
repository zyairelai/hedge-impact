live_trade = True

coin = ["BTC", "ETH"]
quantity = [0.001, 0.01]
leverage = [75, 60]
take_profit_percentage = 300

pair = []
for i in range(len(coin)):
    pair.append(coin[i] + "USDT")
