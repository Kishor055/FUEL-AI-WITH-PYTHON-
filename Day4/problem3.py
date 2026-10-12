#Apply a 10% Discount to prices above 500 in an array using np.where
import numpy as np

# Sample prices array
prices = np.array([100, 450, 500, 600, 750, 1000])

# Apply a 10% discount (multiplying by 0.90) to prices > 500, keeping others unchanged
discounted_prices = np.where(prices > 500, prices * 0.90, prices)

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)