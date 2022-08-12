.. _code-rst-ref-code-blocks:

.. role:: rst(code)

====================================
Code Blocks With Syntax Highlighting
====================================

A code block consists of a :rst:`.. code-block::` directive and the actual code indented by three spaces, the standard indentation for reStructured Text.

.. tabularcolumns:: arg1

.. code-block:: c++
   :caption: Example Hello World

   /**
   * Example code to print hello world
   **/
   int main()
   {
     std::cout << "Hello World" << std::endl;
     return 0; 
   }
      
.. tabs:: 

   .. group-tab:: Source (rst)
      
      .. code-block:: rst

         .. code-block:: c++
            :caption: Example Hello World

            /**
            * Example code to print hello world
            **/

            #include <iostream>

            int main()
            {
               std::cout << "Hello World" << std::endl;
               return 0; 
            }

   .. group-tab:: Output

      .. code-block:: c++
         :caption: Example Hello World

         /**
         * Example code to print hello world
         **/

         #include <iostream>

         int main()
         {
            std::cout << "Hello World" << std::endl;
            return 0; 
         }

* Always use :ref:`syntactically correct code <code-rst-ref-code-syntax-err>` in a code block.
* Use `Placeholders`_ in angle brackets (:rst:`<placeholder-name>``) to refer to a place in the code where the exact value is not important or to be replaced.

.. _code-rst-ref-code-blocks-codeblock:

Code block directive (:rst:`.. code-block::`)
=============================================

A code block has the following sytax:

.. code-block:: rst

   .. code-block:: <language>
      :caption: <caption>
      <options>

      <code>

.. important:: 

   * There must be a newline between the options and the code.
   * There must not be a newline between the directive line and options or within options.

   Otherwise the rendering will fail.

**<language>**
   The language of the code-block. We commonly use the following: :rst:`c++`,
   :rst:`python3`, :rst:`rst`, :rst:`yaml`, :rst:`javascript`,
   :rst:`html`, :rst:`bash`, :rst:`xml`, :rst:`none`.

   See all :ref:`available lexers <code-rst-ref-code-blocks-lexers>`


**<caption>**
   A caption is highly recommended to give a brief explanation of the code block, or to list out the file path to the referenced code block.

**<options>**
   The following options may be used, all options are optional,
   but :rst:`caption` is highly recommended:

   .. code-block:: rst

      .. code-block:: <language>
         :caption: <caption>
         :linenos:
         :lineno-start: <start-number>
         :emphasize-lines: <emphasized-line-numbers>
         :name: <reference-label>

   :rst:`linenos`
      Show line numbers.

   :rst:`lineno-start`
      Start line numbers with <start-number>.

   :rst:`emphasize-lines`
      <emphasized-line-numbers> contains a comma separated list of line numbers
      to be emphasized.

   :rst:`name`
      Set a <reference-label>. This label can be used to link from any given
      text to the specific code block. The name needs to be unique within one
      manual.

   See also the official
   `sphinx documentation on code-blocks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`__.


.. _code-rst-ref-code-syntax-err:

.. attention::

   **No syntax errors!**

   Syntax highlighting only works if the lexer can parse the code without
   errors. In other words: If there's a syntax error in the code the
   highlighting may not work properly.

   .. tabs::

      .. group-tab:: Correct

         .. code-block:: c++

            #include <iostream>
            using namespace std;

            int main()
            {
               cout << "Hello World" << endl;
               return 0;
            }


      .. group-tab:: Wrong

         .. code-block:: c++
            :emphasize-lines: 1, 2

            #include (iostream)
            using namespace std

            int main()
            {
               cout << "Hello World" << endl;
               return 0;
            }

Examples
========

Code block with line numbers and highlighting of one line
---------------------------------------------------------

.. tabs:: 

   .. group-tab:: Sourcd (rst)

      .. code-block:: rst

         .. code-block:: python3
            :caption: Factorial of a number using recursion
            :linenos:
            :emphasize-lines: 6, 9

            def factorial(x):
                """This is a recursive function
                to find the factorial of an integer"""

                if x == 1:
                    return 1
                else:
                    # recursive call to the function
                    return (x * factorial(x-1))

   .. group-tab:: Output

      .. code-block:: python3
         :caption: Factorial of a number using recursion
         :linenos:
         :emphasize-lines: 6, 9

         def factorial(x):
             """This is a recursive function
             to find the factorial of an integer"""

             if x == 1:
                 return 1
             else:
                 # recursive call to the function
                 return (x * factorial(x-1))

Use code blocks containing diffs
--------------------------------


To emphasize changes that should be made:

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: diff
            :caption: ext_localconf.php.diff

             <?php

            -defined('TYPO3_MODE') or die();
            +defined('TYPO3') or die();

   .. group-tab:: Output

      .. code-block:: diff
         :caption: ext_localconf.php.diff

          <?php

         -defined('TYPO3_MODE') or die();
         +defined('TYPO3') or die();

.. hint::
   You can use diff tools such as the
   `bartlweb diff file generator <https://tools.bartlweb.net/diff/>`__. Make
   sure to use the type :code:`unified context`.


Show a directory tree
---------------------

.. tabs:: 

   .. group-tab:: Source (rst)

      .. code-block:: rst

         .. code-block:: none
            :caption: Page tree of directory :file:`vendor/composer`

            $ tree vendor/composer
            ├── ClassLoader.php
            ├── LICENSE
            ├── autoload_classmap.php
            ├── ...
            └── installed.json

   .. group-tab:: Output

      .. code-block:: none
         :caption: Page tree of directory :file:`vendor/composer`

         $ tree vendor/composer
         ├── ClassLoader.php
         ├── LICENSE
         ├── autoload_classmap.php
         ├── ...
         └── installed.json


.. _code-rst-ref-code-blocks-lexers:

Available lexers
================

You can use any of the following names of lexers:


``| bash, sh, ksh, shell |`` for example all mean the same lexer:

abap \|
abnf \|
ada, ada95, ada2005 \|
adl \|
agda \|
ahk, autohotkey \|
alloy \|
ampl \|
antlr-as, antlr-actionscript \|
antlr-cpp \|
antlr-csharp, antlr-c# \|
antlr-java \|
antlr-objc \|
antlr-perl \|
antlr-python \|
antlr-ruby, antlr-rb \|
antlr \|
apacheconf, aconf, apache \|
apl \|
applescript \|
arduino \|
as, actionscript \|
as3, actionscript3 \|
aspectj \|
aspx-cs \|
aspx-vb \|
asy, asymptote \|
at, ambienttalk, ambienttalk/2 \|
autoit \|
awk, gawk, mawk, nawk \|
basemake \|
bash, sh, ksh, shell \|
bat, batch, dosbatch, winbatch \|
bbcode \|
bc \|
befunge \|
blitzbasic, b3d, bplus \|
blitzmax, bmax \|
bnf \|
boo \|
boogie \|
brainfuck, bf \|
bro \|
bugs, winbugs, openbugs \|
c-objdump \|
c \|
ca65 \|
cadl \|
camkes, idl4 \|
cbmbas \|
ceylon \|
cfc \|
cfengine3, cf3 \|
cfm \|
cfs \|
chai, chaiscript \|
chapel, chpl \|
cheetah, spitfire \|
cirru \|
clay \|
clean \|
clojure, clj \|
clojurescript, cljs \|
cmake \|
cobol \|
cobolfree \|
coffee-script, coffeescript, coffee \|
common-lisp, cl, lisp \|
componentpascal, cp \|
console, shell-session \|
control, debcontrol \|
coq \|
cpp, c++ \|
cpp-objdump, c++-objdumb, cxx-objdump \|
cpsa \|
crmsh, pcmk \|
croc \|
cryptol, cry \|
csharp, c# \|
csound, csound-orc \|
csound-document, csound-csd \|
csound-score, csound-sco \|
css+django, css+jinja \|
css+erb, css+ruby \|
css+genshitext, css+genshi \|
css+lasso \|
css+mako \|
css+mako \|
css+mozpreproc \|
css+myghty \|
css+php \|
css+smarty \|
css \|
cucumber, gherkin \|
cuda, cu \|
cypher \|
cython, pyx, pyrex \|
d-objdump \|
d \|
dart \|
delphi, pas, pascal, objectpascal \|
dg \|
diff, udiff \|
django, jinja \|
docker, dockerfile \|
doscon \|
dpatch \|
dtd \|
duel, jbst, jsonml+bst \|
dylan-console, dylan-repl \|
dylan-lid, lid \|
dylan \|
earl-grey, earlgrey, eg \|
easytrieve \|
ebnf \|
ec \|
ecl \|
eiffel \|
elixir, ex, exs \|
elm \|
emacs, elisp, emacs-lisp \|
erb \|
erl \|
erlang \|
evoque \|
extempore \|
ezhil \|
factor \|
fan \|
fancy, fy \|
felix, flx \|
fish, fishshell \|
flatline \|
fortran \|
fortranfixed \|
foxpro, vfp, clipper, xbase \|
fsharp \|
gap \|
gas, asm \|
genshi, kid, xml+genshi, xml+kid \|
genshitext \|
glsl \|
gnuplot \|
go \|
golo \|
gooddata-cl \|
gosu \|
groff, nroff, man \|
groovy \|
gst \|
haml \|
handlebars \|
haskell, hs \|
haxeml, hxml \|
hexdump \|
hsail, hsa \|
html+cheetah, html+spitfire, htmlcheetah \|
html+django, html+jinja, htmldjango \|
html+evoque \|
html+genshi, html+kid \|
html+handlebars \|
html+lasso \|
html+mako \|
html+mako \|
html+myghty \|
html+php \|
html+smarty \|
html+twig \|
html+velocity \|
html \|
http \|
hx, haxe, hxsl \|
hybris, hy \|
hylang \|
i6t \|
idl \|
idris, idr \|
iex \|
igor, igorpro \|
inform6, i6 \|
inform7, i7 \|
ini, cfg, dosini \|
io \|
ioke, ik \|
irc \|
isabelle \|
j \|
jade \|
jags \|
jasmin, jasminxt \|
java \|
javascript+mozpreproc \|
jcl \|
jlcon \|
js+cheetah, javascript+cheetah, js+spitfire, javascript+spitfire \|
js+django, javascript+django, js+jinja, javascript+jinja \|
js+erb, javascript+erb, js+ruby, javascript+ruby \|
js+genshitext, js+genshi, javascript+genshitext, javascript+genshi \|
js+lasso, javascript+lasso \|
js+mako, javascript+mako \|
js+mako, javascript+mako \|
js+myghty, javascript+myghty \|
js+php, javascript+php \|
js+smarty, javascript+smarty \|
js, javascript \|
jsgf \|
json \|
jsonld, json-ld \|
jsp \|
julia, jl \|
kal \|
kconfig, menuconfig, linux-config, kernel-config \|
koka \|
kotlin \|
lagda, literate-agda \|
lasso, lassoscript \|
lcry, literate-cryptol, lcryptol \|
lean \|
less \|
lhs, literate-haskell, lhaskell \|
lidr, literate-idris, lidris \|
lighty, lighttpd \|
limbo \|
liquid \|
live-script, livescript \|
llvm \|
logos \|
logtalk \|
lsl \|
lua \|
make, makefile, mf, bsdmake \|
mako \|
mako \|
maql \|
mask \|
mason \|
mathematica, mma, nb \|
matlab \|
matlabsession \|
minid \|
modelica \|
modula2, m2 \|
monkey \|
moocode, moo \|
moon, moonscript \|
mozhashpreproc \|
mozpercentpreproc \|
mql, mq4, mq5, mql4, mql5 \|
mscgen, msc \|
mupad \|
mxml \|
myghty \|
mysql \|
nasm \|
ncl \|
nemerle \|
nesc \|
newlisp \|
newspeak \|
nginx \|
nimrod, nim \|
nit \|
nixos, nix \|
nsis, nsi, nsh \|
numpy \|
objdump-nasm \|
objdump \|
objective-c++, objectivec++, obj-c++, objc++ \|
objective-c, objectivec, obj-c, objc \|
objective-j, objectivej, obj-j, objj \|
ocaml \|
octave \|
odin \|
ooc \|
opa \|
openedge, abl, progress \|
pacmanconf \|
pan \|
parasail \|
pawn \|
perl, pl \|
perl6, pl6 \|
php, php3, php4, php5 \|
pig \|
pike \|
pkgconfig \|
plpgsql \|
postgresql, postgres \|
postscript, postscr \|
pot, po \|
pov \|
powershell, posh, ps1, psm1 \|
praat \|
prolog \|
properties, jproperties \|
protobuf, proto \|
ps1con \|
psql, postgresql-console, postgres-console \|
puppet \|
py3tb \|
pycon \|
pypylog, pypy \|
pytb \|
python, py, sage \|
python3, py3 \|
qbasic, basic \|
qml, qbs \|
qvto, qvt \|
racket, rkt \|
ragel-c \|
ragel-cpp \|
ragel-d \|
ragel-em \|
ragel-java \|
ragel-objc \|
ragel-ruby, ragel-rb \|
ragel \|
raw \|
rb, ruby, duby \|
rbcon, irb \|
rconsole, rout \|
rd \|
rebol \|
red, red/system \|
redcode \|
registry \|
resource, resourcebundle \|
rexx, arexx \|
rhtml, html+erb, html+ruby \|
roboconf-graph \|
roboconf-instances \|
robotframework \|
rql \|
rsl \|
rst, rest, restructuredtext \|
rts, trafficscript \|
rust \|
sass \|
sc, supercollider \|
scala \|
scaml \|
scheme, scm \|
scilab \|
scss \|
shen \|
silver \|
slim \|
smali \|
smalltalk, squeak, st \|
smarty \|
sml \|
snobol \|
sourceslist, sources.list, debsources \|
sp \|
sparql \|
spec \|
splus, s, r \|
sql \|
sqlite3 \|
squidconf, squid.conf, squid \|
ssp \|
stan \|
swift \|
swig \|
systemverilog, sv \|
tads3 \|
tap \|
tcl \|
tcsh, csh \|
tcshcon \|
tea \|
termcap \|
terminfo \|
terraform, tf \|
tex, latex \|
text \|
thrift \|
todotxt \|
trac-wiki, moin \|
treetop \|
ts, typescript \|
turtle \|
twig \|
typoscript \|
typoscriptcssdata \|
typoscripthtmldata \|
urbiscript \|
vala, vapi \|
vb.net, vbnet \|
vcl \|
vclsnippets, vclsnippet \|
vctreestatus \|
velocity \|
verilog, v \|
vgl \|
vhdl \|
vim \|
wdiff \|
x10, xten \|
xml+cheetah, xml+spitfire \|
xml+django, xml+jinja \|
xml+erb, xml+ruby \|
xml+evoque \|
xml+lasso \|
xml+mako \|
xml+mako \|
xml+myghty \|
xml+php \|
xml+smarty \|
xml+velocity \|
xml \|
xquery, xqy, xq, xql, xqm \|
xslt \|
xtend \|
xul+mozpreproc \|
yaml+jinja, salt, sls \|
yaml \|
zephir \|

**Tip:** Try the Pygments Demo at http://pygments.org/


`Sphinx <http://www.sphinx-doc.org/en/stable/>`__ uses `Pygments
<http://pygments.org/>`__ for highlighting. On a machine that has Pygments
installed the command `pygmentize -L` will list all available lexers.

Literalinclude
==============

A drawback of code blocks is that most editors cannot properly highlight or
indent code within code blocks. The directive :rst:`.. literalinclude::` enables you
to store longer code blocks in an external file with the proper file extension.

The :rst:`.. literalinclude::` directive imports the file and displays its content as
code block.


.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/SiteConfiguration/Index.rst

         .. literalinclude:: /Doc/_Templates/project.rst.txt
            :language: rst
            :emphasize-lines: 5,8-11
            :linenos:

   .. group-tab:: Output

      .. literalinclude:: /Doc/_Templates/project.rst.txt
         :language: rst
         :emphasize-lines: 5,8-11
         :linenos:

Literal includes can even be used to render the difference between files,
without having to create a diff file first:

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/SiteConfiguration/Index.rst

         .. literalinclude:: /Doc/_Templates/package.rst.txt
            :diff: /Doc/_Templates/project.rst.txt

   .. group-tab:: Output

      .. literalinclude:: /Doc/_Templates/package.rst.txt
         :diff: /Doc/_Templates/project.rst.txt


See also `literalinclude directive
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`__.


Placeholders
============

Placeholders in this context are named tags in code and
example URLs where the exact value does not matter,
but is referenced in the surrounding documentation.
Use the *Backus-Naur form* ``<placeholder-name>`` for placeholders in code and
URLs, i.e. use angle brackets to encapsulate the placeholder name.

For example in C++

.. code-block:: rst

   Set up a controller class to handle user interaction with the entity data
   model:

   .. code-block:: c++

      class <Entity>Controller : public ActionController
      {
         ...
      };

   where `<Entity>` corresponds to the entity data model class name.
