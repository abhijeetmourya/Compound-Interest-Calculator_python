
def  compound_intrest(p, r, t):
    ci = p * (pow((1 + r / 100), t))

    print("Principle: ", p)
    print("Interest rate: ", r)
    print("Time in years: ", t)
    print("compound Interest: ", ci)




principal = float(input("Enter the principle amount : "))
rate = float(input("Enter the rate of interest : "))
time = float(input("Enter the time in the years: "))
compound_intrest(principal, rate, time)



