a=5
b=2



try:
    print("resource Open")
    print(a/b)

    k = int(input("enter rthe number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide",e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
       print("resource closed")