import random
# Generate a random wall location

wall_x = random.randint(min_x, max_x)
wall_y = random.randint(min_y, max_y)

# Check if the wall is on the road
if wall_y >= 400:
    wall_y = wall_y - 100

# Generate a random coin location
coin_x = random.randint(min_x, max_x)
coin_y = random.randint(min_y, max_y)

# Check if the coin is on the road
if coin_y >= 400:
    coin_y = coin_y - 100
