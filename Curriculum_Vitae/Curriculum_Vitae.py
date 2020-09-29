"""
Summary:

Here we run all functions.
Runs only one classifier and does a cross-validation(k=2).
"""

import re

# Header
Header = 'I used Python to entirely generated this resume. You can find the full source code on my GitHub.'
Name = 'Name'
Title = 'Title'
Resume_Objective = 'Recent graduate ... '

# Picture
Picture = True
Picture_Path = 'picture_example.png'

# QR-Code
QR = True
QR_Path = 'qr_code_example.png'

# Contacts
Address = 'Street'
Phone = 'Number'
Email= 'E-Mail'
Website = 'Website'
Personal_info = [Address, Phone, Email, Website]

# Skills
Skills_Desc = ['Skill 1',
              'Skill 2',
              'Important Skill',
              'Very Important Skill',
              'Is That Even A Skill?',
              'Forgot About This',
              'Active Learning',
              'Python']

# Languages
Languages_List = ['Language 1', 'Language 2']
Languages_Desc = ['Native Speaker',
                  'Fluent']


CodeTitle = 'View Portfolio'

# Paragraph 1
Education_Header = 'EDUCATION'
Education_Titles = ['University ..., MSc in ...',
                    'University ..., BSc in ...']
Education_Dates = ['2016 - 2019', '2011 - 2017']
Education_Texts = ['Final grade: Best\nRelevant Coursework:\n- Course 1\n- Course 2\n- Course 3',
                   'Final grade: Best']

# Paragraph 2
Work_Header = 'WORK EXPERIENCE'
Work_Titles = ['Internship']
Work_Dates = ['2019 - present']
Work_Texts = ['I did important stuff there.']

# Paragraph 3
Projects_Header = 'PROJECTS'
Project_Titles = ['Project I',
                  'Project II',
                  'Project III',
                  'Currently working on ...']
Project_Dates = ['2013 - 2016', '2016 - 2019', '2019 - 2020', '2020 - present']
Project_Texts = ['- Summary of project',
                 '- Summary of project',
                 '- Summary of project',
                 '']

# Global parameters
box_gap = .045

def box(lower_left_coordinate, upper_right_coordinate=(.99, 1), color_preset='#000000', alpha_preset=.5):
    box_width = upper_right_coordinate[0] - lower_left_coordinate[0]
    box_height = upper_right_coordinate[1] - lower_left_coordinate[1]
    ax.add_patch(matplotlib.patches.Rectangle(lower_left_coordinate, box_width, box_height, color=color_preset, alpha=alpha_preset))

# def project_icon(x_coordinate, y_coordinate, size):
#     ax.text(x_coordinate + 0.005, y_coordinate, symbol_dic["clipboard"], fontproperties=fp_solid, size=size)
#     ax.text(x_coordinate + 0.0051, y_coordinate + 0.002, symbol_dic["lightbulb"], fontproperties=fp_solid, size=size-5, color='white')
#     ax.text(x_coordinate + 0.012, y_coordinate, symbol_dic["cogs"], fontproperties=fp_solid, size=size-7, color='white')

def header(headline, name, title):
    # Left side
    ax.text(.15, .975, symbol_dic["python"], fontproperties=fp_regu, size=8)
    plt.annotate(headline, (.5, .975), weight='regular', fontsize=8, alpha=.8, color='#ffffff', ha='center')
    ax.text(.83, .975, symbol_dic["git"], fontproperties=fp_regu, size=8)
    plt.annotate(name, (.5, .935), weight='bold', fontsize=20, color='#ffffff', ha='center')
    plt.annotate(title, (.5, .910), weight='regular', fontsize=12, color='#ffffff', ha='center')
    box(lower_left_coordinate=(.02, .9), upper_right_coordinate=(.99, .99), color_preset='#00608e')
    box(lower_left_coordinate=(.02, .9675), upper_right_coordinate=(.99, .99), color_preset='#003955')
    # Intro
    ax.text(.02, .875, Resume_Objective, ha='left', va="top", weight='regular', fontsize=8, wrap=True)
    return (.02, .875 - .04 - .02*Resume_Objective.count("\n"))

def contact_box(personal_info, y_start=.8565):
    # Right Side
    text_gap = .0145
    info_gap = .0205
    plt.annotate('Personal Information', (.7, y_start), weight='bold', fontsize=10, color='#ffffff')
    box(lower_left_coordinate=(.675, y_start - .007), upper_right_coordinate=(.99, y_start + 0.02),
        color_preset='#003955')
    y_current = y_start - .022
    plt.annotate('Address', (.725, y_current), weight='bold', fontsize=8, color='#ffffff')
    ax.text(.7, y_current, symbol_dic["address_card"], fontproperties=fp_solid, size=8)
    y_current = y_current - text_gap*(1+personal_info[0].count("\n"))
    plt.annotate(personal_info[0], (.7, y_current), weight='regular', fontsize=8, color='#ffffff')
    y_current = y_current - info_gap
    plt.annotate('Phone', (.725, y_current), weight='bold', fontsize=8, color='#ffffff')
    ax.text(.7, y_current, symbol_dic["phone"], fontproperties=fp_solid, size=8)
    y_current = y_current - text_gap*(1+personal_info[1].count("\n"))
    plt.annotate(personal_info[1], (.7, y_current), weight='regular', fontsize=8, color='#ffffff')
    y_current = y_current - info_gap
    plt.annotate('E-mail', (.725, y_current), weight='bold', fontsize=8, color='#ffffff')
    ax.text(.7, y_current, symbol_dic["email"], fontproperties=fp_solid, size=8)
    y_current = y_current - text_gap*(1+personal_info[2].count("\n"))
    plt.annotate(personal_info[2], (.7, y_current), weight='regular', fontsize=8, color='#ffffff')
    y_current = y_current - info_gap
    plt.annotate('Website', (.725, y_current), weight='bold', fontsize=8, color='#ffffff')
    ax.text(.7, y_current, symbol_dic["git"], fontproperties=fp_regu, size=8)
    y_current = y_current - text_gap*(1+personal_info[3].count("\n"))
    plt.annotate(personal_info[3], (.7, y_current), weight='regular', fontsize=8, color='#ffffff')
    box(lower_left_coordinate=(.675, y_current - .015), upper_right_coordinate=(.99, y_start + 0.02), color_preset='#00608e')
    return y_current - box_gap

def skill_box(skill_info, y_start=.642):
    line_gap = .03
    skill_gap = .03
    length_scale = .007
    space_scale = 0
    cap_spacing = .007
    plt.annotate('Skills', (.7, y_start), weight='bold', fontsize=10, color='#ffffff')
    box(lower_left_coordinate=(.675, y_start - .007), upper_right_coordinate=(.99, y_start + 0.02),
        color_preset='#003955')
    y_current = y_start - line_gap
    x_current = .7
    length_counter = 0
    skill_line_counter = 0
    for skill_index , skill in enumerate(Skills_Desc):
        if len(skill) > 50:
            break
        else:
            skill_line_counter += 1
            length_counter += len(skill)
            if skill_index == 0:
                x_current = .7
            else:
                x_current += skill_gap + length_scale*len(Skills_Desc[skill_index-1]) + space_scale*Skills_Desc[skill_index-1].count(' ') + cap_spacing*len(re.findall(r'[A-Z]', Skills_Desc[skill_index-1]))
            if ((length_counter >= 32) | (skill_line_counter > 3)):
                y_current -= line_gap
                x_current = .7
                length_counter = len(skill)
                skill_line_counter = 0
            plt.annotate(skill, (x_current, y_current), weight='regular', fontsize=8, color='#ffffff', backgroundcolor='#00608e')
    box(lower_left_coordinate=(.675, y_current - .015), upper_right_coordinate=(.99, y_start+0.02), color_preset='#00608e')
    return y_current - box_gap

def language_box(language_list, languages_desc, y_start=.2835):
    line_gap = .025
    plt.annotate('Languages', (.7, y_start), weight='bold', fontsize=10, color='#ffffff')
    box(lower_left_coordinate=(.675, y_start - .007), upper_right_coordinate=(.99, y_start + 0.02),
        color_preset='#003955')
    y_current = y_start - line_gap
    x_current = .7
    for language_index, language in enumerate(language_list):
            plt.annotate(language, (x_current, y_current), weight='regular', fontsize=8, color='#ffffff')
            plt.annotate(languages_desc[language_index], (x_current + 0.1, y_current), weight='regular', fontsize=8, color='#ffffff')
            if language_index + 1 < len(language_list):
                y_current -=  line_gap
    box(lower_left_coordinate=(.675, y_current - .01), upper_right_coordinate=(.99, y_start+0.02), color_preset='#00608e')
    return y_current - box_gap

def paragraph(headline, subheaders, dates, texts, start_coordinate=(.02, .86), symbol=False):
    plt.axhline(y=start_coordinate[1] + .017, xmin=.02, xmax=.66, color='#004A6F', linewidth=.5)
    if symbol:
        if symbol == 'project_icon':
            project_icon(start_coordinate[0], start_coordinate[1], size=10)
        else:
            ax.text(start_coordinate[0], start_coordinate[1], symbol_dic[symbol], fontproperties=fp_solid, size=10)
        shift_coordinate = (start_coordinate[0] + 0.025, start_coordinate[1])
        plt.annotate(headline, shift_coordinate, weight='bold', fontsize=10, color='#004A6F')
    else:
        plt.annotate(headline, start_coordinate, weight='bold', fontsize=10, color='#004A6F')
    plt.axhline(y=start_coordinate[1]-.007, xmin=.02, xmax=.66, color='#004A6F', linewidth=.5)
    last_coordinate = start_coordinate[1] - .028
    for title_index, title in enumerate(subheaders):
        date_coordinate = (start_coordinate[0], last_coordinate)
        plt.annotate(dates[title_index], date_coordinate, weight='bold', fontsize=10)
        last_coordinate = last_coordinate - 0.0175*title.count("\n")
        title_coordinate = (start_coordinate[0] + .142, last_coordinate)
        plt.annotate(title, title_coordinate, weight='bold', fontsize=10)
        text_coordinate = (title_coordinate[0] + .02, last_coordinate - 0.0155*(1+texts[title_index].count("\n")))
        plt.annotate(texts[title_index], text_coordinate, weight='regular', fontsize=9)
        last_coordinate = text_coordinate[1] - 0.04
    return (start_coordinate[0], last_coordinate-0.05)

# Imports
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# load symbols
fp_solid = matplotlib.font_manager.FontProperties(fname=r"C:\Windows\Fonts\Font Awesome 5 Free-Solid-900.otf")
fp_regu = matplotlib.font_manager.FontProperties(fname=r"C:\Windows\Fonts\Font Awesome 5 Brands-Regular-400.otf")

symbol_dic = dict(address_card = "\uf2bb",
                  phone = "\uf095",
                  email = "\uf0e0",
                  git = "\uf09b",
                  graduate = "\uf501",
                  lightbulb = "\uf0eb",
                  cogs = "\uf085",
                  clipboard = "\uf328",
                  work = "\uf0b1",
                  python = "\uf3e2")

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# Display everything
new_coordinate = header(Header, Name, Title)
# Picture
if Picture:
    qr_code_image = mpimg.imread(Picture_Path)
    image_box = OffsetImage(qr_code_image, zoom=.2)
    ab = AnnotationBbox(image_box, (.8375, .88))
    ax.add_artist(ab)
    new_y = .76
else:
    new_y = .8565
# Important Infos
new_y= contact_box(Personal_info, y_start=new_y)
new_y = skill_box(Skills_Desc, y_start=new_y)
new_y = language_box(Languages_List, Languages_Desc, y_start=new_y)
new_coordinate = paragraph(Education_Header, Education_Titles, Education_Dates, Education_Texts, symbol='graduate', start_coordinate=new_coordinate)
new_coordinate = paragraph(Work_Header, Work_Titles, Work_Dates, Work_Texts, symbol='work',  start_coordinate=new_coordinate)
new_coordinate = paragraph(Projects_Header, Project_Titles, Project_Dates, Project_Texts, symbol='clipboard',  start_coordinate=new_coordinate)
# QR Code
if QR:
    qr_code_image = mpimg.imread(QR_Path)
    if Picture:
        image_box = OffsetImage(qr_code_image, zoom=.15)
        plt.annotate(CodeTitle, (.8375, .125), weight='bold', fontsize=10, ha='center')
        ab = AnnotationBbox(image_box, (.8375, .06))
    else:
        image_box = OffsetImage(qr_code_image, zoom=.25)
        plt.annotate(CodeTitle, (.8375, .2), weight='bold', fontsize=10, ha='center')
        ab = AnnotationBbox(image_box, (.8375, .1))
    ax.add_artist(ab)

plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')
plt.savefig('resumeexample.pdf', dpi=300, bbox_inches='tight')