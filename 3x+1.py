from colorama import Style,Fore
import matplotlib.pyplot as plt


print(Style.BRIGHT+"Welcome To The Collatz Conjecture Simulator")
print()
print("--Rules--")
print()
print("EVEN- Divide By 2")
print("ODD- Multiply By 3 And Add One")
print()

numbers = []
xAxis=[]

while True:
    startNum = int(input("Enter Start Number:"))
    num = startNum
    turns = 0
    numbers = [startNum]
    print("----------------------------------------")

    while num != 2:
        if num % 2 == 0:
            num = int(num/2)
            numbers.append(num)
            print(Fore.RED+str(num)+" - ↓")
            turns+=1
        else:
            num = int((num*3)+1)
            numbers.append(num)
            print(Fore.GREEN+str(num)+" - ↑")
            turns+=1
    print(Fore.RED+str("1")+" - ↓")
    turns+=1
    numbers.append(1)

    print(Fore.RESET+"-----------------------------------------------")
    print(str(startNum)+" Took "+str(turns)+" Goes To Return To 1")

    for i in range(len(numbers)):
        xAxis.append(i)
    


    plt.plot(xAxis, numbers, color='green', linestyle='dashed', linewidth = 1.2,
         markerfacecolor='blue', markersize=12)
  
    plt.xlabel('Number Of Goes')

    plt.ylabel('Number')
  

    plt.title('3X+1 Graph for '+ str(startNum))
    plt.show()
    print()

    

  

