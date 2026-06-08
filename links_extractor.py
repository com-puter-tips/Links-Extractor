#!/usr/bin/env python3
"""Extract all internal and external links from a URL."""
import argparse
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

__author__ = "Devharsh Trivedi"
__license__ = "GPL-3.0"
__version__ = "1.4.0"


def extract_links(url, timeout=30):
    """Fetch a page and return (internal_links, external_links) as sets.

    A link is internal when its host matches the host of ``url`` (or when it
    is a relative link); otherwise it is external. Empty anchors and
    ``javascript:``, ``mailto:``, and ``tel:`` links are ignored.
    """
    page = requests.get(url, timeout=timeout)
    soup = BeautifulSoup(page.text, "lxml")
    external, internal = set(), set()
    base = urlparse(url).netloc.lower()
    for a in soup.findAll("a", attrs={"href": True}):
        href = a["href"].strip()
        if len(href) <= 1 or href[0] == "#":
            continue
        if href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        if "http" in href or "https" in href:
            if base in urlparse(href).netloc.lower():
                internal.add(a["href"])
            else:
                external.add(a["href"])
        else:
            internal.add(a["href"])
    return internal, external


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Extract all internal and external links from one or more URLs.")
    parser.add_argument("urls", nargs="+", help="One or more URLs to scan")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)
    for url in args.urls:
        try:
            internal, external = extract_links(url)
            print(f"\n{url}\n---------------------\n")
            print(f"{len(internal)} internal links found:\n")
            for link in internal:
                print(link)
            print(f"\n{len(external)} external links found:\n")
            for link in external:
                print(link)
            print()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
