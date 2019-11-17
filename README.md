# pdfparser
GUI application for reading PDF files and writing results to file.

## Prerequisites
* Python 3.6

## Installation
```pip install -r requirements.txt```

## Usage
```
from gui import Application
csvFilePath = 'outputs.csv'
app = Application(outPath=csvFilePath)
app.run()
```
