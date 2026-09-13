value = 0
output = 0

while True:
    try:
        pos_int = int(input("Input a positive integer: "))
        if pos_int > 0:
            while output < 100:
                print(value * pos_int)
                value += 1
                output = value * pos_int
            break
        else:
          print("That is not positive.")
    except ValueError:
       print("Please enter an integer.")

    