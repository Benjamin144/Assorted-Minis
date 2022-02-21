# print("Welcome to the tip calculator!")

# total_bill = input ("What was the total bill? £")
# total_bill_as_float = float(total_bill)
# percentage_tip = input("What percentage tip would you like to give 10, 12, or 15? ")
# percentage_tip_as_int = int(percentage_tip)
# split_bill = input("How many people to split the bill? ")
# split_bill_as_int = int(split_bill)

# payable = percentage_tip_as_int / 100 * total_bill_as_float / split_bill_as_int + total_bill_as_float
# final_bill = payable / split_bill_as_int
# message = (f"Each person should pay: £{final_bill:.2f}")
# print(message)


print("Welcome to the tip calculator!")
initial_bill = float(input("What was the total bill? £"))
the_tip = int(input("What percentage tip would you like to give 10, 12, or 15?, (only use numbers not percentages!)")) 
split_bill = int(input("How many people would you like to split the bill? "))
percentage_tip = the_tip / 100 
total_tip = initial_bill * percentage_tip
total_bill = initial_bill + total_tip
persons_payable = total_bill / split_bill 
final_payable = round(persons_payable, 2)
final_payable = "{:.2f}".format(persons_payable)
message = (f"Each person should pay: £{final_payable:}")
print(message)