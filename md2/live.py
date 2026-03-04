# Hour to Minute Converter Program

def hour_to_minute(hours):
    return hours * 60


def main():
    print("=== check it ===")
    
    try:
        hours = float(input("Enter time in hours: "))
        minutes = hour_to_minute(hours)
        print(f"{hours} hour(s) = {minutes} minute(s)")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()