
def sumOfCubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum

n = int(input("Please enter the input number"))
print("The sum of cubes for the given number is:"+" "+str(sumOfCubes(n)))


import threading


def sumOfCubesByThreading(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    print(sum)

if __name__ == "__main__":
    threads=[]
    for items in range(1,n+1):
        temp_thread = threading.Thread(target=sumOfCubesByThreading,args=(items,))
        threads.append(temp_thread)
        temp_thread.start()
    n =int(input("Please enter the input number"))




