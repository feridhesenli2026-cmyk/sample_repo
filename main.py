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
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)






text = "Hello world! Hello everyone. Welcome to the world of Python."

text = text.lower()

text = text.replace("!", "")
text = text.replace(".", "")
text = text.replace(",", "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)



numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]

print(squares)




words = ["apple", "banana", "pear", "grape"]

sorted_words = sorted(words, key=len)

print(sorted_words)
