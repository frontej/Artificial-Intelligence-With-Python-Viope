#Make simple Supermarket -program,

#having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
#asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
#asking products until user gives '0' to quit the program (while-loop).
#printing  "Total:" and the total sum of prices.
#asking "Payment:" from user and printing "Change:" and finally  calculating and printing the amount of change (payment - totalsum) to customer.
#You must use in this program: while, input.

print("""Supermarket
===========""")

prices = [10,14,22,33,44,13,22,55,66,77]
totalsum = []

while True:
        selection = int(input("Please select product (1-10) 0 to Quit:"))
        if selection == 0:
            print("Total: ", sum(totalsum))
            payment = int(input("Payment: "))
            var1 = payment - sum(totalsum)
            print("Change: ", var1)
            break
            
        elif selection == 1: 
            print("Product: ", selection, " Price:", prices[0])
            totalsum.append(prices[0])
            
        
        elif selection == 2: 
            print("Product: ", selection, " Price:", prices[1])
            totalsum.append(prices[1])
            
            
        elif selection == 3: 
            print("Product: ", selection, " Price:", prices[2])
            totalsum.append(prices[2])
            
        elif selection == 4: 
            print("Product: ", selection, " Price:", prices[3])
            totalsum.append(prices[3])
            
        elif selection == 5: 
            print("Product: ", selection, " Price:", prices[4])
            totalsum.append(prices[4])
            
        elif selection == 6: 
            print("Product: ", selection, " Price:", prices[5])
            totalsum.append(prices[5])
            
        elif selection == 7: 
            print("Product: ", selection, " Price:", prices[6])
            totalsum.append(prices[6])
            
        elif selection == 8: 
            print("Product: ", selection, " Price:", prices[7])
            totalsum.append(prices[7])
            
        elif selection == 9: 
            print("Product: ", selection, " Price:", prices[8])
            totalsum.append(prices[8])
            
        elif selection == 10: 
            print("Product: ", selection, " Price:", prices[9])
            totalsum.append(prices[9])
