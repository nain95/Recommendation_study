def msd_sim(data1, data2):
    res = 0
    i_list = []
    for idx in range(range(data1)):
        if data1[idx] != -1 and data2[idx] != -1:
            i_list.append(idx)
    sigma = 0
    for i in i_list:
        sigma += pow(data1[i] - data2[i], 2)
    msd = sigma / len(i_list)
    return 1 / (msd + 1)
