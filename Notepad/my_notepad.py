

from mailbox import mbox
from pickle import TRUE
import tkinter as tk
from tkinter import  ttk
from tkinter import  font,colorchooser, filedialog,messagebox
import os
main_application=tk.Tk()
main_application.geometry("800x600")
main_application.title("My notepad")
main_menu =  tk.Menu()


file= tk.Menu(main_menu,tearoff= False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
colour_theme=tk.Menu(main_menu,tearoff=False)
theme_choose= tk.StringVar()

main_menu.add_cascade(label="File",menu= file)
main_menu.add_cascade(label="Edit",menu= edit)
main_menu.add_cascade(label="View",menu= view)
main_menu.add_cascade(label="Colour Theme",menu= colour_theme)

tool_bar_label=ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

font_tuple= tk.font.families()
font_family= tk.StringVar()
font_box =ttk.Combobox(tool_bar_label,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5,pady=5)
#size box
size_variable= tk.IntVar()
font_size=ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state="readonly")
font_size["values"]= tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)
#bold button
bold_icon=tk.PhotoImage(file="icons/bold.png")
bold_btn=ttk.Button(tool_bar_label,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#italic button
italic_icon=tk.PhotoImage(file="icons/italic.png")
italic_btn=ttk.Button(tool_bar_label,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#underline button
underline_icon=tk.PhotoImage(file="icons/underline.png")
underline_btn=ttk.Button(tool_bar_label,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#font colour button
font_colour_icon=tk.PhotoImage(file="icons/font_colour.png")
font_colour_btn=ttk.Button(tool_bar_label,image=font_colour_icon)
font_colour_btn.grid(row=0,column=5,padx=5)
#align left
align_left_icon=tk.PhotoImage(file="icons/align_left.png")
align_left_btn=ttk.Button(tool_bar_label,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
#align center
align_center_icon=tk.PhotoImage(file="icons/align_center.png")
align_center_btn=ttk.Button(tool_bar_label,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
#align right
align_right_icon=tk.PhotoImage(file="icons/align_right.png")
align_right_btn=ttk.Button(tool_bar_label,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
#text editor
text_editor= tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill= tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command= text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#status bar word and character count
status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_change = False
def change_word(main_application = None):
    global text_change
    if text_editor.edit_modified():
        text_change= True
        word = len(text_editor.get(1.0,"end-1c").split())
        character= len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bar.config(text = f"character :{character}  word :{word}")               
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change_word)
#font family and function
font_now= "Arial"
font_size_now = 16

def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now,font_size_now))
    
def change_size(main_application):
    global  font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font= (font_now,font_size_now))
    
font_size.bind("<<ComboboxSelected>>",change_size)      
    
font_box.bind("<<ComboboxSelected>>",change_font)   

# bold function
#print(tk.font.Font(font=text_editor["font"]).actual())
def bold_fun():
    text_get= tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font=(font_now,font_size_now,"normal")) 
        
bold_btn.configure(command=bold_fun)   
# italic function
def italic_fun():
    text_get= tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font=(font_now,font_size_now,"roman"))    
             
italic_btn.configure(command=italic_fun)    
#underline function
def underline_fun():
    text_get= tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now,font_size_now,"normal")) 
 
underline_btn.configure(command=underline_fun)    

#colour change function
def color_choose():
    color_var= tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    
font_colour_btn.configure(command=color_choose)  
# align function
def align_left():
    text_get_all= text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
    
align_left_btn.configure(command=align_left)

def align_center():
    text_get_all= text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
    
align_center_btn.configure(command=align_center)
  
def align_right():
    text_get_all= text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
    
align_right_btn.configure(command=align_right)

#file menu
text_url= " "
def  new_file(event = None):
    global text_url
    text_url= " "
    text_editor.delete(1.0,tk.END)
    
    
file.add_command(label="New",compound=tk.LEFT,accelerator="ctrl + n",command= new_file)

def  open_file(event = None):
    global text_url
    text_url=filedialog.askopenfilename(initialdir= os.getcwd(),title="select file",filetypes=(("Text file","*.txt"),("All files","*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return  
    except:
        return
    main_application.title(os.path.basename(text_url))       
             
    
file.add_command(label="OPEN",compound=tk.LEFT,accelerator="ctrl + O",command=open_file)
def save_file(event = None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url= filedialog.asksaveasfile(mode ="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*"))) 
            content2= text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()   
    except:
        return           

file.add_command(label="SAVE" ,compound=tk.LEFT,accelerator="ctrl + s",command=save_file)
def save_as_file(event=None):
    global text_url
    try:
        content = text_editor.get(1.0,tk.END)
        text_url= filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return    
    
        
file.add_command(label="SAVE AS" ,compound=tk.LEFT,accelerator="ctrl+alt+s",command=save_as_file)

def exit_fun(event= None):
    global text_change,text_url
    try:
        if text_change:
            mbox= messagebox.askyesnocancel("warning","Do you want to save this file")
            if mbox is TRUE:
                if text_url:
                    content= text_editor.get(1.0,tk.END)
                    with open(text_url,"w",encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2= text_editor.get(1.0,tk.END)
                    text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
      return                           
                    
            

file.add_command(label="EXIT" ,compound=tk.LEFT,accelerator="ctrl+esc ",command=exit_fun)
#edit menu

edit.add_command(label="CUT",compound=tk.LEFT,accelerator="ctrl+x",command= lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="COPY",compound=tk.LEFT,accelerator="ctrl+c",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="PASTE",compound=tk.LEFT,accelerator="ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
def find_fun(event = None):
    
    def  find():
        word = find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches = 0
        if word:
            start_pos ="1.0"
            while True:
                start_pos= text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos= f"{start_pos}+ {len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches+=1
                start_pos= end_pos
                text_editor.tag_config("match",foreground="red",background="blue")
                
    def replace():
        word= find_input.get()
        replace_text=  replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content =content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
        
                    
                
        
    find_popup= tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0,0)
    # frame for find
    find_frame= ttk.Labelframe(find_popup,text="Find and Replace word")
    find_frame.pack(pady=20)
    #label
    text_find= ttk.Label(find_frame,text = "Find")
    text_replace=ttk.Label(find_frame,text="Replace")
    #entry box
    find_input = ttk.Entry(find_frame,width=30)
    replace_input = ttk.Entry(find_frame,width=30)
    #button
    find_button = ttk.Button(find_frame,text = "Find",command=find_fun)
    replace_button =ttk.Button(find_frame,text = "Replace",command=replace)
    #text label grid
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=1,padx=4,pady=4)
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)


edit.add_command(label="FIND",compound=tk.LEFT,accelerator="ctrl+f",command=find_fun)
edit.add_command(label="CLEAR",compound=tk.LEFT,accelerator="ctrl+Alt+x",command=lambda:text_editor.delete(1.0,tk.END))
#view menu
#tool bar and status bar hide
show_status_bar= tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar= tk.BooleanVar()
show_tool_bar.set(True)

def hide_toolbar():
    global show_tool_bar
    if  show_tool_bar:
        tool_bar_label.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar_label.pack(side= tk.TOP, fill = tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar= True
        
def hide_statusbar():
    global show_status_bar
    if  show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar= True
    
        
                   
view.add_checkbutton(label=" TOOL BAR",onvalue=True,offvalue=0,variable =show_tool_bar ,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label=" STATUS BAR",onvalue=True,offvalue=0,variable = show_status_bar,compound=tk.LEFT,command=hide_statusbar)
#colour theme menu

# colour theme function
def change_theme():
    get_theme= theme_choose.get()
    colour_tuple = colour_dict.get(get_theme)
    fg_color,bg_color= colour_tuple[0],colour_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
    
    
    
    

colour_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Night Blue':('#ededed','#6b9dc2')
}
count=0
for i in colour_dict:
    colour_theme.add_radiobutton(label=i,compound=tk.LEFT,variable=theme_choose,command=change_theme)
    count+=1





main_application.config(menu = main_menu)

main_application.mainloop()