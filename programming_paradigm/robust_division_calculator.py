def safe_divide(numerator, denominator):
  
  try:
    numerator = input("float(numerator)")
    denominator = input("float(denominator)")
    result = numerator/denominator 
  
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

  except ValueError:
    print("Error: Please enter numeric values only.")

  else
    print(f"The result of the division is {result.:1}")

  
  
