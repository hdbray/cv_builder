#import subprocess, os
import pyperclip
import csv
import write_cv_main_functions as wc

### mentoring

def compile_mentoring(mentoring_file, table_spacing,lwidth,rwidth,shortcv=False):
    mentoring_txt=wc.header_setup('Mentoring', table_spacing,lwidth,rwidth,False)
    mentoring_dict=wc.convert_csv_to_dict(mentoring_file,'Sorting Date')

    undergrad_research_count=0
    other_count=0
    phd_count=0

    undergrad_research_index_count=0
    other_index_count=0
    phd_index_count=0

## count how many of each so you know the end of your table

    for i in range(len(mentoring_dict)):
        row=mentoring_dict[i]
        mentoring_type=row['Type (undergrad_research, phd, other)']
        if mentoring_type=='undergrad_research':
            undergrad_research_count+=1
        elif mentoring_type=='phd':
            phd_count+=1
        elif mentoring_type=='other':
            other_count+=1
        else:
            print('''
            error line %s of mentoring type sorted by Sorting Date in
            reverse chronological order. Except this isn't working so just
            look for the following row.
                  ''' % (i) )
            print(row)


    if undergrad_research_count==0:
        undergrad_research_txt=''
    else:
        undergrad_research_txt=wc.subheader_setup('Undergraduate Research', table_spacing,lwidth, rwidth) 

    if phd_count==0:
        phd_txt=''
    else:
        phd_txt=wc.subheader_setup('PhD Advising', table_spacing,lwidth, rwidth) 

    if other_count==0:
        other_txt=''
    else:
        other_txt=wc.subheader_setup('Other Mentoring', table_spacing,lwidth, rwidth) 

    for i in range(len(mentoring_dict)):
        row=mentoring_dict[i]

        mentoring_type=row['Type (undergrad_research, phd, other)']
        service_role=row['Service Role']
        title=row['Project Title']
        mentees=row['Mentees']
        comentors=row['CoMentors']
        start_mo=row['Start Month']
        start_yr=row['Start Year']
        end_mo=row['End Month']
        end_yr=row['End Year']
        description=row['Description']

        if comentors!='' and note!='':
            description='''
            Co-Mentors: %s

            %s

            %s

            ''' % (comentors, description,note)
        if comentors!='': 
            description='''
            Co-Mentors: %s 

            %s
            ''' % (comentors, description)

        if shortcv==True:
            description=''

        note=''


        date=wc.format_date('',start_mo,start_yr,'','',end_mo,end_yr,'')


        if mentoring_type=='undergrad_research':
            undergrad_research_index_count+=1
            is_end=undergrad_research_index_count==undergrad_research_count

            undergrad_research_txt+=wc.create_table_entry(service_role, date,is_end,title,mentees,note,description,False)

        if mentoring_type=='phd':
            phd_index_count+=1
            is_end=phd_index_count==phd_count

            phd_txt+=wc.create_table_entry(service_role, date,is_end,title,mentees,note,description,False)

        if mentoring_type=='other':
            other_index_count+=1
            is_end=other_index_count==other_count

            other_txt+=wc.create_table_entry(service_role, date,is_end,title,mentees,note,description,False)

#        is_end=i==len(mentoring_dict)-1

#        mentoring_txt+=wc.create_table_entry(service_role, date,is_end,title,mentees,note,description,False)

    
    mentoring_txt+=phd_txt+undergrad_research_txt+other_txt

    return mentoring_txt


