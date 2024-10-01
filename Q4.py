...
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
...


total_cost = float(input())
sp_per_banana = float(input())
cp_banana = total_cost / 12
total_sp = sp_per_banana * 12
profit_or_loss = total_sp - total_cost
if profit_or_loss > 0:
    print(f"Profit : Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss : Rs.{-profit_or_loss:.2f}")
else:
    print("No Profit No Loss")
