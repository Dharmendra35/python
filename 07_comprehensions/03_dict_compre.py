tea_price_inr = {
  "Masala Chai" : 40,
  "Green Tea" : 50,
  "Lemon Tea" : 29
}

tea_price_usd = {tea : price / 80 for tea, price in tea_price_inr.items()}
print(tea_price_inr)