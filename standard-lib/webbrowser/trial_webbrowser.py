"""
Looks like this just opens the web browser to a given URL.

Not quite the same as selenium, which can control the browser after opening as well.
"""
import webbrowser

if __name__ == "__main__":
    # Default behaviour is to open in a new tab of an existing window, and brought into focus if possible
    webbrowser.open("https://www.python.org")

    webbrowser.open("https://www.python.org", new=1)  # open in a new window if possible
    # Doesn't seem to work on Edge, YMMV on other browsers

    webbrowser.open("https://www.python.org", new=2)  # open in a new tab if possible
    # This is the very similar to the default behaviour anyway

    webbrowser.open("https://www.python.org", new=1, autoraise=False)
    # open in a new window if possible, but don't bring to front
    # Doesn't seem to work on Edge. Window was still brought to front
