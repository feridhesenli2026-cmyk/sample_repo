# Given list of dictionaries
people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

print("Names of people older than 25:")
for person in people:
    if person['age'] > 25:
        print(person['name'])

sorted_people = sorted(people, key=lambda x: x['age'], reverse=True)

print("\nSorted by age (descending):")
print(sorted_people)
 



 # Input range
start = 10
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # Sadə ədədlər 1-dən böyük olur
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
