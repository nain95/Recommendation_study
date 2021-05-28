def pearson_sim(data1, data2):
    i_list = []
    data1_sum = 0
    data1_cnt = 0
    data2_sum = 0
    data2_cnt = 0
    for idx in range(len(data1)):
        if data1[idx] != -1 and data2[idx] != -1:
            i_list.append(idx)
        else:
            if data1[idx] != -1:
                data1_sum += data1[idx]
                data1_cnt += 1
            if data2[idx] != -1:
                data2_sum += data2[idx]
                data2_cnt += 1
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    data1_avg = 0
    data2_avg = 0
    if data1_cnt != 0:
        data1_avg = data1_sum / data1_cnt
    if data2_cnt != 0:
        data2_avg = data2_sum / data2_cnt
    for i in i_list:
        numerator += (data1[i] - data1_avg) * (data2[i] - data2_avg)
        denominator1 += pow(data1[i] - data1_avg, 2)
        denominator2 += pow(data2[i] - data2_avg, 2)
    denominator = pow(denominator1, 0.5) * pow(denominator2, 0.5)
    if denominator == 0:
        return 0
    else:
        return round(numerator / denominator, 6)
