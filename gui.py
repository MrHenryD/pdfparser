import os
import sys
import time

import tkinter as tk
from tkinter import filedialog

from pdfreader import PDF

class Application:
    def __init__(self, outPath, length=700, width=700):
        self.counter = 0
        self.outPath = outPath

        window = tk.Tk()
        window.title('PDF Parser')
        window.geometry('%sx%s' % (length, width))
        self.window = window
        instructionsText = 'Select a PDF to Start!' + '\n'
        instructionsText += 'Results available at: %s' % self.outPath

        self.instructionLabel = tk.Label(self.window, 
                                            text=instructionsText).pack()
        self.btnFile = tk.Button(self.window, text='Open a PDF', command=self.open_file).pack()
        
        self.fileLabelText = tk.StringVar()
        self.fileLabelText.set('')
        self.fileLabel = tk.Label(self.window, textvariable=self.fileLabelText).pack()
        
        self.btnParse = tk.Button(self.window, text='Parse PDF', command=self.parse).pack()
        self.parseLabelText = tk.StringVar()
        self.parseLabelText.set('')
        self.parseLabel = tk.Label(self.window, textvariable=self.parseLabelText).pack()

    def open_file(self):
        filePath = filedialog.askopenfilename()
        self.fileLabelText.set(filePath)
        self.parseLabelText.set('')
        self.refresh()

    def parse(self):
        pdfFile = self.fileLabelText.get()
        if '.pdf' not in pdfFile:
            self.parseLabelText.set('Invalid File. Not a PDF file.')
            self.refresh()
        else:
            self.parseLabelText.set('Parsing File')
            self.refresh()
            pdf = PDF()
            fields = pdf.getFormFields(pdfFile)
            pdf.write(fields, self.outPath)

            resultString = ''
            for k, v in fields.items():
                resultString += '%s: %s \n' % (k, v)
            resultString += 'Finished Parsing File.' 

            self.parseLabelText.set(resultString)
            self.refresh()
            self.counter += 1

        if self.counter > 2:
            sys.exit('Exiting...')

    def refresh(self):
        self.window.update_idletasks()
        time.sleep(0)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()