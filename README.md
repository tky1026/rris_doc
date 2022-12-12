# RRIS Documentation

## Building the documentation
1. Create conda environment
    ```bash
    conda create -n rris_doc python=3.9
    conda activate rris_doc
    ```

1. Install required packages

    ```bash
    pip install -r docs/requirements.txt
    ```

    Or

    ```bash
    pip install sphinx==4.5.0
    pip install sphinx-rtd-theme==1.0.0
    pip install sphinx-tabs==3.3.1
    pip install sphinx-copybutton
    pip install sphinx-design
    pip install sphinxcontrib-youtube
    pip install Sphinx-Substitution-Extensions
    pip install --upgrade myst-parser
    ```
    - *Note: Building the documentation requires Python>=3.7, sphinx==4.5.0 and sphinx-rtd-theme==1.0.0. For proper rendering, install version specific packages if specified.*

1. Build this documentation using sphinx

    ```bash
    cd docs
    mkdir build
    make html
    ```

### Read the Docs

Project home: https://readthedocs.org/projects/rris-doc-testing/

View online: https://rris-doc-testing.readthedocs.io/en/latest/


### Ref

https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Index.html

https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html

https://docutils.sourceforge.io/docs/user/rst/quickref.html

https://github.com/leggedrobotics/ros_best_practices/wiki

https://answers.ros.org/question/11835/when-should-i-split-my-code-into-multiple-packages-and-whats-a-good-way-to-split-it/

http://wiki.ros.org/DevelopersGuide

!!

https://docutils.sourceforge.io/docs/ref/rst/directives.html#id1


- alias shortcut

    ```shell
    alias rerun_server="cd; cd ~/Desktop/rris_doc/docs/build/html; python3 -m http.server"
    ```