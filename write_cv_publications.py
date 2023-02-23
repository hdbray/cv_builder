#import subprocess, os
import pyperclip
import csv
import write_cv_main_functions as wc

### some useful functions


#### publications CV data


def compile_publications(publications_file,table_spacing, lwidth, rwidth, selected=False):

    publications_txt=wc.header_setup('Preprints and Publications', table_spacing,lwidth,rwidth)
    selected_publications_txt=wc.header_setup('Selected Publications', table_spacing,lwidth,rwidth)

    publications_dict=wc.convert_csv_to_dict(publications_file)


    for i in range(len(publications_dict)):
        row=publications_dict[i]

        authors=row['Authors']
        title=row['Title']
        year=row['Year']
        status=row['Status']
        journal=row['Journal']
        vol=row['Volume']
        no=row['Number']
        pp=row['Pages']
        arxiv=row['ArXiv']
        doi=row['DOI']
        include=row['Compile']
        short_cv=row['Short CV']

        publication_main='''
        %s. \\textit{%s}. (%s). 
        ''' % (authors, title, year)


        if status=='published':
            journal_data=''
            if vol!='':
                if pp!='':
                    if no!='':
                        journal_data=journal_data+'\\textbf{%s}. Vol %s: (%s) %s.' % (journal, vol, no, pp)
                    else: 
                        journal_data=journal_data+'\\textbf{%s}. Vol %s: %s.' % (journal, vol, pp)
                else: 
                    if no!='':
                        journal_data=journal_data+'\\textbf{%s}. Vol %s: %s.' % (journal, vol, no)
                    else: 
                        journal_data=journal_data+'\\textbf{%s}. Vol %s.' % (journal, vol)
            else:
                journal_data=journal_data+'\\textbf{%s}.' % (journal)

        elif status=='to appear':
            journal_data='T%s in \\textbf{%s}.' % (status[1:], journal)
        elif status=='accepted':
            journal_data='A%s at \\textbf{%s}.' % (status[1:], journal)
        else:
            if arxiv!='':
                journal_data=' \\textbf{%s%s}. \\url{%s}' % (status[0].capitalize(),status[1:],arxiv)
            else:
                journal_data=' \\textbf{%s%s}. ' % (status[0].capitalize(),status[1:])



        publication_item=publication_main + journal_data

        is_end=i==len(publications_dict)-1

        publication_item=wc.create_table_entry(publication_item,year,is_end)

        if include=='Y':
            publications_txt=publications_txt+'\n'+publication_item
            if short_cv=='Y':
                selected_publications_txt=selected_publications_txt+'\n'+publication_item



    if selected==True:
        return selected_publications_txt
    else:
        return publications_txt




