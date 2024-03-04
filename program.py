airport = {}

print("\nAirport Database")
print("1. Add a new airport")
print("2. Fetch airport information")
print("3. Quit")

c = input("Enter your choice (1/2/3): ")

while c != '3':
    if c == '1':
        ic = input("Enter the ICAO code of the airport: ")
        nm = input("Enter the name of the airport: ")
        airport[ic] = nm
        print(f"Airport {ic} - {nm} added successfully.")
    elif c == '2':
        ic = input("Enter the ICAO code of the airport to fetch information: ")
        print(f"The name of the airport with ICAO code {ic} is {airport.get(ic, 'not found')}.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    c = input("Enter your choice (1/2/3): ")

print("Exiting program.")
