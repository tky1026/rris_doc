# Build Documentation

The following sections describes how to build this documentation locally and view offline.

## Build instruction

1. **Create and activate conda environment**

    ```bash
    conda create -n rris_doc python=3.9
    ```

    Activate conda environment
    ```bash
    conda activate rris_doc
    ```

2. **Install required packages**

    Install Sphinx, Read-the-Docs theme and extensions.

    For this doucmentation
    ```bash
    pip install -r docs/requirements.txt
    ```

    Or in general

    ```bash
    pip install sphinx==4.5.0 
    pip install sphinx-rtd-theme==1.0.0
    pip install sphinx-tabs==3.3.1
    pip install sphinx-copybutton
    pip install sphinx-design
    pip install sphinxcontrib-youtube
    pip install Sphinx-Substitution-Extensions
    ```

    Install Markdown support
    ```bash
    pip install --upgrade myst-parser
    ```

    *Note: Building the documentation requires Python>=3.7, sphinx==4.5.0 and sphinx-rtd-theme==1.0.0. For proper rendering, install version specific packages if specified.*

3. **Build docs**

    For building this documentation
    ```bash
    clone
    cd docs
    mkdir build
    make html
    ```

    For new documentation
    ```bash
    mkdir docs
    cd docs
    sphinx-quickstart
    # setup project configuration, then
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
