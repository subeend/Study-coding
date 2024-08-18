def solution(arr, queries):
    arr_list=[]
    for s,e,k in queries:
        tmp = sorted(arr[s:e+1])
        res = next((x for x in tmp if x > k), -1)
        arr_list.append(res)

    return arr_list