def safe_divide(numerator, denominator):
  
  try:
    numerator = input("float(numinator)")
    denominator = input("float(denominator)")
    result = numerator/denominator 
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError:
    print("Error: Please enter numeric values only")
  else 
  print("The result of the division is" result)
