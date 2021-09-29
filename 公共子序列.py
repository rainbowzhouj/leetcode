# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def Gonggong(x):
    if x<=0 :
        return 0
    if x==1:
        return 1
    if x==2:
        return 2
    else:
        return Gonggong(x-1)+Gonggong(x-2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(Gonggong(7))



