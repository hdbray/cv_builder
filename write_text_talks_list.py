#import subprocess, os
#import pyperclip
import csv
import write_cv_main_functions as wc

### talks_visits

def compile_talks_visits(talks_visits_file): #, table_spacing,lwidth,rwidth):

    talks_visits_dict=wc.convert_csv_to_dict(talks_visits_file,'Sorting Date')

    talks_visits_txt=''#talks_visits_dict[2]

    for i in range(2,len(talks_visits_dict)):
        row=talks_visits_dict[i]
        if wc.string_to_float(row['Start Year'])>2018 and row['Role (speaker, conference participant, seminar participant, or visitor)']=='speaker':
            talks_visits_txt+=row['Event']+'. '+row['Institution']+'.  '+row['Location']+'. '+row['Sorting Date']+'\n'



#    talks_visits_txt=wc.header_setup('Conferences, Seminars, Workshops, and Visits', table_spacing,lwidth,rwidth,False)
#
#    invited_talks_count=0
#    invited_talks_index_count=0
#    conferences_attended_count=0
#    conferences_attended_index_count=0
#    seminars_attended_count=0
#    seminars_attended_index_count=0
#    invited_guest_count=0
#    invited_guest_index_count=0
#
#    ## count total in each category
#    
#    for i in range(len(talks_visits_dict)):
#        row=talks_visits_dict[i]
#        event_type=row['Type (seminar, workshop, conference, invited visit, colloquium, minicourse)']
#        role=row['Role (speaker, conference participant, seminar participant, or visitor)']
#
#        if role=='conference participant':
#            conferences_attended_count+=1
#        elif role=='seminar participant':
#            seminars_attended_count+=1
#        elif role=='speaker':
#            invited_talks_count+=1
#        elif role=='visitor':
#            invited_guest_count+=1
#
#    ### compile invited talks
#
#    if invited_talks_count==0:
#        invited_talks_txt=''
#    else: 
#        invited_talks_txt= wc.subheader_setup('Invited Presentations', table_spacing,lwidth, rwidth)
#    if seminars_attended_count==0:
#        seminars_attended_txt=''
#    else: 
#        seminars_attended_txt= wc.subheader_setup('Seminars Attended', table_spacing,lwidth, rwidth)
#    if conferences_attended_count==0:
#        conferences_attended_txt=''
#    else: 
#        conferences_attended_txt= wc.subheader_setup('Conferences Attended', table_spacing,lwidth, rwidth)
#    if invited_guest_count==0:
#        invited_guest_txt=''
#    else: 
#        invited_guest_txt=wc.subheader_setup('Invited Visits', table_spacing,lwidth, rwidth)
#
#    for i in range(len(talks_visits_dict)):
#        row=talks_visits_dict[i]
#
#        event=row['Event']
#        location=row['Location']
#        institution=row['Institution']
#        event_type=row['Type (seminar, workshop, conference, invited visit, colloquium, minicourse)']
#        role=row['Role (speaker, conference participant, seminar participant, or visitor)']
#        link=row['Link']
#
#        start_date=row['Start Day']
#        start_mo=row['Start Month']
#        start_sem=row['Start Semester']
#        start_yr=row['Start Year']
#        end_date=row['End Day']
#        end_mo=row['End Month']
#        end_sem=row['End Semester']
#        end_yr=row['End Year']
#
#        if row['Active'].strip()=='Y':
#            active=True
#        else: 
#            active=False
#
#        date=wc.format_date(start_date, start_mo, start_yr,start_sem,end_date,end_mo,end_yr,end_sem,active)
#
#        description=''
#
#        note=row['Note']
#
#        if role=='conference participant':
#            conferences_attended_index_count+=1
#            is_end=conferences_attended_index_count==conferences_attended_count
#            conferences_attended_txt+=wc.create_table_entry(event,date,is_end,institution, location, note, description,False)
#
#        elif role=='seminar participant':
#            seminars_attended_index_count+=1
#            is_end=seminars_attended_index_count==seminars_attended_count
#            seminars_attended_txt+=wc.create_table_entry(event,date,is_end,institution, location, note, description,False)
#        elif role=='speaker':
#            invited_talks_index_count+=1
#            is_end=invited_talks_index_count==invited_talks_count
#            invited_talks_txt+=wc.create_table_entry(event,date,is_end,institution, location, note, description,False)
#        elif role=='visitor':
#            invited_guest_index_count+=1
#            is_end=invited_guest_index_count==invited_guest_count
#            invited_guest_txt+=wc.create_table_entry(event,date,is_end,institution, location, note, description,False)
#
#        
#    talks_visits_txt+=invited_talks_txt
#    talks_visits_txt+=conferences_attended_txt
#    talks_visits_txt+=seminars_attended_txt
#    talks_visits_txt+=invited_guest_txt
#
#
    return talks_visits_txt

print(compile_talks_visits('csv_files/talks_visits.csv'))

#
#
#
