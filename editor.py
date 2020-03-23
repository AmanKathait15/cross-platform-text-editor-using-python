

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

copy_icon_path = '/home/aman/Desktop/text editor/icons2/copy.png'
cut_icon_path = '/home/aman/Desktop/text editor/icons2/cut.png'
paste_icon_path = '/home/aman/Desktop/text editor/icons2/paste.png'
clear_icon_path = '/home/aman/Desktop/text editor/icons2/clear_all.png'
find_icon_path = '/home/aman/Desktop/text editor/icons2/find.png'

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

copy_icon = tk.PhotoImage(file = copy_icon_path)
cut_icon = tk.PhotoImage(file = cut_icon_path)
paste_icon = tk.PhotoImage(file = paste_icon_path)
clear_icon = tk.PhotoImage(file = clear_icon_path)
find_icon = tk.PhotoImage(file = find_icon_path)


# to add drop down menu in file section

file.add_command(label = 'New', image = new_icon , compound = tk.LEFT , accelerator = 'Ctrl+n')
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

view.add_command(label = 'Copy', image = copy_icon , compound = tk.LEFT , accelerator = 'Ctrl+c')
view.add_command(label = 'Cut', image = cut_icon , compound = tk.LEFT , accelerator = 'Ctrl+x')
view.add_command(label = 'Paste', image = paste_icon , compound = tk.LEFT , accelerator = 'Ctrl+v')
view.add_command(label = 'Clear all', image = clear_icon , compound = tk.LEFT , accelerator = 'Ctrl+ALT+s')
view.add_command(label = 'Find', image = find_icon , compound = tk.LEFT , accelerator = 'Ctrl+q')

#############################################            #################################################

main_application.config(menu = main_menu)
main_application.mainloop()
