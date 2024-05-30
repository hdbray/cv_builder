#import subprocess, os
#import pyperclip
import csv

### some useful functions

def table_setup(table_spacing,lwidth,rwidth):
    return '''
    \\begin{center}
    {
    \\renewcommand{\\arraystretch}{%s}
    \\begin{longtable}{p{%s\\textwidth}  p{%s\\textwidth}}
    ''' % (table_spacing,lwidth,rwidth)

def header_setup(headername, table_spacing,lwidth,rwidth,include_table_setup=True):
    add_table_setup=''
    if include_table_setup==True:
        add_table_setup=table_setup(table_spacing,lwidth,rwidth)
    add_table_setup='''
    \\medskip

    \\myheader{%s}

    \\medskip
    ''' % (headername) +add_table_setup
    if include_table_setup==False:
        add_table_setup=add_table_setup+'\\medskip\n\n'
    return add_table_setup

def subheader_setup(headername, table_spacing,lwidth,rwidth,include_table_setup=True):
    add_table_setup=''
    if include_table_setup==True:
        add_table_setup=table_setup(table_spacing,lwidth,rwidth)
    return '''

    \\textbf{\\large %s}
    ''' % (headername) +add_table_setup


def table_close():
    return '''
    \\end{longtable}
    } 
    \\end{center}

    \\vspace{-1em}
    '''

def string_to_float(string):
    if string=='':
        return 0
    else:
        return float(string)

def convert_csv_to_dict(filename,sort_key=''):
    #filename should be a string
    #it is the prefix 
    #do not include the ex
    
    temp_list=[]
    list_of_dicts=[]
    
    with open(filename) as open_file:
        reader=csv.reader(open_file, quotechar='"')
        for row in reader:
            temp_list.append(row)
    
    
    k=len(temp_list)
    
    headers=temp_list[0]


    # sort list
      
    if sort_key!='':
        index=0
    
        for i in range(len(headers)):
            if headers[i]==sort_key:
                index=i
                break
    
        sorted_list=[]
    
        sorted_list.append(headers)
    
        entries_for_sorting=temp_list[1:]
    
        entries_for_sorting.sort(key=lambda a: a[index].lower(), reverse=True)
    
        sorted_list.extend(entries_for_sorting)
    
        temp_list=sorted_list

    
    for i in range(k):
            list_of_dicts.append({})

    for i in range(k):
        for j in range(len(headers)):
            list_of_dicts[i][headers[j]]=temp_list[i][j].strip()

    return list_of_dicts[1:]

def format_date(start_day='', start_mo='', start_yr='', start_sem='', end_day='', end_mo='', end_yr='', end_sem='', active=False):

#    start_sem=start_sem[:2]
#    end_sem=end_sem[:2]
    if start_mo!='' and start_mo.strip()!='May':
        start_mo=start_mo.strip()[:3]+'.'
    if end_mo!='' and end_mo.strip()!='May':
        end_mo=end_mo.strip()[:3]+'.'

    if start_yr==end_yr:
        if start_mo==end_mo:
            start_date='%s %s' % (start_day, start_sem)
        else: 
            start_date='%s %s %s' % (start_day, start_mo, start_sem)
    else: 
        start_date='%s %s %s %s' % (start_day, start_mo, start_sem, start_yr.strip())
    end_date='%s %s %s %s' % (end_day, end_mo, end_sem, end_yr.strip())
    if active==True:
        return start_date+' -- present'
    elif end_yr=='': 
        return start_date
    else: 
        return start_date+' -- '+end_date




def create_table_entry(main,date=0,end=True, primary_note='', location='', secondary_note='', description='',simple=True):
    add_note=''
    add_descr=''
    if primary_note!='':
        primary_note='\\textit{%s}. '% (primary_note)
    if secondary_note!='':
        add_note='(%s)' % secondary_note.strip()
    if description!='':
        add_descr='''
        \\hspace{-1em}

        {\\small
        \\begin{itemize}
        \\setlength{\\parindent}{0em}
        \item[] %s
        \\end{itemize}
        }
        \\vspace{-1em}
        ''' % (description)
#        add_descr='\n'+'\n {\\small \\qquad %s}' % description
#        add_descr='''
#        \\begin{center}
#        \\begin{minipage}[t]{.75\\textwidth}
#        {\\small %s}
#        \\end{minipage}
#        \\end{center}
#        
#
#        \\vspace{-1em}
#        ''' % (description)
    if location!='':
        location=' '+location+'. '
    if simple==True:
        text='%s & %s' % (date,main)
    elif main=='':
        text='%s & %s%s%s%s ' % (date, primary_note, location, add_note, add_descr)
    else: 
        text='%s & \\textbf{%s}. %s%s%s%s ' % (date, main,primary_note, location, add_note, add_descr)
    if end==False:
        text+='\\'+'\\ \n'
    else: 
        text+=table_close()

    return text


