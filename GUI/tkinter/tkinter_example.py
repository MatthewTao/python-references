"""
https://www.pythontutorial.net/tkinter/
"""
import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')
"""
geometry takes a weird string input `{width}x{height}{x}{y}`
The width is the window's width in pixels.
The height is the window's height in pixels.

The x is the window's horizontal position. 
+50 means the left edge of the window should be 50 pixels from the left edge of the screen.
And -50 means the right edge of the window should be 50 pixels from the right edge of the screen.

The y is the window's vertical position.
+50 means the top edge of the window should be 50 pixels below the top of the screen.
And -50 means the bottom edge of the window should be 50 pixels above the bottom of the screen.

# If a centered window is desired

```python
window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
```
"""

# 0 fully transparent, 1.0 opaque default is 1
root.attributes('-alpha', 0.5)

# To change the default icon. Must be .ico file
# root.iconbitmap('./assets/pythontutorial.ico')


# Create a Label widget
# places that widget in the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()
