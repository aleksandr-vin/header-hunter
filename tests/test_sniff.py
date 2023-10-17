from header_hunter.sniff import (
    sniff_header_from_text,
    sniff_cookie_from_text,
)
from tests.samples import copy_as_curl


def test_sniff_header_from_text():
    assert 'foo: bar' == sniff_header_from_text('foo', """'foo: bar'""")
    assert 'Foo: bar' == sniff_header_from_text('foo', """'Foo: bar'""")
    assert 'Foo: bar' == sniff_header_from_text('foo', """-H 'Foo: bar'""")
    assert 'Foo: bar' == sniff_header_from_text('foo', """-H 'xFoo: bar'\n-H 'Foo: bar'""")


def test_sniff_header_from_text():
    for browser, versions in copy_as_curl.items():
        for version, sample in versions.items():
            assert 'Cookie: MpConsentState=AdobeAudienceManager,Google,Facebook,Criteo,GoogleAnalytics; XXSession=xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx; cs_fpid=xxxxxxyyyyyy; fffff=bbbbb' == sniff_cookie_from_text(sample)
