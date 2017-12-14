from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import func as d


def create_gui():  # Main window implementation
    master = Tk()
    master.title("algorithms")

    mainframe = ttk.Frame(master, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    def open_file():
        filename = askopenfilename(master=mainframe)  # Log file path retrieval
        console.insert(END, filename + " opened" + '\n')  # Displaying the path information in text area
        set_path(filename)

    def set_path(path_input):
        path.set(path_input)

    def set_date(date_input):
        date.set(date_input)

    def get_return():  # Returning the result according the type of result
        a = d.search_file(path.get(), date.get())
        for i in a:
            console.insert(END, i)
        print(a)

    def file_sorted():  # Sort completed information
        d.file_sorting(path.get())
        console.insert(END, "File sorted" + '\n')

    path = StringVar(mainframe, value='Enter your file path or choose')  # String variable of path
    date = StringVar(mainframe, value='Enter a date(day/month/year)')  # String variable of date

    path_label = Label(mainframe, text="Path of log file")  # Labeling the path text box
    path_label.grid(row=1, column=2, sticky=N)

    file_path = Entry(mainframe, textvariable=path, width=50)  # Path input box
    file_path.config(justify=CENTER)
    file_path.grid(row=1, column=3, columnspan=2, sticky=N)

    file_chooser = Button(mainframe, text="Choose log file", command=open_file)  # File choose box
    file_chooser.grid(row=1, column=5, sticky=N)

    file_sorter = Button(mainframe, text="Sort the log file", command=lambda: file_sorted())  # Sort button
    file_sorter.grid(row=1, column=6, sticky=N)

    sort_label = Label(mainframe, text="Search date")  # Labeling the date box
    sort_label.grid(row=2, column=2, sticky=N)

    file_path = Entry(mainframe, textvariable=date, width=50)  # Date input box
    file_path.config(justify=CENTER)
    file_path.grid(row=2, column=3, columnspan=2, sticky=N)

    date_searcher = Button(mainframe, text="Search", command=lambda: get_return())  # Search button
    date_searcher.grid(row=2, column=5, sticky=N)

    console = Text(mainframe, width=120)  # Information text box
    console.grid(row=3, column=1, columnspan=8)

    mainframe.mainloop()  # Main frame initialization


create_gui()
