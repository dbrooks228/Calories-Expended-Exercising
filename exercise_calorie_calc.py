import argparse

def calculate_calories_burned(weight, distance):
    """Calculate the total calories burned based on user weight and distance walked or run."""
    calories_burned_per_mile = 0.75 * weight
    total_calories_burned = calories_burned_per_mile * distance
    return total_calories_burned

def main():
    parser = argparse.ArgumentParser(description="Calculate the calories burned based on weight and walking/running distance.")
    parser.add_argument("weight", type=float, help="User's weight in pounds.")
    parser.add_argument("distance", type=float, help="Distance walked or run in miles.")
    
    args = parser.parse_args()
    
    total_calories = calculate_calories_burned(args.weight, args.distance)
    print(f"Total calories burned: {total_calories:.2f}")

if __name__ == "__main__":
    main()
