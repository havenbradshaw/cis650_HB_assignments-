def number_to_words(num):
    units = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if not isinstance(num, int) or num < 10 or num > 99:
        return "Error: input must be a two digit number"
    if num < 20:
        return teens[num]

    tens_digit = (num // 10) * 10
    units_digit = num % 10

    if units_digit == 0:
        return tens[tens_digit]
    else:
        return tens[tens_digit] + ' ' + units[units_digit]

print("-- Interface for infinite user inputs using a while loop --")

while True:
    user_input = input("Enter a two digit number (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    if not user_input.isdigit():
        print("Error: input must be a two digit number (10-99)")
        continue
    result = number_to_words(int(user_input))
    print(result)

print("-- Interface for caching numbers --")
seen = {}  # stores number

while True:
    user_input = input("Enter a two digit number (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    if not user_input.isdigit():
        print("Error: input must be a two digit number (10-99)")
        continue

    num = int(user_input)

    if num in seen:
        print(f"{seen[num]} (already asked before)")
    else:
        result = number_to_words(num)
        seen[num] = result
        print(result)