# Serve

Simple webserver that hosts html, css and binary files on your localhost. Can be used to create a pip package that runs from the macOS terminal.
Does not inject code into your pages and cannot auto refresh. After changing your website code, the browser needs a manual reload.

# Create pip package

Go to the folder that contains pyproject.toml and execute:

```pip install .```

# Usage

Go to a folder in the Terminal that contains index.html and execute:

```serve```

# Uninstall

pip uninstall serve
