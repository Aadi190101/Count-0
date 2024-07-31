count = 0


def countzero(num):
    global count
    num = abs(num)
    if num == 0:
        return 1
    if num > 0:
        if num % 10 == 0:
            count += 1
        countzero(num // 10)
    return count


n = int(input("Enter an integer :"))
print("The number of Zeros in the Given number is:", countzero(n))
