daily_sales = [23, 12, 45, 67, 54, 56, 77, 55]

total_cups = sum(sale for sale in daily_sales if sale > 40)

print(total_cups)