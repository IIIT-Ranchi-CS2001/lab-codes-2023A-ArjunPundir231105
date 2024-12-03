#Program 1,2
def my_zip(a,b,c):
    return list(zip(a,b,c))

def my_sort(arr, key):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if (arr[j][key]) > (arr[j+1][key]):
                arr[j], arr[j+1]  = arr[j+1], arr[j]
                swapped = True
                if (swapped == False):
                    break
customer_name =  [x for x in input().split()]
customer_id =  [(int)(x) for x in input().split()]
shop_pts = [(int)(x) for x in input().split()]

ans =  my_zip(customer_name,customer_id,shop_pts)

print("Original list")
print(ans)
print("Sorted List with key 0:-")
my_sort(ans,0)
print(ans)
print("Sorted List with key 1:-")
my_sort(ans,1)
print(ans)
print("Sorted List with key 2:-")
my_sort(ans,2) 
print(ans)