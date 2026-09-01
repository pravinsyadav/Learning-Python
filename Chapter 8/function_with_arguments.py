def goodday(name):            # 'name' is parameter
    print("good morning " + name)

goodday("pravin")        # 'pravin' is argument  
goodday('sanuu')     


def total_cal(price,quantity):
    a = int(price)
    b = int(quantity)

    total = a * b
    return total

print(total_cal(10,5))
print(total_cal(55,2))