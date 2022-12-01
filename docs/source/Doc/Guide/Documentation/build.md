# Build Documentation

The following sections describes how to build this documentation locally and view offline.

## Build instruction

1. Create and activate conda environment

    ```bash
    conda create -n rris_doc python=3.6
    ```

    Activate conda environment
    ```bash
    conda activate rris_doc
    ```

2. Install required packages


    Install Sphinx, Read-the-Docs theme and extensions
    ```bash
    pip install sphinx sphinx-rtd-theme
    pip install sphinx-copybutton
    pip install sphinx-tabs
    pip install sphinxcontrib-youtube
    pip install sphinx-design
    ```

    (Optional) Install Markdown support
    ```bash
    pip install --upgrade myst-parser
    pip install docutils==0.17
    ```

3. Build docs

    For new documentation
    ```bash
    mkdir docs
    cd docs
    sphinx-quickstart
    # setup project configuration, then
    make html
    ```

    For building this documentation
    ```bash
    clone
    cd docs
    mkdir build
    make html
    ```

    View offline by running a web server
    ```bash
    # Inside docs/build/html directory
    python3 -m http.server
    ```
    Then open in browser [http://localhost:8000](http://localhost:8000).

## Errors

- pip dependency errors

    ```shell
    pip install pillow
    pip install six
    pip install decorator
    pip install pexpect
    ```
