# EDL Tools

Tools for working with mpv `.edl` files

## `get_edl_sources.py`

List media used by an `.edl` file.

### Usage:

```sh
python3 get_edl_sources.py <edl filename>
```

If the `.edl` file contains nested `.edl` files, those will also be scanned. 

If a `.edl` file contains a reference to itself, no problem (cyclic reference protection is provided).

# Installation

Clone the repo and run as per usage above.
