from tkinter import filedialog
import tkinter as tk

class DJToolRegexHelperGUI:
    def __init__(self, regex, root):

        self.regex = regex
        self.root = root

        # Configure column weights
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)  # Button column with higher weight
        root.columnconfigure(2, weight=1)

        # Configure row weights
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)  # Button row with higher weight
        root.rowconfigure(2, weight=1)


        # Create dir button and pack it in grid
        self.select_dir_button = tk.Button(root, text="Directory", command=self.select_input_dir)
        self.select_dir_button.grid(row=1, column=0)


        # Create regex pattern drop down menu define options and pack it into grid
        self.options = ['[...]','.mp3']
        self.selected_option = tk.StringVar() # Create a StringVar to hold the selected option
        self.selected_option.set('Select Pattern')  # Default value
        self.select_regex_pattern_menu = tk.OptionMenu(self.root, self.selected_option, *self.options, command=self.remove_regex_pattern)
        self.select_regex_pattern_menu.grid(row=1, column=2)

        # Create Info Label
        self.info_label = tk.Label(self.root, text='')

    def select_input_dir(self):
        self.regex.dir = filedialog.askdirectory(title='Select Directory')

    def remove_regex_pattern(self, pattern):
        if self.regex.dir and pattern:
            match pattern:
                case '[...]':
                    self.regex.remove_sqr_brackets()
                case '.mp3':
                    self.regex.remove_redundant_mp3()
            #self.info_label.grid(row=2, column=1, pady=10)
            #self.info_label['text'] = 'Working'
            #self.root.after(100, self.check_thread_completion)

    def check_thread_completion(self):
        if self.regex.thread_completion_event.is_set():
            self.info_label['text'] = 'Finished'
            self.regex.thread_completion_event.clear()

        else:
            self.root.after(100, self.check_thread_completion)
        