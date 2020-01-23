import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad Text Editor')
main_application.wm_iconbitmap('icon.ico')

#todo############################# Main menu #############################
main_menu = tk.Menu()

#? file menu and icon
new_icon = tk.PhotoImage(file = 'icons2/new.png') # icon location
open_icon = tk.PhotoImage(file = 'icons2/open.png')
save_icon = tk.PhotoImage(file = 'icons2/save.png')
save_as_icon = tk.PhotoImage(file = 'icons2/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons2/exit.png')

file = tk.Menu(main_menu, tearoff = False)

#? Edit menu and icons
copy_icon = tk.PhotoImage(file = 'icons2/copy.png')
paste_icon = tk.PhotoImage(file = 'icons2/paste.png')
cut_icon = tk.PhotoImage(file = 'icons2/cut.png')
clear_all_icon = tk.PhotoImage(file = 'icons2/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons2/find.png')

edit = tk.Menu(main_menu, tearoff = False)

#? view menu and icons
tool_bar_icon = tk.PhotoImage(file = 'icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff = False)

#? color_theme menu and icons
light_default_icon = tk.PhotoImage(file = 'icons2/light_default.png') # color icons photo
light_plus_icon = tk.PhotoImage(file = 'icons2/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons2/dark.png')
red_icon = tk.PhotoImage(file = 'icons2/red.png')
monokai_icon = tk.PhotoImage(file = 'icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons2/night_blue.png')

theme_choice = tk.StringVar()

color_icons = (light_default_icon,light_plus_icon, dark_icon,red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default' : ('#000000','#ffffff'), #first: text color, last: background color
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

color_theme = tk.Menu(main_menu, tearoff = False)

#? about menue ***********
Help = tk.Menu(main_menu,tearoff = False)

#* cascade
main_menu.add_cascade(label = 'File', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'View', menu = view)
main_menu.add_cascade(label = 'Color Theme', menu = color_theme)
main_menu.add_cascade(label = 'Help',menu = Help)
#todo&&&&&&&&&&&&&&&&&&&&&&&&&& End main menu &&&&&&&&&&&&&&&&&&&&&&&&&&&&

#todo############################# Tool bar #############################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP, fill = tk.X) #pack muloto middel state ee thake. tai tk.x die etake north ee newa hoyese

#? font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0, column = 0, padx = 5)

#? size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,81,2))
font_size.current(2)
font_size.grid(row = 0, column = 1, padx = 5)

#? bold button
bold_icon = tk.PhotoImage(file = 'icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0, column = 2, padx = 5)

#? italic button
italic_icon = tk.PhotoImage(file = 'icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row = 0, column = 3, padx = 5)
#?underline button
underline_icon = tk.PhotoImage(file = 'icons2/underline.png')
underline_btn = tk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column = 4, padx = 5)
#? font color button
font_color_icon = tk.PhotoImage(file = 'icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0, column = 5, padx = 5)
#? align left
align_left_icon = tk.PhotoImage(file = 'icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image = align_left_icon)
align_left_btn.grid(row = 0, column = 6, padx = 5)
#? align center
align_center_icon = tk.PhotoImage(file = 'icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image = align_center_icon)
align_center_btn.grid(row = 0, column = 7, padx = 5)
#? align right
align_right_icon = tk.PhotoImage(file = 'icons2/align_right.png')
align_rigt_btn = ttk.Button(tool_bar, image = align_right_icon)
align_rigt_btn.grid(row = 0, column = 8, padx = 5)
#todo&&&&&&&&&&&&&&&&&&&&&&&&&& End Tool bar &&&&&&&&&&&&&&&&&&&&&&&&&&&&

#todo############################# Text editor #############################
text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word',relief = tk.FLAT) # wrap = word that meand, jokhon courser next line ee move korbe tokhon according to word move korbe. mane kono word lakher somoy curser next line ee chole gale full word ta next line ee chole jabe

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set() # courser line er surute dekhar jonno
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview) #scroll bar ta text editor er upar hobe seta bujanor jonno
text_editor.config(yscrollcommand = scroll_bar.set) # text editor horizontal hobe vertical hobena seta bujanor jonno

#! font family and font size functionality

current_font_family = 'Arial'
current_font_size = 12
text_editor.configure(font = ('Arial',12)) #ekhane defoult font and size eita thakbe

def change_font(event = None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))
font_box.bind('<<ComboboxSelected>>',change_font) #combobox ke text editor er sathe sonjog korar jonno bind kora hoyese

def change_font_size(event = None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family,current_font_size))
font_size.bind('<<ComboboxSelected>>',change_font_size)

#!#### Button functionality
#*print(tk.font.Font(font= text_editor['font']).actual()) # ekhane actual ekti dictionary return kore
#* output: {'family': 'Arial', 'size': 12, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
#* ekhane text editor er every details powa jay. etake kaje lagia amra button er kaj gulo korbo
######? bold button functionality
def change_bold():
    text_property = tk.font.Font(font= text_editor['font'])#Font-- eti ekti methode font class er
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font = (current_font_family, current_font_size, 'normal'))

bold_btn.configure(command = change_bold)

#######? italic button functionality
def change_italic():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_family,current_font_size, 'normal'))

italic_btn.configure(command = change_italic)

########? underline button functionality
def change_underline():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font = (current_font_family, current_font_size, 'normal'))

underline_btn.configure(command = change_underline)

#############? font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor() #* its return (((160.625, 160.625, 160.625), '#a0a0a0'))
    text_editor.configure(fg = color_var[1]) #* 0 number position ee RGB color and 1 number position ee amader selected color. ja rgb theke mix hoye toiri hoyese

font_color_btn.configure(command = change_font_color)

#! align functionality

##########? left
def align_left():
    text_content = text_editor.get(1.0,'end') # all text ekti variable ee store kora hoyse
    text_editor.tag_config('left',justify = tk.LEFT) # tag re config kore bole dewa hoyse je left ee kaj kora hobe
    text_editor.delete(1.0, tk.END) # text ke delete kora hoyese
    text_editor.insert(tk.INSERT, text_content, 'left') #text ke left ee insert kora hoyese
align_left_btn.configure(command = align_left)

#####? center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify= tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'center')
align_center_btn.configure(command = align_center)

#####? right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right',justify= tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'right')
align_rigt_btn.configure(command = align_right)

#todo&&&&&&&&&&&&&&&&&&&&&&&&&& End Text editor &&&&&&&&&&&&&&&&&&&&&&&&&&&&

#todo############################# status bar #############################
status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

text_changed = False
def changed(event = None):
    global text_changed
    if text_editor.edit_modified(): #check korbe amader text editor ee kisu wirte kora  hoyse kina
        text_changed = True
        words = len(text_editor.get(1.0,'end -1c').split()) # line end er por new line ee gele ekti extra word count hoy seta jage na hoy se jonno
        characters = len(text_editor.get(1.0,'end -1c'))
        status_bar.config(text = f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False) # ekbar modified hoye gale code 2nd time r chole na karon condition True hoye jay. tai code tike protibare chalanor jonno modifie ke false kora hoyse. jate protibar code ta run hoy

text_editor.bind('<<Modified>>', changed)

#todo&&&&&&&&&&&&&&&&&&&&&&&&&& End status bar &&&&&&&&&&&&&&&&&&&&&&&&&&&&

#todo############################# main menu functionality #############################

#! variable
url = '' #amader functionality er sob kaj ai url er maddome korte hobe. protibar url er directory chinta kore kaj koj korte hobe

#?### new functionality

def new_file(event = None):
    global url # it's means url variable ti je kono funtion er modde change kora jabe
    url = ''
    text_editor.delete(1.0, tk.END)
#* file commands
file.add_command(label = 'New', image = new_icon, compound = tk.LEFT, accelerator = 'Ctrl+N',command = new_file) # create drop down menu

#? open functionality
def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes = (('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END) #open korar somoy text file ee jodi kisu thake ta delete hoy jabe
            text_editor.insert(1.0,rf.read()) # 1.0 means first position theke url file ee ja ase sob insert kore dibe
    except FileNotFoundError: #! user jodi kono file select na kore ta hole ai rokom error aste pare
        return   # jodi ei error pay ta hole text editor je rokom ase se rokom ee thakbe
    except: # jodi onno kono error pay ta hole oo airokom thakbe
        return
    main_application.title(os.path.basename(url)) 
    
file.add_command(label = 'Open', image = open_icon, compound = tk.LEFT, accelerator = 'Ctrl+O',command = open_file)

########? save functionality

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension = '.txt', filetypes = (('Text File','*.txt'),('All Files','*.*')))
            content2 = str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label = 'Save', image = save_icon, compound = tk.LEFT, accelerator = 'Ctrl+S',command = save_file)

#####? save as funtionality
def save_as(event = None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w',defaultextension = '.txt', filetypes = (('Text File','*.txt'),('All Files','*.*')))
        content = str(text_editor.get(1.0,tk.END))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label = 'Save As', image = save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S',command = save_as)

########? Exit functionality
def exit_func(event = None):
    global text_changed, url
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                        main_application.destroy()
                else:
                    url = filedialog.asksaveasfile(mode='w',defaultextension = '.txt', filetypes = (('Text File','*.txt'),('All Files','*.*')))
                    content2 = str(text_editor.get(1.0,tk.END))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label = 'Exit', image = exit_icon, compound = tk.LEFT, accelerator = 'Ctrl+Q',command = exit_func)

#* edit commands find functionality
#########? find functionality

def find_func(event = None):
    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    def find(event = None):
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matchs = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matchs += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground = 'red', background = 'yellow')

    def replace(event = None):
        word = find_input.get()
        replace_item = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word,replace_item)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    ##? frame
    find_frame = ttk.LabelFrame(find_dialog,text = 'find/replace')
    find_frame.pack(pady = 20)

    ##? label
    text_find_label = ttk.Label(find_frame,text = 'Find')
    text_replace_label = ttk.Label(find_frame, text = 'Replace')

    ##? entry box
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30)

    ##? button
    find_button = ttk.Button(find_frame,text = 'Find',command = find)
    replace_button = ttk.Button(find_frame,text = 'Replace', command = replace)

    ##? label grid
    text_find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    text_replace_label.grid(row = 1, column = 0, padx = 4, pady = 4)

    ##? entry box grid
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)

    ##? button grid
    find_button.grid(row = 2, column = 0, padx = 8, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

    find_dialog.mainloop()
    
#* edit commands
edit.add_command(label = 'Copy', image = copy_icon, compound = tk.LEFT, accelerator = 'Ctrl+C',command = lambda: text_editor.event_generate('<Control c>'))
edit.add_command(label = 'Paste', image = paste_icon, compound = tk.LEFT, accelerator = 'Ctrl+V',command = lambda: text_editor.event_generate('<Control v>'))
edit.add_command(label = 'Cut', image = cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X',command =lambda: text_editor.event_generate('<Control x>'))
edit.add_command(label = 'Clear All', image = clear_all_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+X',command = lambda: text_editor.delete(1.0,tk.END))
edit.add_command(label = 'Find', image = find_icon, compound = tk.LEFT, accelerator = 'Ctrl+F',command = find_func)

#* view commands
#? viw commands functionality

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbal():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True
# ekhane jodi toolbar ke first ee pack kortam ta hole eta niche chole jeto tai age age starus bar text editor ke unpack koresi then toolbar ke top ee pack kora hoyse after sob guloke again repack kora hoyese
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True
#ekhane status bar sobar niche ase tai eke direct pack kora gase. karon jodi emnite kono kisu pack kora hoto ta hole seta niche ii jeto
#* view commands
view.add_checkbutton(label = 'Tool Bar',onvalue = True, offvalue = False, variable = show_toolbar, image = tool_bar_icon, compound = tk.LEFT,command = hide_toolbal)
view.add_checkbutton(label = 'Status Bar',onvalue = 1, offvalue = 0, variable = show_statusbar, image = status_bar_icon, compound = tk.LEFT,command = hide_statusbar) # 1,0 or true,false eki kotha

#* color theme commands
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background = bg_color, fg = fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice,compound = tk.LEFT,command = change_theme)
    count += 1

#* help command
#?####   welcome cmd
def welcome_func(event = None):
    mbox = messagebox.showinfo('Welcome','Welcome to Vpad Text Editor\n Start your writing \n Have a good day')

#???#### about cmd
def about_func(event = None):
    mbox = messagebox.showinfo('About','version : 0.01\ndate : 10-01-2020\npython: 3.7.4\nTkinter Application')

def developer_func():
    mbox = messagebox.showinfo('Developer','This app developed by\nMD.Mohiuddin Khan Akash\nStudent of Daffodil International University\nDepartment Of Computer Science And Engineering')

Help.add_command(label = 'Welcome',compound = tk.LEFT, command = welcome_func)
Help.add_separator()
Help.add_command(label = 'Developer',compound = tk.LEFT, command = developer_func)
Help.add_separator()
Help.add_command(label = 'About',compound = tk.LEFT, command = about_func)
#todo&&&&&&&&&&&&&&&&&&&&&&&&&& End main menu functionality &&&&&&&&&&&&&&&&&&&&&&&&&&&&

#*######  bind shortcut key
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', open_file)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-Alt-s>', save_as)
main_application.bind('<Control-f>', find_func)
main_application.bind('<Control-q>', exit_func)

main_application.config(menu = main_menu)
main_application.mainloop()