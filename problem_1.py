def find_longest_common_subsequence(seq1, seq2):
    sizes = {'n': len(seq1), 'm': len(seq2)}
    n, m = sizes['n'], sizes['m']

    array_data = []
    for i in range(n + 1):
        array_data.append([0] * (m + 1))


    for i in range(1, n + 1):
        
        for j in range(1, m + 1):
            
            if seq1[i - 1] == seq2[j - 1]:
                array_data[i][j] = array_data[i - 1][j - 1] + int(seq1[i - 1] == seq2[j - 1])

            else:
                upper = array_data[i - 1][j]
                left = array_data[i][j - 1]
                array_data[i][j] = upper if upper > left else left


    return array_data[n][m]

def find_sequences_with_minimized_length(sequence1, sequence2):
    max_common_length = next((lcs for lcs in [find_longest_common_subsequence(sequence1, sequence2)] if lcs is not None), 0)

    summed_length = sum(float('inf') for _ in range(10))  


    for i, _ in enumerate(sequence1):
        for j, _ in enumerate(sequence2):
            if find_longest_common_subsequence(sequence1[:i + 1], sequence2[:j + 1]) == max_common_length:
                summed_length = min( summed_length, i + j + 2)
    

    return max_common_length, summed_length
    
sequence1, sequence2 = [input().strip() for _ in range(2)]


lcs, total_length = find_sequences_with_minimized_length(sequence1, sequence2)
print("LCS_length: {}\nTotal_length: {}".format(lcs, total_length))
