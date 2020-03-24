

import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('pyeditor')

############################################## MAIN MENU #################################################

main_menu = tk.Menu()

#creating label of main menu

# tearoff = false so that drop down menu stick with its section user cannot move it 

file = tk.Menu(main_menu,tearoff=False)
edit = tk.Menu(main_menu,tearoff=False)
view = tk.Menu(main_menu,tearoff=False)
theme = tk.Menu(main_menu,tearoff=False)

#cascading label without it label are their but not show

main_menu.add_cascade(label = 'File', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'View', menu = view)
main_menu.add_cascade(label = 'Theme', menu = theme)

################################### icon path ############################################

############### file icon ##############

new_icon_path = '/home/aman/Desktop/text editor/icons2/new.png'
open_icon_path = '/home/aman/Desktop/text editor/icons2/open.png'
save_icon_path = '/home/aman/Desktop/text editor/icons2/save.png'
save_as_icon_path = '/home/aman/Desktop/text editor/icons2/save_as.png'
exit_icon_path = '/home/aman/Desktop/text editor/icons2/exit.png'

############### edit icon ##############

copy_icon_path = '/home/aman/Desktop/text editor/icons2/copy.png'
cut_icon_path = '/home/aman/Desktop/text editor/icons2/cut.png'
paste_icon_path = '/home/aman/Desktop/text editor/icons2/paste.png'
clear_icon_path = '/home/aman/Desktop/text editor/icons2/clear_all.png'
find_icon_path = '/home/aman/Desktop/text editor/icons2/find.png'

############### view icon ##############

tool_bar_icon_path = '/home/aman/Desktop/text editor/icons2/tool_bar.png'
status_bar_icon_path = '/home/aman/Desktop/text editor/icons2/status_bar.png'

############### theme icon ##############

light_icon_path = '/home/aman/Desktop/text editor/icons2/light_default.png'
light_plus_icon_path = '/home/aman/Desktop/text editor/icons2/light_plus.png'
dark_icon_path = '/home/aman/Desktop/text editor/icons2/dark.png'
monokai_icon_path = '/home/aman/Desktop/text editor/icons2/monokai.png'
night_blue_icon_path = '/home/aman/Desktop/text editor/icons2/night_blue.png'

############### button icon ##############

bold_icon_path = '/home/aman/Desktop/text editor/icons2/bold.png'
italic_icon_path = '/home/aman/Desktop/text editor/icons2/italic.png'
underline_icon_path = '/home/aman/Desktop/text editor/icons2/underline.png'
font_color_icon_path = '/home/aman/Desktop/text editor/icons2/font_color.png'
left_align_icon_path = '/home/aman/Desktop/text editor/icons2/align_left.png'
center_align_icon_path = '/home/aman/Desktop/text editor/icons2/align_center.png'
right_align_icon_path = '/home/aman/Desktop/text editor/icons2/align_right.png'

########################################## icon image ##################################################

############### file icon ##############

new_icon = tk.PhotoImage(file = new_icon_path)
open_icon = tk.PhotoImage(file = open_icon_path)
save_icon = tk.PhotoImage(file = save_icon_path)
save_as_icon = tk.PhotoImage(file = save_as_icon_path)
exit_icon = tk.PhotoImage(file = exit_icon_path)

############### edit icon ##############

copy_icon = tk.PhotoImage(file = copy_icon_path)
cut_icon = tk.PhotoImage(file = cut_icon_path)
paste_icon = tk.PhotoImage(file = paste_icon_path)
clear_icon = tk.PhotoImage(file = clear_icon_path)
find_icon = tk.PhotoImage(file = find_icon_path)

############### view icon ##############

tool_bar_icon = tk.PhotoImage(file = tool_bar_icon_path)
status_bar_icon = tk.PhotoImage(file = status_bar_icon_path)

############### theme icon ##############

light_icon = tk.PhotoImage(file = light_icon_path)
light_plus_icon = tk.PhotoImage(file = light_plus_icon_path)
dark_icon = tk.PhotoImage(file = dark_icon_path)
monokai_icon = tk.PhotoImage(file = monokai_icon_path)
night_blue_icon = tk.PhotoImage(file = night_blue_icon_path)

############### button icon ##############

bold_icon = tk.PhotoImage(file = bold_icon_path)
italic_icon = tk.PhotoImage(file = italic_icon_path)
underline_icon = tk.PhotoImage(file = underline_icon_path)
font_color_icon = tk.PhotoImage(file = font_color_icon_path)
left_align_icon = tk.PhotoImage(file = left_align_icon_path)
center_align_icon = tk.PhotoImage(file = center_align_icon_path)
right_align_icon = tk.PhotoImage(file = right_align_icon_path)

############### tool bar ##############

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP , fill = tk.X)

############### text editor ##############

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word' , relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT , fill = tk.Y)
text_editor.pack(fill = tk.BOTH , expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

############### status bar ##############

status_bar = ttk.Label(main_application, text = 'status bar')
status_bar.pack(side = tk.BOTTOM)

### font box ###

fonts = tk.font.families()
#print(fonts)
font_family = tk.StringVar()

font_box =ttk.Combobox(tool_bar , width = 30 , textvariable = font_family , state = 'readonly')
font_box['values'] = fonts

font_box.current(fonts.index('fixed'))
font_box.grid(row = 0, column = 0 , padx = 5)

### size box ###

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width = 14 , textvariable = size_var , state = 'readonly')

font_size['values'] = tuple(range(8,40,1))
font_size.current(4)	# at index 4 value in tuple is 12 i.e 12 id by deafult font size
font_size.grid(row = 0,  column = 1, padx = 5)

### bold button ###

bold_button = ttk.Button(tool_bar, image = bold_icon)
bold_button.grid(row = 0, column = 2, padx = 5)

### italic button ###

italic_button = ttk.Button(tool_bar, image = italic_icon)
italic_button.grid(row = 0, column = 3, padx = 5)

### underline button ###

underline_button = ttk.Button(tool_bar, image = underline_icon)
underline_button.grid(row = 0, column = 4, padx = 5)

### font color button ###

font_color_button = ttk.Button(tool_bar, image = font_color_icon)
font_color_button.grid(row = 0, column = 5, padx = 5)

### left align button ###

left_align_button = ttk.Button(tool_bar, image = left_align_icon)
left_align_button.grid(row = 0, column = 6, padx = 5)

### center align button ###

center_align_button = ttk.Button(tool_bar, image = center_align_icon)
center_align_button.grid(row = 0, column = 7, padx = 5)

### right align button ###

right_align_button = ttk.Button(tool_bar, image = right_align_icon)
right_align_button.grid(row = 0, column = 8, padx = 5)


################# adding functionality of font box and size box to text editor ############################3

current_font = 'fixed'
current_font_size = 12

def change_font(main_application):

	global current_font
	current_font = font_family.get()
	text_editor.configure(font = (current_font,current_font_size))

def change_font_size(event = None):		# one parameter we have to pas due to binding it can main_application also

	global current_font_size
	current_font_size = size_var.get()
	text_editor.configure(font = (current_font,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)

########## adding button functionality ###########

### bold button ###

def change_to_bold():

	text_property = tk.font.Font(font = text_editor['font'])
	#print(text_property.actual())
	if(text_property.actual()['weight']=='normal'):
		text_editor.configure(font = (current_font,current_font_size,'bold'))
	elif(text_property.actual()['weight']=='bold'):
		text_editor.configure(font = (current_font,current_font_size,'normal'))

bold_button.configure(command = change_to_bold)

### italic button ###

def change_to_italic():

	text_property = tk.font.Font(font = text_editor['font'])

	if(text_property.actual()['slant']=='roman'):
		text_editor.configure(font = (current_font,current_font_size,'italic'))
	elif(text_property.actual()['slant']=='italic'):
		text_editor.configure(font = (current_font,current_font_size,'roman'))

italic_button.configure(command = change_to_italic)

### underline button ###

def change_to_underline():

	text_property = tk.font.Font(font = text_editor['font'])

	if(text_property.actual()['underline']==0):
		text_editor.configure(font = (current_font,current_font_size,'underline'))
	elif(text_property.actual()['underline']==1):
		text_editor.configure(font = (current_font,current_font_size,'normal'))

underline_button.configure(command = change_to_underline)

text_editor.config(font = (current_font,current_font_size))

# to add drop down menu in file section

# compound is used so that label and icon not overlap with each other

file.add_command(label = 'New', image = new_icon ,compound = tk.LEFT , accelerator = 'Ctrl+n')
file.add_command(label = 'Open', image = open_icon , compound = tk.LEFT , accelerator = 'Ctrl+o')
file.add_command(label = 'Save', image = save_icon , compound = tk.LEFT , accelerator = 'Ctrl+s')
file.add_command(label = 'Save_as', image = save_as_icon , compound = tk.LEFT , accelerator = 'Ctrl+ALT+s')
file.add_command(label = 'Exit', image = exit_icon , compound = tk.LEFT , accelerator = 'Ctrl+q')

# to add drop down menu in edit section

edit.add_command(label = 'Copy', image = copy_icon , compound = tk.LEFT , accelerator = 'Ctrl+c')
edit.add_command(label = 'Cut', image = cut_icon , compound = tk.LEFT , accelerator = 'Ctrl+x')
edit.add_command(label = 'Paste', image = paste_icon , compound = tk.LEFT , accelerator = 'Ctrl+v')
edit.add_command(label = 'Clear all', image = clear_icon , compound = tk.LEFT , accelerator = 'Ctrl+ALT+s')
edit.add_command(label = 'Find', image = find_icon , compound = tk.LEFT , accelerator = 'Ctrl+q')

# to add drop down menu in view section

view.add_checkbutton(label = 'tool_bar', image = tool_bar_icon , compound = tk.LEFT , accelerator = 'Ctrl+c')
view.add_checkbutton(label = 'status_bar', image = status_bar_icon , compound = tk.LEFT , accelerator = 'Ctrl+x')

theme_choice = tk.StringVar()
color_icons = (light_icon,light_plus_icon,dark_icon,monokai_icon,night_blue_icon)

color_dict = {
	
	'light' : ('#000000' , '#ffffff'),
	'light plus' : ('#474747' , '#e0e0e0'),
	'dark' : ('#e4e4e4' , '#ffe8e8'),
	'monokai' : ('#ededed' , '#6b9dc2'),
	'night_blue' : ('#2d2d2d' , 'ffe8e8'),
}
count = 0
for key in color_dict:
	theme.add_radiobutton(label = key, image = color_icons[count] , variable = theme_choice , compound = tk.LEFT)
	count+=1

#############################################            #################################################

main_application.config(menu = main_menu)
main_application.mainloop()
