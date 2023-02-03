# Q1 Answer template

def solution(lottos, win_nums):
    answer=[]
    count_max=0
    count_min=0
    for i in range(6):
        if lottos[i] in win_nums:
            
            count_max+=1
            count_min+=1
        elif lottos[i]==0:
            count_max+=1
            count_min+=0
    if count_max==0:
        count_max=1
    if count_min==0:
        count_min=1
        
    answer=[7-count_max,7-count_min]
            
             
    return answer

lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]
answer = solution(lottos, win_nums)
print(answer)