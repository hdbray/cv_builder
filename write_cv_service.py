import csv
import write_cv_main_functions as wc

### service

def compile_service(service_file,
                    table_spacing,lwidth,rwidth,shortcv_boolean):

    service_dict=wc.convert_csv_to_dict(service_file,'Sorting Date')

    service_txt=wc.header_setup('Service and Leadership', table_spacing,lwidth,rwidth,False)


    other_service_count=0
    organizing_count=0
    committee_count=0
    leadership_count=0
    outreach_count=0

    other_service_index_count=0
    organizing_index_count=0
    committee_index_count=0
    leadership_index_count=0
    outreach_index_count=0



    ## count how many of each so you know the end of your table 

    for i in range(len(service_dict)):
        row=service_dict[i]
        activity_type=row['Type (service, committee work, outreach, leadership, organizing)']
        if activity_type=='service':
            other_service_count+=1
        elif activity_type=='organizing':
            organizing_count+=1
        elif activity_type=='committee work':
            committee_count+=1
        elif activity_type=='leadership':
            leadership_count+=1
        elif activity_type=='outreach':
            outreach_count+=1
        else:
            print('''

            error line %s of service type when sorted by Sorting Date

            ''' % (i))




    if other_service_count==0:
        other_service_txt=''
    else:
        other_service_txt=wc.subheader_setup('Professional Service', table_spacing,lwidth, rwidth)

    if organizing_count==0:
        organizing_txt=''
    else:
        organizing_txt=wc.subheader_setup('Organizational Work', table_spacing,lwidth, rwidth)

    if committee_count==0:
        committee_txt=''
    else:
        committee_txt=wc.subheader_setup('Committee Work', table_spacing,lwidth, rwidth)

    if leadership_count==0:
        leadership_txt=''
    else:
        leadership_txt=wc.subheader_setup('Leadership', table_spacing,lwidth, rwidth)

    if outreach_count==0:
        outreach_txt=''
    else:
        outreach_txt=wc.subheader_setup('Community Outreach', table_spacing,lwidth, rwidth)

    for i in range(len(service_dict)):
        row=service_dict[i]
        role=row['Role']
        activity_type=row['Type (service, committee work, outreach, leadership, organizing)']
        topic_or_org=row['Topic or Organization']
        details=row['Significant Details']
        description=row['Description']
        if shortcv_boolean==True:
            description=''

        start_day=row['Start Day']
        start_mo=row['Start Month']
        start_yr=row['Start Year']
        start_sem=row['Start Semester']
        end_day=row['End Day']
        end_mo=row['End Month']
        end_yr=row['End Year']
        end_sem=row['End Semester']

        date=wc.format_date(start_day,start_mo,start_yr,start_sem,end_day,end_mo,end_yr,end_sem)

        alt_start_list=[]

        alt_start_day1=row['Alternate Start Day 1']
        alt_start_mo1=row['Alternate Start Month 1']
        alt_start_yr1=row['Alternate Start Year 1']
        alt_start_sem1=row['Alternate Start Semester 1']

        alt_start_list.append([alt_start_day1,alt_start_mo1,alt_start_yr1,alt_start_sem1])

        alt_start_day2=row['Alternate Start Day 2']
        alt_start_mo2=row['Alternate Start Month 2']
        alt_start_yr2=row['Alternate Start Year 2']
        alt_start_sem2=row['Alternate Start Semester 2']

        alt_start_list.append([alt_start_day2,alt_start_mo2,alt_start_yr2,alt_start_sem2])

        alt_start_day3=row['Alternate Start Day 3']
        alt_start_mo3=row['Alternate Start Month 3']
        alt_start_yr3=row['Alternate Start Year 3']
        alt_start_sem3=row['Alternate Start Semester 3']

        alt_start_list.append([alt_start_day3,alt_start_mo3,alt_start_yr3,alt_start_sem3])


        for i in range(len(alt_start_list)):
            if alt_start_list[i][2]!='':
                date+=', '
                alt_date=wc.format_date(alt_start_list[i][0],alt_start_list[i][1],alt_start_list[i][2],alt_start_list[i][3],'','','','')
                date=date+alt_date

        if activity_type=='service':
            other_service_index_count+=1
            is_end=other_service_index_count==other_service_count
            other_service_txt+= wc.create_table_entry(role,date,is_end, topic_or_org, details, '', description,False)
        elif activity_type=='organizing':
            organizing_index_count+=1
            is_end=organizing_index_count==organizing_count
            organizing_txt+= wc.create_table_entry(role,date,is_end, topic_or_org, details, '', description,False)
        elif activity_type=='committee work':
            committee_index_count+=1
            is_end=committee_index_count==committee_count
            committee_txt+= wc.create_table_entry(role,date,is_end, topic_or_org, details, '', description,False)
        elif activity_type=='leadership':
            leadership_index_count+=1
            is_end=leadership_index_count==leadership_count
            leadership_txt+= wc.create_table_entry(role,date,is_end, topic_or_org, details, '', description,False)
        elif activity_type=='outreach':
            outreach_index_count+=1
            is_end=outreach_index_count==outreach_count
            outreach_txt+= wc.create_table_entry(role,date,is_end, topic_or_org, details, '', description,False)

#    other_service_txt+=wc.table_close()
#    outreach_txt+=wc.table_close()
#    leadership_txt+=wc.table_close()
#    organizing_txt+=wc.table_close()
#    committee_txt+=wc.table_close()

    service_txt+=leadership_txt+organizing_txt+committee_txt+other_service_txt+outreach_txt

    return service_txt

#
#
#
