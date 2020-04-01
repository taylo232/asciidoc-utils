This is a set of python script collecting together the commands I have
been using in linux (wsl) to process my asciidocs.

rascon.py
=========

This converts an asciidoc file into a variety of formats, all done in
the working directory.

The formats are \[d\]ocx, \[e\]pub, \[h\]tml, \[m\]arkdown, \[p\]df,
\[t\]xt, docbook\[x\]ml, \[a\]ll

Usage: `rascon.py [adehmptx] file.adoc`

A lack of command options assumes \[a\]all

====== OS Dependencies Linux: pandoc, asciidoc, dblatex

====== TODO

Offer a help option (h and --help) along with version date
