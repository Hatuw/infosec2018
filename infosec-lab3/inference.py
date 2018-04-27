# -*- coding:utf-8 -*-
"""
Inference of infosec2018-lab3
Author: Hatuw
Mail: jiaxi_wu@ieee.org
"""

# import urllib
import pandas as pd

SNO = 28    # student no.
rank_file = './school_list.xlsx'

# load the scholl list
schools = pd.read_excel(rank_file, [0, 1])

# get the list for processing
tmp_slice = range((SNO-1)*4, SNO*4)
domestic_list = schools[0].iloc[tmp_slice, 1].values
foreign_list = schools[1].iloc[tmp_slice, 1].values
for school in domestic_list:
    print(school)
for school in foreign_list:
    print(school)
