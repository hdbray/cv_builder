#import subprocess, os
#import pyperclip
import csv
import write_cv_main_functions as wc

#### academic positions

def compile_positions(positions_file, table_spacing,lwidth,rwidth):

    positions_txt=wc.header_setup('Positions', table_spacing,lwidth,rwidth)
    positions_dict=wc.convert_csv_to_dict(positions_file)

    for i in range(len(positions_dict)):
        row=positions_dict[i]

        institution=row['Institution']
        location=row['Location']
        address=row['Address']
        title=row['Title']
        start_mo=row['Starting Month']
        end_mo=row['Ending Month']
        start_yr=row['Starting Year']
        end_yr=row['Ending Year']
        is_current=row['Current'].strip()=='Y'

#        institution_data='\\textit{%s}. %s' % (institution, location)
        note=''
        description=''

        start_date=start_mo[:3]+' '+start_yr
        end_date=end_mo[:3]+' '+end_yr

        if is_current==True:
            end_date='present'

        date=start_date+'--'+end_date

        is_end=i==len(positions_dict)-1

        positions_txt=positions_txt+wc.create_table_entry(title,date,is_end,institution, location ,note,description,False)

    return positions_txt


