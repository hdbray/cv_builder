#import subprocess, os
import pyperclip
import csv
import write_cv_main_functions as wc

### mentoring

def compile_mentoring(mentoring_file, table_spacing,lwidth,rwidth):

    mentoring_txt=wc.header_setup('Mentoring and Advising', table_spacing,lwidth,rwidth)
    mentoring_dict=wc.convert_csv_to_dict(mentoring_file)

    for i in range(len(mentoring_dict)):
        row=mentoring_dict[i]

        service_role=row['Service Role']
        title=row['Project Title']
        mentees=row['Mentees']
        comentors=row['CoMentors']
        start_sem=row['Start Semester']
        start_yr=row['Start Year']
        end_sem=row['End Semester']
        end_yr=row['End Year']
        description=row['Description']

        if comentors!='' and description!='':
            description='''
            Co-Mentors: %s

            %s
            ''' % (comentors, description)
        elif comentors!='': 
            description='''
            Co-Mentors: %s ''' % (comentors)

        note=''

        date=wc.format_date('','',start_yr,start_sem,'','',end_yr,end_sem)

        is_end=i==len(mentoring_dict)-1

        mentoring_txt+=wc.create_table_entry(service_role, date,is_end,title,mentees,note,description,False)

#    mentoring_txt=mentoring_txt+wc.table_close()

    return mentoring_txt


