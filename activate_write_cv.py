import write_cv_academic_positions as wc_positions
import write_cv_education as wc_education
import write_cv_grants_awards as wc_grants_awards
import write_cv_pedagogical_training as wc_pedagogical_training
import write_cv_publications as wc_publications
import write_cv_talks_visits as wc_talks_visits
import write_cv_mentoring as wc_mentoring
import write_cv_teaching as wc_teaching
import write_cv_service as wc_service


default_table_spacing=1.5
thin_table_spacing=1.2

default_full_table_width=.9
default_lwidth=.1
default_rwidth=default_full_table_width-default_lwidth

thin_lwidth=.05
thin_rwidth=default_full_table_width-thin_lwidth

thick_lwidth=.2
thick_rwidth=default_full_table_width-thick_lwidth

### write publications tex file 

prefix='publications'
publications_file='csv_files/'+prefix+'.csv'
publications_tex='tex_files/'+prefix+'.tex'

publications_text_for_tex=wc_publications.compile_publications(publications_file,default_table_spacing, thin_lwidth,thin_rwidth)

with open(publications_tex, 'w') as write_file:
    write_file.write(publications_text_for_tex)


#### write grants_awards tex file

prefix='grants_awards'
grants_awards_file='csv_files/'+prefix+'.csv'
grants_awards_tex='tex_files/'+prefix+'.tex'

table_spacing=default_table_spacing

grants_awards_text_for_tex=wc_grants_awards.compile_grants_awards(grants_awards_file,table_spacing,default_lwidth,default_rwidth)

with open(grants_awards_tex, 'w') as write_file:
    write_file.write(grants_awards_text_for_tex)


#### write positions tex file

prefix='positions'
positions_file='csv_files/'+prefix+'.csv'
positions_tex='tex_files/'+prefix+'.tex'

table_spacing=default_table_spacing

positions_text_for_tex=wc_positions.compile_positions(positions_file,table_spacing,thick_lwidth,thick_rwidth)

with open(positions_tex, 'w') as write_file:
    write_file.write(positions_text_for_tex)


#### write education tex file

prefix='education'
education_file='csv_files/'+prefix+'.csv'
education_tex='tex_files/'+prefix+'.tex'

table_spacing=default_table_spacing

education_text_for_tex=wc_education.compile_education(education_file,table_spacing,thick_lwidth,thick_rwidth)

with open(education_tex, 'w') as write_file:
    write_file.write(education_text_for_tex)

#### write talks_visits tex file

prefix='talks_visits'
talks_visits_file='csv_files/'+prefix+'.csv'
talks_visits_tex='tex_files/'+prefix+'.tex'

table_spacing=default_table_spacing

talks_visits_text_for_tex=wc_talks_visits.compile_talks_visits(talks_visits_file,table_spacing,thick_lwidth,thick_rwidth)

with open(talks_visits_tex, 'w') as write_file:
    write_file.write(talks_visits_text_for_tex)

#### write mentoring tex file

prefix='mentoring'
mentoring_file='csv_files/'+prefix+'.csv'
mentoring_tex='tex_files/'+prefix+'.tex'

table_spacing=default_table_spacing

mentoring_text_for_tex=wc_mentoring.compile_mentoring(mentoring_file,table_spacing,thick_lwidth,thick_rwidth)

with open(mentoring_tex, 'w') as write_file:
    write_file.write(mentoring_text_for_tex)

#### write service tex file

prefix='service'
service_file='csv_files/'+prefix+'.csv'
service_tex='tex_files/'+prefix+'.tex'

table_spacing=thin_table_spacing

service_text_for_tex=wc_service.compile_service(service_file,table_spacing,thick_lwidth,thick_rwidth)

with open(service_tex, 'w') as write_file:
    write_file.write(service_text_for_tex)


#### write pedagogical_training tex file

prefix='pedagogical_training'
pedagogical_training_file='csv_files/'+prefix+'.csv'
pedagogical_training_tex='tex_files/'+prefix+'.tex'

table_spacing=thin_table_spacing

pedagogical_training_text_for_tex=wc_pedagogical_training.compile_pedagogical_training(pedagogical_training_file,table_spacing,thick_lwidth,thick_rwidth)

with open(pedagogical_training_tex, 'w') as write_file:
    write_file.write(pedagogical_training_text_for_tex)



#### write teaching tex file

prefix='teaching'
teaching_file='csv_files/'+prefix+'.csv'
teaching_tex='tex_files/'+prefix+'.tex'

table_spacing=thin_table_spacing

teaching_text_for_tex=wc_teaching.compile_teaching(teaching_file,table_spacing,default_lwidth,default_rwidth)

with open(teaching_tex, 'w') as write_file:
    write_file.write(teaching_text_for_tex)


