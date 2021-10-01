# Sneakers API [DEV]

### v4.0.0a

## Ryzen Update!!!

### Main

We are preparing something big!

### Computer Vision Model Summary

- Tensorflow model
- Dataset constructor
- Training builder
- Plotting and debugging utilities

## Installation:

### Linux, Windows, Mac:

`$ git clone https://github.com/dyphen12/Sneakers.git`

`$ cd Sneakers`

`$ pip install -r requirements.txt`

`$ python3 unit-test.py` 

Windows users: make sure you got python in your $PATH

## How To Use:

You can run the example script 'unit-test.py'.

`$ python3 unit-test.py`

Also, you can use a Tkinter GUI.

`$ python3 main.py`

Or, you can start the REST API.

`$ python3 app.py`

### Basic usage:

```
unit-test.py

import sneakers.api.utils as skutils
from sneakers.api.composer import Composer


# Set the title of our Worksheet and set the composer.
titl = skutils.composer_title('composer', 'Testings1')


# This is necessary on windows systems.
if __name__ == '__main__':

    # Creates a basic composer with a worksheet of size 5
    xcomposer = Composer(titl)
    
    # Expand worksheet from 5 to 200
    xcomposer.expand_worksheet(200)
    
    # Write 100 images from the start to 102.
    xcomposer.write_wb_xl([2,102],iny_size=100)
    
    # Upload file to drive for the first time
    xcomposer.upload_file()
```

### Worksheet Title

_Example:_

**Motor:** composer

**Title:** hello-world1

`titl = skutils.composer_title('composer', 'hello-world1')`

The title is the name of the worksheet and the name of the composer, 
in order to load or create a workbook you must provide the correct name.






