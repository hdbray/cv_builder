#import subprocess, os
#import pyperclip
import csv
import write_cv_main_functions as wc

### pedagogical_training

def compile_pedagogical_training(pedagogical_training_file, table_spacing,lwidth,rwidth):

    pedagogical_training_txt=wc.header_setup('Pedagogical Training', table_spacing,lwidth,rwidth)
    pedagogical_training_dict=wc.convert_csv_to_dict(pedagogical_training_file,'Sorting Date')

    for i in range(len(pedagogical_training_dict)):
        row=pedagogical_training_dict[i]

        workshop=row['Workshop']
        location=row['Location']
        institution=row['Institution']
        department=row['Department']
        start_sem=row['Start Semester']
        start_yr=row['Start Year']
        end_sem=row['End Semester']
        end_yr=row['End Year']
        alt_sem2=row['Semester 2']
        alt_yr2=row['Year 2']
        alt_sem3=row['Semester 3']
        alt_yr3=row['Year 3']

        if row['Active'].strip()=='Y':
            active=True
        else: 
            active=False

        date=wc.format_date('','',start_yr,start_sem,'','',end_yr,end_sem,active)

        if alt_sem2!='':
            alt_date=wc.format_date('','',alt_yr2,alt_sem2,'','','','',False)
            date=date+', '+alt_date

        description=row['Description']


        note=''

        dept_data='%s. %s' % (department,location)

        is_end=i==len(pedagogical_training_dict)-1

        pedagogical_training_txt+=wc.create_table_entry(workshop, date,is_end,institution, dept_data,note,description,False)

#    pedagogical_training_txt=pedagogical_training_txt+wc.table_close()

    return pedagogical_training_txt


