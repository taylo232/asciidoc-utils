This is a set of python scripts collecting together the commands I have
been using on the linux commandline (wsl) to process my asciidocs.

rascon.py
=========

*(R)ichard’s (AS)ciidoc (CON)version*

This script converts an asciidoc file into a variety of formats, all in
the current directory.

The formats are \[**d**\]ocx, \[**e**\]pub, \[**h**\]tml,
\[**m**\]arkdown, \[**p**\]df, \[**t**\]xt, docbook\[**x**\]ml,
\[**a**\]ll.

For conversion to MS Word (.docx) there needs to be a Word document
called `template.docx` in `` home/<user>/.pandoc/` ``. The template can
be configured in MS Word to your own preferred style.

Usage: `rascon.py [adehmptx] file.adoc`

A lack of command options assumes \[**a**\]ll

**OS Dependencies (Linux):**

-   pandoc, asciidoc, dblatex

**TODO:**

-   Offer a help option (h and --help) along with versioning/date

-   Auto check for the presence of `template.docx` and warn if necessary

raspub.py
=========

*(R)ichard’s (AS)ciidoc (PUB)lisher*

This script moves any html files in the current folder to the nominated
publishing folder. In the destination folder, the existing `index.html`
file is replaced with a new one containing the links to any html file
found in that folder. The links are sorted by modified date, with the
newest at the top. It is assumed that the publishing folder contains a
css file `pub.css`.

Usage: `raspub.py`

**OS Dependencies (Linux):** - None

**TODO:**

-   Offer ftp transfer of pub files through commandline option and cfg
    file for login info


