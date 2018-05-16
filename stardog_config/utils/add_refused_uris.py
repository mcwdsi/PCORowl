#!/bin/python

import csv

input_file = "demographic.csv"
output_file = "demographic_added_cols.csv"
starting_uri = 100000000000
new_cols = ['pr_uri', 'p_uri', 'p_patid_uri', 'patid_uri', 'p_pheno_sex', 'p_neonate_stage_uri', 'p_birth_uri', 't1_uri', 'tr2_uri', 'tr3_uri', 'eip1_uri', 'hlid1_uri', 'etl1_uri', 'pnhid1_uri']

with open(input_file, "r") as csvfile:
    file_reader = csv.DictReader(csvfile)
    file_reader_list = []
    for row in file_reader:
        file_reader_list.append(row)
    fieldnames = file_reader.fieldnames
    for item in new_cols:
        fieldnames.append(item)    
    for new_col in new_cols:
        for row in file_reader_list:
       #     print row
            row[new_col] = starting_uri
            starting_uri+=1
            #print row
        #file_reader.seek(0)
    with open(output_file, "w") as csv_output:    
        writer = csv.DictWriter(csv_output, fieldnames)
        writer.writeheader()
        for row in file_reader_list:
            writer.writerow(row)
          
