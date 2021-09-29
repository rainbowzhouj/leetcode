from typing import List


def a(list:List[int])->int:
    for i in range(len(list)-1,0,-1):
        if list[i]==list[i-1]:
            del list[i]
    return len(list)

if __name__=='__main__':
    aa=[1,2,2,3]
    print(a(aa))
