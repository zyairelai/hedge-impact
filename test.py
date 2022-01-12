import api_binance

pair = "BTCUSDT"
position_size = 0.001
response = api_binance.position_information(pair)
# print(response[0])

print(response[1])
if float(response[1].get('positionAmt')) > 0:
    long  = float(response[1].get('unRealizedProfit')) / (float(response[1].get('entryPrice')) * abs(float(response[1].get('positionAmt'))) / int(response[1].get('leverage'))) * 100
    price_difference = (float(response[1].get('markPrice')) - float(response[1].get('entryPrice'))) / float(response[1].get('entryPrice')) * int(response[1].get('leverage')) * 100
    print("Long Percentage  : " + str(long))
    print("Price Difference : " + str(price_difference))

print()
print(response[2])
if float(response[2].get('positionAmt')) != 0:
    short = float(response[2].get('unRealizedProfit')) / (float(response[2].get('entryPrice')) * abs(float(response[2].get('positionAmt'))) / int(response[2].get('leverage'))) * 100
    price_difference = -((float(response[2].get('markPrice')) - float(response[2].get('entryPrice')) )/ float(response[2].get('entryPrice')) * int(response[2].get('leverage'))) * 100
    print("Short Percentage : " + str(short))
    print("Price Difference : " + str(price_difference))
