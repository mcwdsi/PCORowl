#!/bin/python

import csv

input_file = "demographic_cut.csv"
output_file = "demographic_added_cols.csv"
starting_uri = 100000000000
new_cols = ['pr_uri', 'p_uri', 'p_patid_uri', 'patid_uri', 'p_pheno_sex', 'p_neonate_stage_uri', 'p_birth_uri', 't1_uri', 'tr2_uri', 'tr3_uri', 'eip1_uri', 'hlid1_uri', 'etl1_uri', 'pnhid1_uri', 'hlid2_uri', 'rip1_uri', 'pnhid2_uri']

limited_new_cols = ['rta2_uri', 'ridqap1_uri']

with open(input_file, "r") as csvfile:
    file_reader = csv.DictReader(csvfile)
    file_reader_list = []
    for row in file_reader:
        file_reader_list.append(row)
    fieldnames = file_reader.fieldnames
    for item in new_cols:
        fieldnames.append(item)

    for item in limited_new_cols:
        fieldnames.append(item)

    for new_col in new_cols:
        for row in file_reader_list:
            
            row[new_col] = starting_uri
            starting_uri+=1

    for new_col in limited_new_cols:
        print(new_col)
        for row in file_reader_list:
            if row['race'] == '07':
                #print(starting_uri)
                row[new_col] = starting_uri
                starting_uri+=1

    with open(output_file, "w") as csv_output:    
        writer = csv.DictWriter(csv_output, fieldnames)
        writer.writeheader()
        for row in file_reader_list:
            writer.writerow(row)
          
