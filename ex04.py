#logic operator

# print(1 > 2)
# print(1 < 2)
# print(1 <= 2)
# print(1 >= 2)
# print(2 >= 2)
# print(2 <= 2)
# print(2 == 2)
# print(2 == 2)
# print(2 == 3)
# print(2 == 2)
# print(2 == "2")
# print(2 != "2")
# print(2 != 2)

age = 55
user_active = True
message =""" 
------------------------------- 
Welcome City Movie Theater 
Movie : Gladiator II
--------------------------------
"""
print(message)
if age > 54:
  print(f"Age :{age}\nR-rated movie tickets are now available for purchase + 20% discount." )
elif age > 17:
  print(f"Age :{age}\nR-rated movie tickets are now available for purchase.")
else:
  print(f"Age :{age}\nSorry, you don't meet the age requirement to watch this movie!")

#----------Termary---------------#
message = "\nUser Status : Active " if user_active else "User No Active"
print(message)
