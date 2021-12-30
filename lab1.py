print("WEEKLY CHALLENGES")
print("="*20)
print("         lab1")
income = float(input("Enter the annual income: "))
if income <= 85528:
        tax = (income-556.02)*0.18
else:
        tax = (income-85528)*0.32 + 14839.02
        
tax = round(tax,0)
print("The tax is:", tax)
