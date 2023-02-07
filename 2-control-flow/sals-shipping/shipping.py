weight = 41.5
#ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight >6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

print(cost_ground)
cost_premium = 125.00
print(cost_premium)

#drone shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <=6:
  cost_drone = weight * 9.0
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.0
elif weight > 10:
  cost_drone = weight * 12.25

print(cost_drone)
