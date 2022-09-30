print("Welcome to the tip Calculator")
total_bill=float(input("What was the Total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people=int(input("How many people would you like to split the bill?"))
bill_with_tip=tip/100*total_bill+total_bill
split_bill = round((bill_with_tip/people),2)
print(f"total amount of bill you have to pay {split_bill}")


