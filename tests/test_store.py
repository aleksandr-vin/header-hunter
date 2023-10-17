from header_hunter.store import (
    store_in_env,
    store_in_cookiejar,
    store_value,
)


def test_store_in_env():
    assert 'FOO="bar"' == store_in_env('foo: bar', export=False)
    assert 'export FOO="bar"' == store_in_env('foo: bar', export=True)
    assert 'FOO=""' == store_in_env('foo: ', export=False)
    assert 'export FOO=""' == store_in_env('foo: ', export=True)
    assert 'FOO=""' == store_in_env('foo', export=False)
    assert 'export FOO=""' == store_in_env('foo', export=True)
    assert 'FOO="bar:baz"' == store_in_env('foo: bar:baz', export=False)

def test_store_in_cookiejar():
    assert """#LWP-Cookies-2.0
Set-Cookie3: MpConsentState="AdobeAudienceManager,Google,Facebook,Criteo,GoogleAnalytics"; path="/"; domain="localhost.net"; path_spec; discard; HttpOnly=None; version=0
Set-Cookie3:  XXSession="xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"; path="/"; domain="localhost.net"; path_spec; discard; HttpOnly=None; version=0
Set-Cookie3:  cs_fpid=xxxxxxyyyyyy; path="/"; domain="localhost.net"; path_spec; discard; HttpOnly=None; version=0
Set-Cookie3:  fffff=bbbbb; path="/"; domain="localhost.net"; path_spec; discard; HttpOnly=None; version=0
""" == store_in_cookiejar('Cookie: MpConsentState=AdobeAudienceManager,Google,Facebook,Criteo,GoogleAnalytics; XXSession=xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx; cs_fpid=xxxxxxyyyyyy; fffff=bbbbb', domain="localhost.net")

def test_store_value():
    assert 'bar' == store_value('foo: bar')
    assert '' == store_value('foo: ')
    assert '' == store_value('foo')
    assert 'bar:baz' == store_value('foo: bar:baz')
