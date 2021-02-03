# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:21:35 2021

@author: mehdi
"""

import os
import glob
import pandas as pd
os.chdir("D:/XAI/DB/DISFA/CSV/DISFA_CSV_256/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

