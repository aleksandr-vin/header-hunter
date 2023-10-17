

def store_in_cookiejar(cookie_str, domain):
    """
    Store cookies from 'Cookie: ...' string into a cookie jar file. Provide domain.
    """
    if cookie_str == None:
        return

    import tempfile
    
    with tempfile.NamedTemporaryFile('w+', delete=True) as temp_file:
        import http.cookiejar
        jar = http.cookiejar.LWPCookieJar(temp_file.name)

        for cookie in cookie_str.split(": ")[1].split(";"):
            cookie_name, cookie_value = cookie.split("=", 1)
            cookie = http.cookiejar.Cookie(
                version=0,
                name=cookie_name,
                value=cookie_value,
                port=None,
                port_specified=False,
                domain=domain,
                domain_specified=True,
                domain_initial_dot=False,
                path="/",
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={"HttpOnly": None},
                rfc2109=False
            )
            jar.set_cookie(cookie)

        jar.save(ignore_discard=True)
        temp_file.seek(0)
        print(temp_file.read())


def store_in_env(text, export=False):
    """
    Print a 'Foo: Bar' text as FOO="Bar" line.
    """
    if text == None:
        return

    if export:
        prefix = 'export '
    else:
        prefix = ''

    s = text.split(": ")
    k = s[0]
    v = s[1]
    print(prefix + k.upper() + '="' + v + '"')
