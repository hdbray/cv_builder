#import pyperclip
import csv
import write_cv_main_functions as wc

#### grants and awards CV data

def compile_teaching(teaching_file, table_spacing,lwidth,rwidth):

    teaching_txt=wc.header_setup('Teaching Experience', table_spacing,lwidth,rwidth, False)
    teaching_dict=wc.convert_csv_to_dict(teaching_file)

    institutions_set=set()
    institutions_count_dict={}
    institutions_index_count_dict={}
    institution_txt_dict={}

    # build the set of distint institutions and keep track of how many
    # times taught at each institution (so that your code knows when to
    # close the table environment)

    for i in range(len(teaching_dict)):
        row=teaching_dict[i]

        role=row['Role']
        course=row['Course']
        institution=row['Institution']

        if institution in institutions_set:
            institutions_count_dict[institution]+=1
        else: 
            institutions_set.add(institution)
            institutions_count_dict[institution]=1
            institutions_index_count_dict[institution]=0

    # subheaders for each institution added to the dictionary of strings
    # the dictionary of strings is called institution_txt_dict
    # key = institutions (string) value = text to add to the document
    # (string)

    for institution in institutions_set:
        institution_txt_dict[institution]= wc.subheader_setup(institution, table_spacing, lwidth, rwidth)

    # add rows to the appropriate table in the .tex file for each entry of
    # the csv. There is a table for each institution

    for i in range(len(teaching_dict)):
        row=teaching_dict[i]

        role=row['Role']
        course_no=row['Course Number']
        course=row['Course']
        if course_no!='':
            course='{\\normalfont %s:} %s' % (course_no, course)

        institution=row['Institution']
        start_sem=row['Start Semester']
        start_year=row['Start Year']
        end_sem=row['End Semester']
        end_year=row['End Year']
        note=row['Note']
        description=row['Description']
    
        description=''

        date=wc.format_date('', '', start_year, start_sem, '', '', end_year, end_sem, active=False)

        for given_institution in institutions_set:
            if institution==given_institution:
                institutions_index_count_dict[given_institution]+=1

                is_end=institutions_count_dict[given_institution]==institutions_index_count_dict[given_institution]

                institution_txt_dict[given_institution]+=wc.create_table_entry(course,date,is_end,role, '', note, description,False)


    # add everybody to the main string


    for key in institutions_set:
        teaching_txt+=institution_txt_dict[key]

    return teaching_txt


