names = []

for i in range(5):
  names.append(input("Enter 5 names:"))

print(names)


choice = input('Would you like to remove someone?')

if choice == "yes" or choice == 'y':
  rname = input("Enter the name youd like to remove:")
  names.remove(rname)
else:
  print("Have a Great DaY!")
  
print(names)

