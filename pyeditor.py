

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

new_icon_path = 'new.png'
open_icon_path = 'open.png'
save_icon_path = 'save.png'
save_as_icon_path = 'save_as.png'
exit_icon_path = 'exit.png'

############### edit icon ##############

copy_icon_path = 'copy.png'
cut_icon_path = 'cut.png'
paste_icon_path = 'paste.png'
clear_icon_path = 'clear_all.png'
find_icon_path = 'find.png'

############### view icon ##############

tool_bar_icon_path = 'tool_bar.png'
status_bar_icon_path = 'status_bar.png'

############### theme icon ##############

light_icon_path = 'light_default.png'
light_plus_icon_path = 'light_plus.png'
dark_icon_path = 'dark.png'
monokai_icon_path = 'monokai.png'
red_icon_path = 'red.png'
night_blue_icon_path = 'night_blue.png'

############### button icon ##############

bold_icon_path = 'bold.png'
italic_icon_path = 'italic.png'
underline_icon_path = 'underline.png'
font_color_icon_path = 'font_color.png'
left_align_icon_path = 'align_left.png'
center_align_icon_path = 'align_center.png'
right_align_icon_path = 'align_right.png'

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
red_icon = tk.PhotoImage(file = red_icon_path)
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

#### adding status bar functionality ####

text_change = 0

def text_modified(event = None):

	if(text_editor.edit_modified()):

		global text_change 
		text_change = 1
		text = text_editor.get(1.0,'end-1c')		## end-1c mean exluding 1 character i.e '\n'
		no_of_char = len(text)
		words = text.split()
		no_of_words = len(words)

		status_bar.config(text = f'no of character : {no_of_char} no of words : {no_of_words}')

	text_editor.edit_modified(False) 	# to change status bar when text is modified

text_editor.bind('<<Modified>>',text_modified)

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

### font color ###

def change_font_color():

	color_var = tk.colorchooser.askcolor()
	text_editor.configure(fg = color_var[1]) 	## 0 index for RGB and 1 for hexcode

font_color_button.configure(command = change_font_color)

### adding alignment functionality ###

def left_align():

	text_content = text_editor.get(1.0,'end')
	text_editor.tag_config('left',justify = tk.LEFT)
	text_editor.delete(1.0,'end')
	text_editor.insert(tk.INSERT , text_content , 'left')

left_align_button.configure(command = left_align)

def center_align():

	text_content = text_editor.get(1.0,'end')
	text_editor.tag_config('center',justify = tk.CENTER)
	text_editor.delete(1.0,'end')
	text_editor.insert(tk.INSERT , text_content , 'center')

center_align_button.configure(command = center_align)

def right_align():

	text_content = text_editor.get(1.0,'end')
	text_editor.tag_config('right',justify = tk.RIGHT)
	text_editor.delete(1.0,'end')
	text_editor.insert(tk.INSERT , text_content , 'right')

right_align_button.configure(command = right_align)

text_editor.config(font = (current_font,current_font_size))

# to add drop down menu in file section

# compound is used so that label and icon not overlap with each other

url = ''

def new_file(event = None):
	global url,text_change
	try:
		if text_change:
			text_change = 0
			mbox = messagebox.askyesno('warning','Do you want to save this file')
			if mbox:
				if url:
					content = str(text_editor.get(1.0,tk.END))
					with open(url , 'w', encoding='utf-8') as fw:
						fw.write(content)
				else:
					url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
					content2 = str(text_editor.get(1.0,tk.END))
					url.write(content)
					url.close()
	except:
		return
	url=''
	text_editor.delete(1.0,tk.END)

def open_file(event = None):
	global url,text_change
	url = filedialog.askopenfilename(initialdir = os.getcwd(), title='select file', filetypes = (('Text File','*.txt'),('All Files','*.*')))
	try:
		with open(url,'r') as fr:
			text_editor.delete(1.0,tk.END)
			text_editor.insert(1.0,fr.read())
	except FileNotFoundError:
		return
	except:
		return
	text_change = 0
	main_application.title(os.path.basename(url))

def save_file(event = None):
	global url,text_change
	try:
		text_change = 0
		if url:
			content = str(text_editor.get(1.0,tk.END))
			with open(url , 'w', encoding='utf-8') as fw:
				fw.write(content)
		else:
			url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
			content2 = str(text_editor.get(1.0,tk.END))
			url.write(content)
			url.close()
	except:
		return

def save_file_as(event = None):
	global url,text_change
	try:
		text_change = 0
		url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
		content = text_editor.get(1.0,tk.END)
		url.write(content)
		url.close()
	except:
		return

def exit_func(event = None):
	global url,text_change

	try:
		if text_change:
			mbox = messagebox.askyesnocancel('warning','Do you want to save file ?')

			if mbox is True:

				if url:
					content = str(text_editor.get(1.0,tk.END))
					with open(url , 'w', encoding='utf-8') as fw:
						fw.write(content)
				else:
					url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
					content2 = str(text_editor.get(1.0,tk.END))
					url.write(content)
					url.close()

			elif mbox is False:
				main_application.destroy()
		else:
			main_application.destroy()
	except:
		return


######### adding find functionality #################3

def find_func(event = None):

	def find():
		word = find_input.get()
		text_editor.tag_remove('match','1.0',tk.END)
		matches = 0
		if word:
			start_pos = '1.0'
			while True:
				start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
				if not start_pos:
					break
				end_pos = f'{start_pos}+{len(word)}c'

				text_editor.tag_add('match',start_pos,end_pos)
				matches+=1
				start_pos = end_pos
				text_editor.tag_config('match',foreground = 'red',background = 'yellow')

	def replace():
		
		word = find_input.get()
		replace_text = replace_input.get()
		content = text_editor.get(1.0,tk.END)
		new_content = content.replace(word,replace_text)
		text_editor.delete(1.0,tk.END)
		text_editor.delete(1.0,tk.END)
		text_editor.insert(1.0,new_content)

	find_dialogue = tk.Toplevel()
	find_dialogue.geometry('450x250+500+200')
	find_dialogue.title('Find')
	find_dialogue.resizable(0,0)

	#frame

	find_frame = ttk.LabelFrame(find_dialogue,text='Find/Replace')
	find_frame.pack(pady = 20)

	#labels
	text_find_label = ttk.Label(find_frame,text='Find :')
	text_replace_label = ttk.Label(find_frame , text = 'Replace :')

	#entry
	find_input = ttk.Entry(find_frame,width = 30)
	replace_input = ttk.Entry(find_frame,width = 30)

	#button
	find_button = ttk.Button(find_frame,text='Find',command=find)
	replace_button = ttk.Button(find_frame,text='Replace',command=replace)

	#label grid
	text_find_label.grid(row=0,column=0,padx=4,pady=4)
	text_replace_label.grid(row=1,column=0,padx=4,pady=4)

	#entry grid
	find_input.grid(row=0,column=1,padx=4,pady=4)
	replace_input.grid(row=1,column=1,padx=4,pady=4)

	#button grid
	find_button.grid(row=2,column=0,padx=8,pady=4)
	replace_button.grid(row=2,column=1,padx=8,pady=4)

	find_dialogue.mainloop()

file.add_command(label = 'New', image = new_icon ,compound = tk.LEFT , accelerator = 'Ctrl+n' , command = new_file)
file.add_command(label = 'Open', image = open_icon , compound = tk.LEFT , accelerator = 'Ctrl+o' , command = open_file)
file.add_command(label = 'Save', image = save_icon , compound = tk.LEFT , accelerator = 'Ctrl+s' , command = save_file)
file.add_command(label = 'Save_as', image = save_as_icon , compound = tk.LEFT , accelerator = 'Ctrl+ALT+s', command = save_file_as)
file.add_command(label = 'Exit', image = exit_icon , compound = tk.LEFT , accelerator = 'Ctrl+q',command = exit_func)

# to add drop down menu in edit section

edit.add_command(label = 'Copy', image = copy_icon , compound = tk.LEFT , accelerator = 'Ctrl+c',command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = 'Cut', image = cut_icon , compound = tk.LEFT , accelerator = 'Ctrl+x',command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = 'Paste', image = paste_icon , compound = tk.LEFT , accelerator = 'Ctrl+v',command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = 'Clear all', image = clear_icon , compound = tk.LEFT , accelerator = 'Ctrl+ALT+x',command = lambda:text_editor.event_generate("<Control Alt x>"))
edit.add_command(label = 'Find', image = find_icon , compound = tk.LEFT , accelerator = 'Ctrl+q',command = find_func)

# to add drop down menu in view section

show_tool_bar = tk.BooleanVar()
show_status_bar = tk.BooleanVar()

show_tool_bar.set(True)
show_status_bar.set(True)

###### adding toolbar functionality ######

def hide_tool_bar():

	global show_tool_bar,show_status_bar
	if show_tool_bar:
		tool_bar.pack_forget()
		show_tool_bar=False
	else:
		text_editor.pack_forget()
		if show_status_bar:
			status_bar.pack_forget()
		tool_bar.pack(side=tk.TOP,fill=tk.X)
		text_editor.pack(fill=tk.BOTH,expand=True)
		if show_status_bar:
			status_bar.pack(side=tk.BOTTOM)
		show_tool_bar=True

def hide_status_bar():

	global show_status_bar

	if show_status_bar:
		status_bar.pack_forget()
		show_status_bar=False
	else:
		status_bar.pack(side=tk.BOTTOM)
		show_status_bar=True


view.add_checkbutton(label = 'tool_bar',onvalue=1,offvalue=0,variable=show_tool_bar, image = tool_bar_icon , compound = tk.LEFT ,command = hide_tool_bar)
view.add_checkbutton(label = 'status_bar',onvalue=1,offvalue=0,variable=show_status_bar, image = status_bar_icon , compound = tk.LEFT,command = hide_status_bar)

theme_choice = tk.StringVar()
color_icons = (light_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

######## adding theme functionality ##########

def change_theme():

	chosen_theme = theme_choice.get()
	color_tuple = color_dict.get(chosen_theme)

	fg_color,bg_color = color_tuple[0],color_tuple[1]

	text_editor.config(bg=bg_color , fg = fg_color)

color_dict = {
	
	'light' : ('#000000' , '#ffffff'),
	'light plus' : ('#474747' , '#e0e0e0'),
	'dark' : ('#e4e4e4' , '#2d2d2d'),
	'red'  : ('#2d2d2d','#ffe8e8'),
	'monokai' : ('#ffaeff' , '#474747'),
	'night_blue' : ('#ededed' , '#6b9dc2'),
}
count = 0
for key in color_dict:
	theme.add_radiobutton(label = key, image = color_icons[count] , variable = theme_choice , compound = tk.LEFT , command = change_theme)
	count+=1

main_application.bind(("<Control-n>"),new_file)
main_application.bind(("<Control-o>"),open_file)
main_application.bind(("<Control-s>"),save_file)
main_application.bind(("<Control-Alt-s>"),save_file_as)
main_application.bind(("<Control-q>"),exit_func)
main_application.bind(("<Control-f>"),find_func)


#############################################            #################################################

main_application.config(menu = main_menu)
main_application.mainloop()
