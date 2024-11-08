import csv
import write_cv_main_functions as wc

### service

def compile_referee(referee_file):

    referee_dict=wc.convert_csv_to_dict(referee_file)

    referee_txt='''\myheader{Referee Reports} 
    \medskip

    '''
    for i in range(len(referee_dict)-1):
        referee_txt+=(referee_dict[i]['Journal'])
        referee_txt+=', '

    referee_txt+=referee_dict[len(referee_dict)-1]['Journal']
    referee_txt+='.'





    return referee_txt

#
#
#
