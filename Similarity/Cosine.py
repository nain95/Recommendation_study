def cosine_sim(data1, data2):
    i_list = []
    for idx in range(len(data1)):
        if data1[idx] != -1 and data2[idx] != -1:
            i_list.append(idx)
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in i_list:
        numerator += data1[i] * data2[i]
        denominator1 += data1[i] ** 2
        denominator2 += data2[i] ** 2
    denominator = pow(denominator1, 0.5) * pow(denominator2, 0.5)
    if denominator == 0:
        return 0
    else:
        return round(numerator / denominator, 6)
