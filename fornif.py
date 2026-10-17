
total = 0

for day in range(1, 6):
    minutes = int(input(f"Minutes studied on day {day}: "))
    total = total + minutes

print(f"You studied for {total} minutes in total.")

if total >= 600:
    print("Week goal achieved!")
else:
    print("Keep practising!")