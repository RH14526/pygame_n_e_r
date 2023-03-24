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

    import random
    from typing import List, Tuple


    def generate_wall_location(min_x: int, max_x: int, min_y: int, max_y: int, min_dist: int,
                               existing_walls: List[Tuple[int, int]]) -> Tuple[int, int]:
        while True:
            # Generate a random wall location
            wall_x = random.randint(min_x, max_x)
            wall_y = random.randint(min_y, max_y)

            # Check if the wall overlaps with any existing walls
            overlaps = False
            for loc in existing_walls:
                if abs(wall_x - loc[0]) < min_dist and abs(wall_y - loc[1]) < min_dist:
                    overlaps = True
                    break

            # If the wall doesn't overlap with any existing walls, return its location
            if not overlaps:
                return (wall_x, wall_y)



