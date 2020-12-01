#==========================Necessary imports===================================
import tkinter as tk                    #used to make the whole GUI
from tkinter import ttk                 #used for creating label and different widgets from it
from collections import OrderedDict     #used in scale tones to store different tones and corresponding note.
#===============================================================================

#ordered dictionary contains all type of tunes corresponds to notes enum. 31 different tones
scales_chords = OrderedDict([
    ('Major', [0, 2, 2, 1, 2, 2, 2, 1]),
    ('Natural minor' , [0, 2, 1, 2, 2, 1, 2, 2]),
    ('Harmonic minor' , [0, 2, 1, 2, 2, 1, 3, 1]),
    ('Melodic minor' , [0, 2, 1, 2, 2, 2, 2, 2]),
    ('Dorian mode' , [0, 2, 1, 2, 2, 2, 1, 2]),
    ('Phrygian mode' , [0, 1, 2, 2, 2, 1, 2, 2]),
    ('Lydian mode' , [0, 2, 2, 2, 1, 2, 2, 1]),
    ('Mixolydian mode' , [0, 2, 2, 1, 2, 2, 1, 2]),
    ('Locrian mode' , [0, 1, 2, 2, 1, 2, 2, 2]),
    ('Ahava raba mode' , [0, 1, 3, 1, 2, 1, 2, 2]),
    ('Minor pentatoinc' , [0, 3, 2, 2, 3, 2]),
    ('pentatoinc' , [0, 2, 2, 3, 2, 3]),
    ('Blues', [0, 3, 2, 1, 1, 3]),
    ('5 chord', [0, 7]),
    ('Major chord', [0, 4, 3]),
    ('Minor chord', [0, 3, 4]),
    ('Diminished chord', [0, 3, 3]),
    ('Augmented chord', [0, 4, 4]),
    ('Sus2 chord', [0, 2, 5]),
    ('Sus4 chord', [0, 5, 2]),
    ('Maj7 chord', [0, 4, 3, 4]),
    ('min7 chord', [0, 3, 4, 3]),
    ('7 chord', [0, 4, 3, 3]),
    ('min7b5 chord', [0, 3, 3, 4]),
    ('dim7 chord', [0, 3, 3, 3]),
    ('9 chord', [0, 4, 3, 3, 4]),
    ('Maj9 chord', [0, 4, 3, 4, 3]),
    ('m9 chord', [0, 3, 4, 3, 4]),
    ('11 chord', [0, 4, 3, 3, 4, 3]),
    ('Maj11 chord', [0, 4, 3, 4, 3, 3]),
    ('min11 chord', [0, 3, 4, 3, 4, 3])])

chord_array = [0, 7, 3, 10, 5, 0]

#instance of tk window
win = tk.Tk()

#will return the note corresponding the argument. arguments from above scale_chords.
def chord_name(tonename):
    scaleref = {'E ': 0, 'F ': 1, 'F#': 2, 'G ': 3, 'Ab': 4, 'A ': 5, 'Bb': 6, 'B ': 7, 'C ': 8, 'Db': 9, 'D ': 10,'Eb': 11}
    return scaleref[tonename]

#return the scale note for coloring.
def note_name(tonename):
    notedict = ['E ', 'F ', 'F#', 'G ', 'Ab', 'A ', 'Bb', 'B ', 'C ', 'Db', 'D ', 'Eb']
    return notedict[tonename % 12]

#reset button command line
def reset_it():
    for i in range(0, 25):
        for j in range(2, 8):
            ttk.Label(win, text=note_name(i + chord_array[j-2])).grid(row=j, column=i + 1, padx=0, pady=0)
            

def scale_maker(chord_sel, scale_sel):
    temp_arr = []
    temp_arr.extend(scales_chords[scale_sel])
    temp = 0
    # fill array with 16 notes relevant to key and option.
    new_scale = []
    key_len = len(temp_arr)
    for lin in range(key_len):
        temp += temp_arr[lin % len(temp_arr)]
        new_scale.append(int(temp + chord_name(chord_sel)))
    return new_scale

#default scale when GUI program starts will change to change the deafult preset 
scale = scale_maker('E ', 'Major')

#for console print and for debugging purpose.
print (scale)

#varible instances for using in different ttk instances of Option Menu and other buttons.
var1 = tk.StringVar(win)
var1.set('E ')
var2 = tk.StringVar(win)
var2.set('Major')

#main driving function for coloring the notes from option Menus.
def color_it(val):
    our_tone = str(var1.get())
    our_key = str(var2.get())

    scale = scale_maker(our_tone, our_key)
    #array that will give us our notes which is required and arguments are from the Option Menus.
    ournotes = []

    for notes in scale:
        ournotes.append(note_name(notes))

    #print command when any new note we want to find in scale.
    print (ournotes)

    # draw our whole scale
    for i in range(0, 25):
        for j in range(2, 8):
            first = chord_array[j-2]

            # draw grey for win notes
            if our_tone == note_name(i + first % 12):
                ttk.Label(win, text=note_name(i + first), background='red').grid(row=j, column=i + 1)
            # draw cyan for notes in the scale
            elif note_name(i + first) in ournotes:
                ttk.Label(win, text=note_name(i + first), background='cyan').grid(row=j, column=i + 1)
            # only write note_name
            else:
                ttk.Label(win, text=note_name(i + first)).grid(row=j, column=i + 1)




if __name__ == "__main__":
    #tk window geometry according to the GUI size.
    win.geometry('710x220')
    #resizable set to false as one can't change the size of our GUI window.
    win.resizable(False, False)
    #Title for TK window instance
    win.title('GuitarScaleChart')
    #default value for seeting and placing up different widgets in TK window Layout management
    defX = 40
    defY = 20

    color_it("")

    ttk.Label(win,text="==Options==").place(x=defX* 15.5, y=defY) #label for options.
    chordOptions = ttk.OptionMenu(win, var1, 'E ', 'F ', 'F#', 'G ', 'Ab', 'A ', 'Bb', 'B ', 'C ', 'Db', 'D ','Eb', command=color_it).place(x=defX * 15.5, y=defY*2)  #Option Menu contains all the notes
    scaleOptions = ttk.OptionMenu(win, var2, *scales_chords.keys(), command=color_it).place(x=defX * 15.5, y=defY*4)#
    resetOption = ttk.Button(win, text=' Reset ', command=reset_it).place(x=defX * 15.5, y=defY*6)
    
    #loop for getting the counting from 1 to 25.This is the horizontal counting line.
    for i in range(0, 25):
        ttk.Label(win, text=i, font="Ariel").grid(row=0, column=i + 1,columnspan=1, sticky=tk.E)
        
    #list used to print the vertical scale notes
    stringarray = ['E', 'B', 'G', 'D', 'A', 'E']
    #loop which labels all the above stringarray notes in vertical order
    for j in range(0, 6):
        ttk.Label(win, text=stringarray[j], font="Ariel" ).grid(column=0, row=j + 2, padx=25, pady=5)

    #start of tk window GUI
    win.mainloop()
