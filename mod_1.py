print("This is mod_1's name -->", __name__) ##file name

def amazing_sum(num1,num2):
    return (int(num1)+ int(num2))


def demo_amazing_sum():
    print('Welcome to the amazing sum demo!')
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    print(amazing_sum(num1,num2))



if __name__ == '__main__':
    demo_amazing_sum()
   # print("We are running this file directly")

else:
    print("THis file was called / imported from somewhere")