from typing import List


def a(list:List[int])->int:
    for i in range(len(list)-1,0,-1):
        if list[i]==list[i-1]:
            del list[i]
    return len(list)

if __name__=='__main__':
    aa=[0,0,1,1,1,2,2,3,3,4]
    print(a(aa))
