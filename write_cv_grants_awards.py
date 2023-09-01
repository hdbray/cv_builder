#import pyperclip
import csv
import write_cv_main_functions as wc

#### grants and awards CV data

def compile_grants_awards(grants_awards_file, table_spacing,lwidth,rwidth):

    grants_awards_txt=wc.header_setup('Grants and Awards', table_spacing,lwidth,rwidth)
    grants_awards_dict=wc.convert_csv_to_dict(grants_awards_file,'Sorting Date')

    for i in range(len(grants_awards_dict)):
        row=grants_awards_dict[i]

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

        is_end=i==len(grants_awards_dict)-1

        if award_amt!='':
            award_amt='\$'+award_amt
            if note!='':
                note=award_amt+'. '+note
            else: 
                note=award_amt

        add_text=wc.create_table_entry(award_name,date,is_end,institution_name, '', note, description,False)

        grants_awards_txt=grants_awards_txt+add_text

    return grants_awards_txt


