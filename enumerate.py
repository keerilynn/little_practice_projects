groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

index = 1
for index, item in enumerate(groceries, 1):
   print(f'{index}. {item}')

# enumerate is more effective than looping to create an indexed list