# bubble sort
def bubble_sort(num):
    size=len(num)
    for i in range(size-1):
        for j in range(size-1):
            if num[j]["transaction_amount"]>num[j+1]["transaction_amount"]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
    return num

if __name__ == "__main__":
    elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    print(bubble_sort(elements),end="")