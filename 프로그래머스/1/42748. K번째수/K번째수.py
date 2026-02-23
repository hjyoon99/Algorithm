def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k - 1])
    return answer