# bubble sort
def bubble_sort(num):
    size=len(num)
    for i in range(size-1):
        for j in range(size-1):
            if num[j]> num[j + 1]:
                num[j], num[j + 1]= num[j + 1], num[j]
    return num


if __name__ == "__main__":
    numbers = [38, 9, 23, 34, 5, 11]
    print(bubble_sort(numbers))

