from header_hunter.sniff import sniff_header_from_clipboard, sniff_cookie_from_clipboard
from header_hunter.store import store_in_env, store_in_cookiejar
from header_hunter.version_info import version
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description=f'HTTP Header Hunter v{version}')

    parser.add_argument(
        '-o', '--output-format',
        choices=['env', 'export', 'jar'],
        default='env',
        help='choose the output format (env, export or jar)'
    )

    parser.add_argument(
        '-c', '--cookie', 
        action='store_true',
        help='enbale cookie sniffing'
    )

    parser.add_argument(
        '--no-cookie',
        action='store_false',
        dest='cookie',
        help='disable cookie sniffing'
    )

    parser.add_argument('header_names', nargs='*', help='header names')

    parser.set_defaults(cookie=True)

    args = parser.parse_args()

    encoders = {
        'env': lambda x: store_in_env(x, export=False),
        'export': lambda x: store_in_env(x, export=True),
        'jar': lambda x: store_in_cookiejar(x, 'localhost')
    }

    encoder = encoders[args.output_format]

    for name in args.header_names:
        encoder(sniff_header_from_clipboard(name))
    
    if args.cookie:
        encoder(sniff_cookie_from_clipboard())
