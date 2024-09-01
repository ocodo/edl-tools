import os
import sys
import inspect


def help():
    script = os.path.basename(__file__)

    print(inspect.cleandoc(f'''
    Get .edl sources

    Print an unsorted list of unique primary media files
    used by an mpv .edl file.

    It will recursively read child .edl files used in the given .edl file

    Usage:

    python3 {script} <edlfile.edl>
    '''))


def media_filename(line):
    return line.split(',')[0]


def get_edl_media(edl_filename):
    '''
    Open edl_filename and read the contents,
    parse out and return the unique media filenames.
    '''
    media = set()

    nested_edls = set()

    with open(edl_filename, 'r') as edl_file:
        for line in edl_file:
            line = line.rstrip()

            _, ext = os.path.splitext(line)

            # Ignore comments and file header
            if line.startswith('#'):
                continue

            # Ignore stream commands etc.
            if line.startswith('!'):
                continue

            if ext == '.edl':
                nested_edls.add(line)
                continue

            if line:
                media.add(media_filename(line))

    for edl in nested_edls:
        try:
            nested_media = get_edl_media(edl)
            for m in nested_media:
                media.add(m)
        except RuntimeError:
            # on recursion limit
            break

    return media


if __name__ == '__main__':
    if len(sys.argv) != 2:
        help()
        quit()

    edl = sys.argv[1]
    if os.path.exists(edl):
        filename, ext = os.path.splitext(edl)
        if ext == '.edl':
            print('\n'.join(get_edl_media(edl)))
        else:
            print(f'Not an edl file: {edl}')
    else:
        print(f'File not found: {edl}')
