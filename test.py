#부분집합의 합
def promising(i, weight, total):
    return (weight+total>=W) and (weight==W or weight+w[i+1]<=W)

def s_s(i, weight, total, include):
    #sum of subsets 구현
    if promising(i,weight,total):
        if weight==W:
            for k in range(n):
                print(include[k], end=" ")
            print()
        else:
            if i+1<n:
                include[i+1]=1
                s_s(i+1, weight+w[i+1], total-w[i+1], include)
                include[i+1]=0
                s_s(i+1, weight, total-w[i+1], include)

n=4
w=[1,2,4,6]
W=6
print("items =",w, "W= ", W)
include =n*[0]
total=0
for k in w:
    total+=k
s_s(-1,0,total,include)



#graph coloring
def color(i, vcolor):
    if promising(i, vcolor):
        if i == n - 1: 
            for k in range(n):
                print(vcolor[k], end=" ")
            print()
        else:
            for col in range(1, m+1):  
                vcolor[i + 1] = col
                color(i + 1, vcolor)

def promising(i, vcolor):
    for j in range(i): 
        if W[i][j] and vcolor[i] == vcolor[j]:  
            return False
    return True

n = 4
W = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vcolor = [0] * n  
m = 3  
print("\n\n")
print("result of graph coloring")
color(-1, vcolor)
