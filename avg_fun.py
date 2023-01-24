
def average(sum):
    avg = sum/2
    return avg


a = int(input("How many number to search:"))
sum = 0
print("Enter the number:")
for i in range(a):
    b = int(input())
    sum += b

Avg = average(sum)

print("Enter the average of following number:",Avg)