from collections import defaultdict

def solve():
    res = []
    j_list = list(movie_list - set(user_dic[target_user_id].keys()))
    i_list = list(user_dic[target_user_id].keys() - set(j_list))
    for j in j_list:
        Rj = 0
        hash_j = movie_hash[j]
        sum_dev_ji = 0
        for i in i_list:
            hash_i = movie_hash[i]
            dev_ji = 0
            if len(both_assessment[hash_j][hash_i]) > 0:
                for both_id in both_assessment[hash_j][hash_i]:
                    u = user_dic[both_id]
                    dev_ji += (u[j] - u[i]) / len(both_assessment[hash_j][hash_i])
                Rj += 1
                sum_dev_ji += dev_ji + user_dic[target_user_id][i]
        res.append([j, round(sum_dev_ji / Rj, 3)])
    res = sorted(res, key=lambda x:x[1], reverse=True)
    for result in res[:reco_size]:
        print(result[0], format(result[1], ".3f"))
