# Car Cost

def car_listing(car_prices):
  result = ""
  for name,cost in car_prices.items():
    result += "{} costs {} dollars".format(name,cost) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))