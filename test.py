import api_binance

pair = "BTCUSDT"
position_size = 0.001
response = api_binance.position_information(pair)
for each in response: print(each)

long  = float(response[1].get('unRealizedProfit')) / (float(response[1].get('entryPrice')) * abs(float(response[1].get('positionAmt'))) / int(response[2].get('leverage'))) * 100
short = float(response[2].get('unRealizedProfit')) / (float(response[2].get('entryPrice')) * abs(float(response[2].get('positionAmt'))) / int(response[2].get('leverage'))) * 100
print(long)
print(short)
