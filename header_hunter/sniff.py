

def sniff_header_from_text(name, text):
    """
    Sniff specific header from the text.
    """
    import re
    pattern = f"'{name}: *.*?'"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        result = match.group(0)[1:][:-1]
        return result
    else:
        return None


def sniff_cookie_from_text(text):
    """
    Sniff Cookie from the text.
    """
    return sniff_header_from_text('Cookie', text)


def sniff_cookie_from_clipboard():
    """
    Sniff Cookie from the clipboard. If you copy request from your browser's Network tab (in Developer Tools) as a Curl, then Cookie header will be there.
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
    return sniff_header_from_text(name, text)
