# mkdocs_include_exclude_files

By default, mkdocs copies everything it can find in the `docs_dir` directory that doesn't start with a `.`

This plugin allows for customising that.

## Installation

```bash
pip install mkdocs_include_exclude_files
```

Requires MkDocs 1.2.3+ and Python 3.8+

## Usage

In `mkdocs.yml`:
```
plugins:
    - search  # default plugin, need to re-enable when using manual plugins
    - include_exclude_files:
        - include:
            - ".some_file"
            - ".anotherfile"
        - exclude
            - "some_folder"
            - "anotherfolder"
```

Every file exactly matching those in `include` will be included. Any file whose location *starts with* anything in `exclude` will be excluded.
