
def Gonggong(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    else:
        return Gonggong(x - 1) + Gonggong(x - 2)

if __name__ == '__main__':
        print(Gonggong(7))