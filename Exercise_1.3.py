#Make function bubble_sort using bubble sort algorithm to sort numbers given by user; order numbers into the ascending order.

def bubble_sort(numbers):
swapped = True

  
  while swapped:
    
    swapped = False

    
    for i in range(len(numbers) - 1):
      
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
       
        swapped = True

  
  return numbers

  a = []
  number = int(input("Please Enter the Total Number of Elements : "))
  for i in range(number):
    value = int(input("Please enter the % d Element : " % i))
    a.append(value)
  print("The Sorted List in Ascending Order : ", bubble_sort(a))

  a = []
  number = int(input("Please Enter the Total Number of Elements : "))
  for i in range(number):
    value = int(input("Please enter the % d Element : " % i))
    a.append(value)
  print("The Sorted List in Ascending Order : ", bubble_sort(a))
