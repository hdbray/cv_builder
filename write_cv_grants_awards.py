#import pyperclip
import csv
import write_cv_main_functions as wc

#### grants and awards CV data

def compile_grants_awards(grants_awards_file, table_spacing,lwidth,rwidth,is_appendix,shortcv_boolean):

    grants_awards_dict=wc.convert_csv_to_dict(grants_awards_file,'Sorting Date')

    grants_dict=[]
    awards_dict=[]
    appendix_dict=[]
    appendix_indices=[]


    for i in range(len(grants_awards_dict)):
        if grants_awards_dict[i]['Status']=='pending' or grants_awards_dict[i]['Status']=='declined':
            appendix_indices.append(i)
            appendix_dict.append(grants_awards_dict[i])
        elif grants_awards_dict[i]['Type']=='Grant' or grants_awards_dict[i]['Type']=='Conference Grant' or grants_awards_dict[i]['Type']=='Research Grant':
            grants_dict.append(grants_awards_dict[i])
        elif grants_awards_dict[i]['Type']=='Award' or grants_awards_dict[i]['Type']=='Fellowship' :
            awards_dict.append(grants_awards_dict[i])


    for i in appendix_indices:
        del grants_awards_dict[i]

    grants_length=len(grants_dict)-1
    awards_length=len(awards_dict)-1
    appendix_length=len(appendix_dict)-1

### start compiling the text for grants

    grants_txt=wc.header_setup('Grants and Funding', table_spacing,lwidth,rwidth)
    length=grants_length

    for i in range(len(grants_dict)):

        row=grants_dict[i]

        award_name=row['Award Name']
        institution_name=row['Institution Name']
        award_type=row['Type']
        pis=row['PIs']
        copis=row['Co-PIs']




        start_mo=row['Starting Month']
        if start_mo!='':
            start_mo=start_mo[:3]
        end_mo=row['Ending Month']
        if end_mo!='':
            end_mo=end_mo[:3]
        start_year=row['Starting Year']
        end_year=row['Ending Year']
        award_amt=row['Awarded Amount']
        note=row['Note']
        description=row['Description']
    

        if pis!='':
            if copis!='':
                description='PI(s): %s. Co-PI(s): %s.' % (pis,copis)
            else: 
                description='PI(s): %s.' % (pis)
        else:
            if copis!='': 
                description='Co-PI(s): %s.' % (copis)
        
        
        date=wc.format_date('', start_mo, start_year, '', '', end_mo, end_year, '', active=False)

        is_end=i==length #len(grants_dict)-1

        if award_amt!='':
            award_amt='\$'+award_amt
            if note!='':
                note=award_amt+'. '+note
            else: 
                note=award_amt

        add_text=wc.create_table_entry(award_name,date,is_end,institution_name, '', note, description,False)

        grants_txt=grants_txt+add_text


### start compiling the text for awards

    awards_txt=wc.header_setup('Awards and Honors', table_spacing,lwidth,rwidth)
    length=awards_length

    for i in range(len(awards_dict)):

        row=awards_dict[i]

        award_name=row['Award Name']
        institution_name=row['Institution Name']
        award_type=row['Type']
        pis=row['PIs']
        copis=row['Co-PIs']




        start_mo=row['Starting Month']
        if start_mo!='':
            start_mo=start_mo[:3]
        end_mo=row['Ending Month']
        if end_mo!='':
            end_mo=end_mo[:3]
        start_year=row['Starting Year']
        end_year=row['Ending Year']
        award_amt=row['Awarded Amount']
        note=row['Note']
        description=row['Description']
    

        date=wc.format_date('', start_mo, start_year, '', '', end_mo, end_year, '', active=False)

        is_end=i==length #len(awards_dict)-1

        if award_amt!='':
            award_amt='\$'+award_amt
            if note!='':
                note=award_amt+'. '+note
            else: 
                note=award_amt

        add_text=wc.create_table_entry(award_name,date,is_end,institution_name, '', note, description,False)

        awards_txt=awards_txt+add_text

    if shortcv_boolean==False:
        grants_txt+='''

        \\bigskip

See Appendix for a list of additional proposals submitted to the NSF and
Simons Foundation.

    '''


### start compiling the text for appendix (pending and declined)

    appendix_txt=wc.header_setup('Appendix: Submitted Grant Applications', table_spacing,lwidth,rwidth)
    length=appendix_length

    for i in range(len(appendix_dict)):

        row=appendix_dict[i]

        award_name=row['Award Name']
        institution_name=row['Institution Short Name']
        award_type=row['Type']
        pis=row['PIs']
        copis=row['Co-PIs']




        # for appendix, only need date of submission

        mo=row['Application Month'][:3]
        year=row['Application Year']

        award_amt=row['Awarded Amount']
        note=row['Note']
        
        if row['Status']=='pending':
            if note=='':
                note='Pending.'
            else:
                note+='. Pending.'

        if row['Status']=='declined':
            if note=='':
                note='Declined.'
            else:
                note+='. Declined.'

        description=row['Description']
    

        date=wc.format_date('', mo, year, '', '', '', '', '', active=False)

        is_end=i==length #len(appendix_dict)-1

        if award_amt!='':
            award_amt='\$'+award_amt
            if note!='':
                note=award_amt+'. '+note
            else: 
                note=award_amt

        add_text=wc.create_table_entry('',date,is_end,institution_name, '', note, description,False)

        appendix_txt=appendix_txt+add_text

## return appropriate strings

    if is_appendix==True:
        return appendix_txt
    else: 
        return grants_txt+awards_txt


