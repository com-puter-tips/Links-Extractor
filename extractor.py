#!/usr/bin/env python3
"""Backward-compatible entry point. Logic lives in the importable
``links_extractor`` module (pip install the package for the
``links-extractor`` command)."""
from links_extractor import main

if __name__ == "__main__":
    main()
