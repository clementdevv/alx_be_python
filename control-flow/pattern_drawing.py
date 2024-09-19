while True:
  size = int(input("Enter the size of the pattern: "))
  if size > 0:
    break 
  else:
    print("Please enter a positive integer.")

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")  # Print asterisk without newline
    print("\n")  
    row += 1 
