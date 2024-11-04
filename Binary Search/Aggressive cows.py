'''
    Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. 
    The stalls are located along a straight line at positions x1 ... xN (0 <= xi <= 1,000,000,000).
    His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other 
    once put into a stall. To prevent the cows from hurting each other, he wants to assign the cows 
    to the stalls, such that the minimum distance between any two of them is as large as possible. 
    What is the largest minimum distance?
    (GFG)
'''
def can_we_place(stalls, cows, distance) -> bool:
    count_of_cows = 1
    last_cow = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_cow >= distance:
            count_of_cows += 1
            last_cow = stalls[i]
    print(count_of_cows)
    return True if count_of_cows >= cows else False

def solution(stalls, cows):
    stalls.sort()
    low, high = 1, stalls[len(stalls)-1] - stalls[0] 
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if can_we_place(stalls, cows, mid):
            
            ans = mid
            print(ans)
            low = mid + 1
        else:
            high = mid - 1

    return ans

if __name__ == "__main__":
    stalls = [1, 2, 8, 4, 9]
    cows = 3
    # expected op = 3
    print(solution(stalls, cows))