# https://codefights.com/interview/f9A6Mo8wek6qwfa94
def repeatedDNASequences(s):
    if s is "":
        return []
    list_s = list(s)
    result = dict()
    length = 10
    len_list_s = len(list_s)
    for i in range(len_list_s):
        if len_list_s - i < length:
            break
        original_seq = ''.join(list_s[i:length + i])
        if original_seq in result:
            continue
        count = 1
        result[original_seq] = count
        j = i + 1  # sequence start index of target dna sequence
        while (len_list_s - j >= length):
            target_seq = ''.join(list_s[j:length + j])
            # print(target_seq)
            if (original_seq == target_seq):
                count = count + 1
                result[original_seq] = count
                break
                # if (count > 1):
                #    break

            j = j + 1

    result_list = []
    for k, v in result.items():
        if v > 1:
            print("key:" + k + " and " + "value:" + str(v))
            result_list.append(k)

    if len(result_list) == 0:
        return []

    return sorted(result_list)


# print(repeatedDNASequences("A"))
print(repeatedDNASequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# print(repeatedDNASequences("CGACGCAATTTAGAACGGGCCGCACTGCAACCATTGCTCAGACAACGCATGAGTTAAATTTCACAAGTGATAGTGGCTTGCGAGACGTGGGTTGGTGGTAGCGTACGCCCGCTATTCGCCCCTAACGTGACGGGATTATAAGGTCGCTTCCCGGAATGCGCAGACGAGTCTCCGGTTTAGCCTAGACGTCTCACGCGCGCAAGGCGTCAGTTCTCACTATCTCGCACAGGTGTATTCTATTAGTTATGGGTTCTCACTACAGTCGGTTACTTCCTCATCCATTTCTGCATACGGGTCAACTAACAGTGTCATGGGGTATTGGGAAGGATGCGTTTTTAAACCCTCTCAGTAGCGCGAGGATGCCCACAAATACGACGGCGGCCACGGATCTAATGCGAAGCTAGCGACGCTTTCCAGCAACGAGCGCCCCACTTATGACTGCGTGGGGCGCTCCGCTTTCCTAGAGAACATAGATGGTGTTTTCGAATCGTAACCACTTA"))
