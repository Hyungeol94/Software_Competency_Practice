def solution(sequence, k):=
    seq_length = len(sequence)
    for subseq_length in range(seq_length):
        subseq_sum = sum(sequence[:subseq_length])
        start = 0
        end = subseq_length-1
        while True:            
            if subseq_sum == k:
                return [start, end]
            if k < subseq_sum: break                
            end += 1
            if end == seq_length: break            
            subseq_sum = subseq_sum-sequence[start]+sequence[end]
            start += 1