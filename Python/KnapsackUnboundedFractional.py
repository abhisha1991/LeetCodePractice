def unbound_frac_knapsack(n, w, vals, wts, wt_counts):
    result = 0
    result_list = []
    all_wt = 0
    for idx, i in enumerate(wt_counts):
        all_wt += i * wts[idx]
        if all_wt > w:
            break

    if all_wt <= w:
        all_val = 0
        for idx, i in enumerate(wt_counts):
            all_val += i * vals[idx]
        print(all_val)
        return all_val

    val_wt = dict()
    for i in range(n):
        val_wt[i] = vals[i]/wts[i]

    kv = get_max_kv(val_wt)
    k = int(kv[0])
    while wt_counts[k] <= 0:
        del val_wt[k]
        kv = get_max_kv(val_wt)
        k = int(kv[0])

    while w > 0 and w >= wts[k] and wt_counts[k] > 0:
        w = w - wts[k]
        result += vals[k]
        result_list.append(wts[k])
        wt_counts[k] -= 1
        if wt_counts[k] == 0:
            del val_wt[k]
            kv = get_max_kv(val_wt)
            k = int(kv[0])
            continue

    if w < wts[k]:
        result += val_wt[k] * w
        result_list.append(w)
        wt_counts[k] -= 1

    print(wt_counts)
    print(result_list)
    print(result)
    return result


def get_max_kv(dic):
    import operator
    return max(dic.items(), key=operator.itemgetter(1))
    # For printing the k,v pair with the max value

unbound_frac_knapsack(3, 501, [100, 200, 500], [30, 40, 100], [40, 3, 2])
