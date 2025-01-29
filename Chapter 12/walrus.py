# WALRUS OPERATOR ->it is used for assignment expressions, meaning it allows you to assign a value to a variable as part of an expression.
value = input("Enter something: ")
if len(value) > 5:
    print("Input is longer than 5 characters!")
#here value is assigned first and then the length is checked


if (value := input("Enter something: ")).strip():
    print(f"You entered: {value}")
# value gets assigned inside the condition.
