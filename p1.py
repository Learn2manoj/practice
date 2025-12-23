def takeinput(input_list):
    i = 0
    while i < 7:
        try:
            # 1. Get the number and store it in a temporary variable
            number = int(input(f"Entermarks of sub {i + 1} : "))
            
            # 2. Append the number to the list passed in
            input_list.append(number)
            
            # 3. Increment the counter
            i += 1
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            # Do not increment i if input is invalid
            
    # 4. Return the fully populated list
    return input_list

result = []
result = takeinput(result)
# Removed the unnecessary and erroneous line: result.append(marks)

print("The numbers you entered are:", result)
result.sort()
print("this the sort list of marks:",result)
print("The maximum number is:", max(result))