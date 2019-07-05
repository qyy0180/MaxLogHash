import  random
import  math
import argparse
import time
import sys
import mmh3
import numpy as np
from heapq import heapify,heappop,heappush

totalShingles = (1 << 32) - 1

def MaxLog(seed):
    randomNoA = hash_parameter(k)
    randomNoB = hash_parameter(k)

    for item in stream:
        # print "item"
        # print item
        if item [0] in maxShingleID.keys():
            max_hash_val_list = maxShingleID[item[0]][0]
            max_hash_sig_list = maxShingleID[item[0]][1]
            # print max_hash_val_list
            # print max_hash_sig_list
            for x  in range(0, k):
                temp = ((randomNoA[x] * mmh3.hash(str(item[1]),seed) + randomNoB[x]) % totalShingles)
                temp = temp / float(totalShingles)
                if temp != 0:
                   log_temp = - math.log(temp,2)
                   hash_val =  math.ceil(log_temp)
                elif temp == 0 :
                    hash_val = sys.getsizeof(temp)
                if hash_val > max_hash_val_list[x]:
                   max_hash_val_list[x] = hash_val
                   max_hash_sig_list[x] = 1
                elif hash_val == max_hash_val_list[x]:
                     max_hash_sig_list[x] = 0
            maxShingleID [item[0]][0]= max_hash_val_list
            maxShingleID [item[0]][1]= max_hash_sig_list
        else:
            max_hash_val_list = [0] * k
            max_hash_sig_list = [1] * k
            max_hash_res_new = []
            max_hash_res_new.append(max_hash_val_list)
            max_hash_res_new.append(max_hash_sig_list)
            maxShingleID[item[0]] = max_hash_res_new
    return


def hash_parameter(k):
    randList = []
    randIndex = random.randint(0, totalShingles - 1)
    randList.append(randIndex)
    while k > 0:
        while randIndex in randList:
              randIndex = random.randint(0, totalShingles - 1)
        randList.append(randIndex)
        k = k - 1

    return randList

def estimate():
    con = 0
    for x in range(0, k):
       if (maxShingleID['setA'][0][x] > maxShingleID['setB'][0][x] and  maxShingleID['setA'][1][x] ==1 ):
            con = con + 1
       elif (maxShingleID['setA'][0][x] < maxShingleID['setB'][0][x] and  maxShingleID['setB'][1][x] ==1 ):
            con = con + 1
    # print con
    num = float(k)
    # print num
    jaccard_sim = 1.0 - con*(1/num)*(1/0.7213)
    return jaccard_sim

if __name__ == '__main__':
    random_seed = 1
    card = 10000
    jaccard_true = 0.9
    k = int(128)
    total_num = card * 2
    sim = (2 * jaccard_true) / (1 + jaccard_true)

    maxShingleID = {}
    the_same_index = total_num / 2 * sim
    setA_uni_index = total_num / 2 * 1
    setB_uni_index = total_num / 2 * (2 - sim)

    stream = []
    #synthetic data
    for num in range(total_num):
        if num <= the_same_index:
            stream.append(['setA', num])
            stream.append(['setB', num])
        elif num <= setA_uni_index:
            stream.append(['setA', num])
        elif num <= setB_uni_index:
            stream.append(['setB', num])
        else:
            break

    MaxLog(random_seed)
    jaccard_est = estimate()
    print(jaccard_true, jaccard_est)



