#LOOPS:Applied concepts loop problems
print("Performing Program76")
#count vowels: count the number of vowels in the string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
input_string = input("Enter String:")
result = count_vowels(input_string)
print(f"Number of vowels: {result}")
print("Performing program77")
#INCREASING+DECREASING:USING A SINGLE RECURSIVE FUNCTION, PRINT NUMBERS IN INCRESING AND THEN DECREASING ORDER
def print_inc_dec(current, limit):
    # Base case: stop when current number exceeds the limit
    if current > limit:
        return
    print(current, end=" ")
    print_inc_dec(current + 1, limit)
    print(current, end=" ")
# Main program
number = int(input("Enter a number: "))
limit = int(input("Enter Limit: "))
if number <= limit:
    print_inc_dec(number, limit)
    print()  # Newline at the end
else:
    print("Starting number must be less than or equal to the limit.")