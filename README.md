# Tools for mpv / .edl files

[![Test/Lint](https://github.com/ocodo/edl-tools/actions/workflows/python-package.yml/badge.svg)](https://github.com/ocodo/edl-tools/actions/workflows/python-package.yml)

- - -

## `get_edl_sources.py`

List media used by an `.edl` file.

### Usage:

```sh
python3 get_edl_sources.py <edl filename>
```

If the `.edl` file contains nested `.edl` files, those will also be scanned.

If a `.edl` file contains a reference to itself, no problem (cyclic reference protection is provided).

- - -

# Planned TODO

- move/copy edl and media
- move/copy edl and modify media paths
- move/rename media and update edl(s)
- list nested edls
- list missing media files
- others...?

# Installation

Clone the repo and run as per usage above.
