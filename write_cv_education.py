#import subprocess, os
#import pyperclip
import csv
import write_cv_main_functions as wc

### education

def compile_education(education_file, table_spacing,lwidth,rwidth):

    education_txt=wc.header_setup('Education', table_spacing,lwidth,rwidth)
    education_dict=wc.convert_csv_to_dict(education_file)

    for i in range(len(education_dict)):
        row=education_dict[i]

        institution=row['Institution']
        deg_type=row['Degree Acronym']
        location=row['Location']
        address=row['Address']
        school=row['School']
        major=row['Major']
        year=row['Year']
        advisor=row['Advisor']
        is_current=row['Current'].strip()=='Y'

#        school_data='\\textit{%s}, %s' %(school,location)

        note=''
        description=major
        if advisor!='':
            description=description+'. \\textbf{ Advisor}: '+advisor

        date=deg_type+', '+year

        if is_current==True:
            date='Projected: '+date

        is_end=i==len(education_dict)-1

        education_txt+=wc.create_table_entry(institution, date,is_end,school,location,note,description,False)


    return education_txt


