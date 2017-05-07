import init
import output_puzzle as op
import copy
import moveCase
import puzzle
result=[0,1,2,3,4,5,6,7,8]  #逆序数为0，偶数
while True:
    initial=init.init()
    print("生成的八数码为")
    op.print_Puzzle(initial)
    test=copy.deepcopy(initial)
    test.remove(0)
    value=0
    for i in range(8):
        for j in range(i):
            if test[j]>test[i]:
                value+=1
    if value%2==0:
        break
    else:
        print("八数码无解，继续生成八数码。")
openList=[]
closeList=[]
currentList=copy.deepcopy(initial)
current=puzzle.puzzle()
current.setList(currentList)
current.setG(0)
current.setH(currentList)
current.setParent(-1)
current.getF()
openList.append(current)
while True:
    lists=moveCase.case(current.list)
    for i in lists:
        closeList1=[]
        for a in closeList:
            closeList1.append(a.list)
        if i not in closeList1 :
            p=puzzle.puzzle()
            p.setList(i)
            p.setG(current.g+1)
            p.setH(i)
            p.setParent(current)
            f=p.getF()
            key=0
            for j in openList:
                if j.list==i:
                    if j.getF()<p.getF():
                        key=1
            if key==0:
                openList.append(p)
    closeList.append(current)
    openList.remove(current)
    if (current.list == result):
        break
    sortList = []
    for k in openList:
        sortList.append(k.getF())
    index = sortList.index(min(sortList))
    current=openList[index]
print("-----------步骤如下-----------------")
bean=closeList[-1]
while(True):
   op.print_Puzzle(bean.list)
   print("----------")
   bean=bean.getParent()
   if bean==-1:
       break







