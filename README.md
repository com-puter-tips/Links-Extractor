# Links-Extractor

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Extract all internal and external links from a URL in Python.

## Description

Links-Extractor fetches one or more web pages and lists the internal and external hyperlinks found on each page. A link is treated as internal when its host matches the host of the page being scanned, and external otherwise. Empty anchors and `javascript:`, `mailto:`, and `tel:` links are ignored.

## Requirements

- Python 3
- Dependencies: `requests`, `beautifulsoup4`, `lxml`

Install them with:

```
pip install -r requirements.txt
```

## Usage

Pass one or more URLs as arguments:

```
python3 extractor.py https://example.com
python3 extractor.py https://example.com https://www.python.org
```

Redirect the output to a file:

```
python3 extractor.py https://example.com > out.txt
```

For each URL the script prints the count and list of internal links followed by the count and list of external links.

A full write-up is available at http://com.puter.tips/2016/12/extract-all-internal-and-external-links.html

You may also find the companion project useful: https://github.com/com-puter-tips/SEO-Analysis

## Citation

If you use this software, please cite it using the metadata in [CITATION.cff](CITATION.cff).

## License

Distributed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
