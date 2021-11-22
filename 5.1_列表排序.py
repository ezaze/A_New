# 排序、冒泡、插入法详见： https://blog.zeruns.tech/archives/297.html

import copy
l1 = [4,5,7,1,3,9,0]
# l2 = list(set(l1))
l2 = copy.copy(l1)
print(l2)
for ii in range(len(l2)-1):
    # print(ii)
    for iii in range(ii+1 ,len(l2)):
        if l2[ii] > l2[iii]:
            t0 = l2[ii]
            l2[ii] = l2[iii]
            l2[iii] = t0

for i in range(len(l1)):
    print(l1[i],l2[i])



