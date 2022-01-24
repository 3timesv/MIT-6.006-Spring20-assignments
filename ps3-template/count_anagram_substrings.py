def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []

    k = len(S[0])
    get_idx = lambda alpha: ord(alpha) - ord('a')

    # initialize hash table to store frequency tables and their counts
    H = {}

    # variable to hold the last frequency table
    prev_ft = None
    for i in range(len(T) - k + 1):
        # build the first frequency table by looping over substring
        # in O(k) time
        if i == 0:
            ft = [0] * 26
            for j in T[i:i+k]:
                ft[get_idx(j)] += 1
        # build other substrings using previous frequency table
        # in O(1) expected time
        else:
            ft = list(prev_ft)
            ft[get_idx(T[i-1])] -= 1
            ft[get_idx(T[i+k-1])] += 1

        # convert list to tuple to make it hashable
        ft = tuple(ft)

        # incrment the count of frequency table in the hash table
        # or add it if doesn't exist
        if ft in H:
            H[ft] += 1
        else:
            H[ft] = 1

        # set current frequency table as previous frequency table
        # for next substring
        prev_ft = ft

    for s_i in S:
        # build frequency table for s_i
        ft = [0] * 26
        for j in s_i:
            ft[get_idx(j)] += 1

        ft = tuple(ft)

        # find its value in data structure and append to A
        A.append(H[ft])

    return tuple(A)
