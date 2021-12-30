print("WELCOME TO THE LOVE CALCULATOR!")
print("="*20)
name1 = input("Your name?\n")
name2 = input("Your partner name?\n")
print("="*20)
combined_names = name1 + name2
lower_case_name = combined_names.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
digit1 = t + r + u + e
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
digit2 = l + o + v + e
score = int(str(digit1) + str(digit2))
print(f"{score}")
if score <= 10 or score >= 90:
  print(f"\nYour Love Score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"\nYour Love Score is {score}, you are alright together.")
else:
  print(f"\nYour Love Score is {score}.")
  print("="*20)
  
  print("      THANK YOU")