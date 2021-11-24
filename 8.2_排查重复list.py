def test(l1,l2):
    for x in l1:
        if x in l2:
            print(str(x) + " in List1 and List2")
        else:
            print(str(x) + " only in List1")

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# 方案一：
print("方案一：")
for x in list1:
    if x in list2:
        print(str(x) + " in List1 and List2")
    else:
        print(str(x) + " only in List1")
# 方案二：
print("方案二：")
test(list1,list2)