myName = "Haven"

while True:
    name = input("Enter your name: ")

    if not name:
        print("This is not a valid name.")
        continue
    else:
        if name == myName:
            try:
                age = float(input("Enter your age: "))
            except ValueError:
                    print("This is not a valid age.")
                    continue
            else:
                if age <= 0:
                    print("You are not born yet.")
                elif age < 18:
                    print("You are a minor.")
                elif age <= 99:                        
                    print("Adult.")
                elif age > 99:
                    print("Nice to meet you.")
            break
        print("Your name is not my name, program ended.")
            
        break
