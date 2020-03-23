

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

# to add file icon

new_icon_path = '/home/aman/Desktop/text editor/icons2/new.png'
open_icon_path = '/home/aman/Desktop/text editor/icons2/open.png'
save_icon_path = '/home/aman/Desktop/text editor/icons2/save.png'
save_as_icon_path = '/home/aman/Desktop/text editor/icons2/save_as.png'
exit_icon_path = '/home/aman/Desktop/text editor/icons2/exit.png'

copy_icon_path = '/home/aman/Desktop/text editor/icons2/copy.png'
cut_icon_path = '/home/aman/Desktop/text editor/icons2/cut.png'
paste_icon_path = '/home/aman/Desktop/text editor/icons2/paste.png'
clear_icon_path = '/home/aman/Desktop/text editor/icons2/clear_all.png'
find_icon_path = '/home/aman/Desktop/text editor/icons2/find.png'

tool_bar_icon_path = '/home/aman/Desktop/text editor/icons2/tool_bar.png'
status_bar_icon_path = '/home/aman/Desktop/text editor/icons2/status_bar.png'

light_icon_path = '/home/aman/Desktop/text editor/icons2/light_default.png'
light_plus_icon_path = '/home/aman/Desktop/text editor/icons2/light_plus.png'
dark_icon_path = '/home/aman/Desktop/text editor/icons2/dark.png'
monokai_icon_path = '/home/aman/Desktop/text editor/icons2/monokai.png'
night_blue_icon_path = '/home/aman/Desktop/text editor/icons2/night_blue.png'

# variable holding image 

new_icon = tk.PhotoImage(file = new_icon_path)
open_icon = tk.PhotoImage(file = open_icon_path)
save_icon = tk.PhotoImage(file = save_icon_path)
save_as_icon = tk.PhotoImage(file = save_as_icon_path)
exit_icon = tk.PhotoImage(file = exit_icon_path)

copy_icon = tk.PhotoImage(file = copy_icon_path)
cut_icon = tk.PhotoImage(file = cut_icon_path)
paste_icon = tk.PhotoImage(file = paste_icon_path)
clear_icon = tk.PhotoImage(file = clear_icon_path)
find_icon = tk.PhotoImage(file = find_icon_path)

tool_bar_icon = tk.PhotoImage(file = tool_bar_icon_path)
status_bar_icon = tk.PhotoImage(file = status_bar_icon_path)

light_icon = tk.PhotoImage(file = light_icon_path)
light_plus_icon = tk.PhotoImage(file = light_plus_icon_path)
dark_icon = tk.PhotoImage(file = dark_icon_path)
monokai_icon = tk.PhotoImage(file = monokai_icon_path)
night_blue_icon = tk.PhotoImage(file = night_blue_icon_path)

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
