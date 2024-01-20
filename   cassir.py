n=int(input())

list=[1,5,10]

answer = []
i=0

while i*10 <= n:
    j=0
    while i*10+j*5 <= n:
        k = n - (i*10+j*5)
        arr = [i+j+k,[10]*i,[5]*j,[1]*k]
        final_arr = [x for x in arr if x!=[]]
        answer.append(final_arr)
        
        j+=1
    i+=1


print(len(answer))
for sub_arr in answer:
    line = ' '.join(map(str, sub_arr))
    print(line.replace("[","").replace("]","").replace(",",""))

