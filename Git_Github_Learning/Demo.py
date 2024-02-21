from os import environ 
print("ENV Variable Name is : ",environ['Name'])
print("Hello world")
print("writing This Code in Windows GitBash and Later Merging with Master")

#Program for priting Even numbers from  given range.
def Print_Even(Range):
    try:
        num = 0
        for i in range(num,Range,2):
            if i ==0:
                pass
            else:
                print(f"Number : {i}")
    except Exception as e:
        print("Error : ",e)
Print_Even(50)
for i in environ['PATH']:
    if i ==":":
        print()
    else:
        print(i,end="")
print()
