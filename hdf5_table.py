# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/26 13:49
@Author:      CookieYang
@FileName:    hdf5_table.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import tables as tb
# need to open HDF5 files
h5f1 = tb.File('1.h5','r')
h5f2 = tb.File('2.h5','r')
# define data and sdata datasets:
data  = h5f1.root.data
sdata = h5f2.root.sdata

# Step 1: Get a Numpy array of the 'ids' field/column from data DS:
ids_arr = data.read(field='ids')
# Step 2: Get new array with unique values only:
uids_arr = np.unique(ids_arr)

#Or, combine steps 1 and 2 into one line:
uids_arr = np.unique(data.read(field='ids'))

# Step 3a: Loop on rows of unique id values
for id_test in uids_arr :hi

# Step 3b: Get an array with all rows that match this id value,
#          Only returns values in field 'a'
     match_row_arr = sdata.read_where('ids==id_test',field='a')