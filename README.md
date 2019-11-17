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

# How it Works

1. Run Application
![step1](/images/first.png)

2. Select a PDF you want Parse
![step2](/images/second.png)

3. Click on Parse PDF (results will be displayed and also available via. output file)
![step3](/images/third.png)
