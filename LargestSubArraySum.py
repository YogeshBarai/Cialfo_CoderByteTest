
def MaxSum(a, size):
    max_sum = 0
    curr_sum = 0
    start_index = 0
    end_index = 0
    loop_index = 0

    for i in range(0, size):
        curr_sum = curr_sum + a[i]       
        if curr_sum < 0:
            curr_sum = 0
            loop_index = i + 1

        if curr_sum > max_sum :
            max_sum = curr_sum
            start_index = loop_index
            end_index = i
        
    return max_sum, start_index, end_index


Input_Ary = [-2, -3, 4, -1, -2, 1, 5, -3]

LargestSum, StartIndex, EndIndex = MaxSum(Input_Ary, len(Input_Ary))


print('SubArray = %s \t Largest SubArray Sum = %d', Input_Ary[StartIndex:EndIndex+1], LargestSum)