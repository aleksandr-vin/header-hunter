# Misc cookie awareness methods


def sniff_cookie_from_clipboard():
    """
    Sniff Cookies from the clipboard. If you copy request from your browser's Network tab (in Developer Tools) as a Curl, then Cookie header will be there.
    """
    return sniff_header_from_clipboard('Cookie')
    

def sniff_header_from_clipboard(name):
    """
    Sniff specific header from the clipboard. If you copy request from your browser's Network tab (in Developer Tools) as a Curl, then header will be there.
    """
    from tkinter import Tk
    t = Tk()
    text = t.clipboard_get()
    t.destroy()
    import re
    pattern = f"'{name}:\s*.*?'"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        result = match.group(0)[1:][:-1]
        return result
    else:
        return None
