import math

num_people = int(input("Enter the number of people attending the cookout: "))
num_hotdogs_per_person = int(input("Enter the number of hot dogs per person: "))

total_hotdogs_needed = num_people * num_hotdogs_per_person

num_hotdog_packages_needed = math.ceil(total_hotdogs_needed / 10)
num_hotdog_bun_packages_needed = math.ceil(total_hotdogs_needed / 8)

hotdogs_leftover = (num_hotdog_packages_needed * 10) - total_hotdogs_needed
buns_leftover = (num_hotdog_bun_packages_needed * 8) - total_hotdogs_needed

print("Minimum number of hot dog packages needed: ", num_hotdog_packages_needed)
print("Minimum number of hot dog bun packages needed: ", num_hotdog_bun_packages_needed)
print("Number of hot dogs left over: ", hotdogs_leftover)
print("Number of hot dog buns left over: ", buns_leftover)
