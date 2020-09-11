#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys

base_dir = '/home/pi'
prj_dir = base_dir + '/csn_raspi'
data_dir = prj_dir + '/earthquakes'
base_filename = 'csn.log'


def getCurrentData():
    with open(data_dir + '/' + base_filename, mode='r') as f:
        reader = f.readlines()
        last_index = len(reader) - 1
        # return reader[last_index]

        # print(reader[0])
        data = []
        for _line in reader[0:10]:
            # print(_line)
            data.append(_line)

    return data


def getDataBy(order, num):
    with open(data_dir + '/' + base_filename, mode='r') as f:
        reader1 = f.readlines()
        data = []
        num_last_index = len(reader1)-num
        i = 0
        if order == "head":
            for _line in reader1[0:num]:
                data.append(reader1[i])
                i = i+1
        return data
        #elif order == "tail"
            #for _line in reader1[num_last_index:num]:
                #data.append(reader1[i])
                #i = i+1
        #return data


if __name__ == "__main__":
   #_data = getCurrentData()
   # print(_data)

    _data1 = getDataBy("head",10)
    print(_data1)
