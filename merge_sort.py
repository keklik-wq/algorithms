def merge_lists(list1,list2):
    i=0
    j=0
    result_list=[]
    while i<len(list1) or j<len(list2):
            if j<len(list2) and i<len(list1):
                if list1[i]<=list2[j]:
                    result_list.append(list1[i])
                    i+=1
                else:
                    result_list.append(list2[j])
                    j+=1
            elif i<len(list1):
                result_list.append(list1[i])
                i+=1
            elif j<len(list2):
                result_list.append(list2[j])
                j+=1
    return result_list

def merge(list):
    if len(list)<2:
        return list
    else:
        half = len(list)//2
        left = merge(list[:half])
        right = merge(list[half:])
        return merge_lists(left,right)

n = int(input())
list = list(map(int,input().split()))

print(*merge(list))
