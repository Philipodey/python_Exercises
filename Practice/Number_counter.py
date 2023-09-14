sample_number = [1, 2, 3, 4, 5, 6, 7,8, 9]
# even_number = sample_number % 2 == 0
# odd_number = sample_number % 2 == 1
odd = 0
even = 0
count = 1
for count in sample_number:
    if count % 2 == 0:
        even += 1
    else:
        odd += 1
    count += 1
print("The odd number is {}".format(odd))
print("The even number is {}".format(even))
