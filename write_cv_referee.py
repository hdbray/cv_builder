import csv
import write_cv_main_functions as wc

### service

def compile_referee(referee_file):

    referee_dict=wc.convert_csv_to_dict(referee_file)

#    print(referee_dict)

    track_referee_repeats={}

    for entry in referee_dict:
        journal_key=entry['Journal']
        service_key=entry['Service (quick opinion, full report)']
        if service_key=='full report':
            if journal_key in track_referee_repeats:
                journal_value=track_referee_repeats[journal_key]
                journal_value+=1
                track_referee_repeats.update({journal_key:journal_value})
            else:
                track_referee_repeats.update({journal_key:1})

#    print(track_referee_repeats)

    referee_txt='''\myheader{Referee Reports} 
    \medskip

    '''
    for journal_key in track_referee_repeats:
        journal_value=track_referee_repeats[journal_key]
        if journal_value>1: 
            referee_txt+=journal_key+' (%s)'% (journal_value)
            referee_txt+=', '
        else: 
            referee_txt+=journal_key+', '
        
    referee_txt=referee_txt[:-2]+'.'

#    print(referee_txt)



#    for i in range(len(referee_dict)-1):
#        referee_txt+=(referee_dict[i]['Journal'])
#        referee_txt+=', '
#
#    referee_txt+=referee_dict[len(referee_dict)-1]['Journal']
#    referee_txt+='.'






    return referee_txt

#compile_referee('csv_files/referee.csv')

#
#
#
