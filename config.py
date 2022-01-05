live_trade = False

coin = ["BTC"]
quantity = [0.001]
leverage = [100]
take_profit_percentage = 150

pair = []
for i in range(len(coin)):
    pair.append(coin[i] + "USDT")
