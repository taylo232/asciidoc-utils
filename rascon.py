#!/usr/bin/env python3
'''
(R)ichard's (AS)ciidoc (CON)version - Convert an asciidoc file into various file formats
[d]ocx, [e]pub, [h]tml, [m]arkdown, [p]df, [t]xt, docbook[x]ml, [a]ll
INPUT:
[switches for choosing conversion type] Name of adoc file. No switches implies [a]ll
Assumes asciidoc file suffix is '.adoc'
OUTPUT: Files in the chosen format in the current directory
OS DEPENDENCIES
pandoc, asciidoctor, asciidoc, dblatex
TODO: Offer a help option (h and --help) along with version date
'''
import sys
import subprocess

# Setting path the the pandoc MS Word template
PANDOCCFG = (os.path.expanduser('~')) + '/.pandoc'
PANDOCDOCX = '--reference-doc=' + PANDOCCFG + '/template.docx'

# read in args
if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("Something not quite right\nrascon [adehmptx] filename.adoc")
    quit()

# if only filename assuming [a]ll. if two args then assume <cmd><file>
if len(sys.argv) == 2:
    CONFILE = sys.argv[1]
    CMDLIST = "a"
else:
    CONFILE = sys.argv[2]
    CMDLIST = sys.argv[1]

# if args wrong way round then swap values
if CMDLIST[-4:] == "adoc":
    CMDLIST, CONFILE = CONFILE, CMDLIST

# if the file suffix is not 'adoc' then abort
if CONFILE[-4:] != "adoc":
    print("Something not quite right\nrascon [adehmptx] filename.adoc")
    quit()
# strip off '.adoc'
CONFILE = CONFILE.replace('.adoc', '')

# print("File stub :", CONFILE)
# print("Commands  :", CMDLIST)

CMDPRINT = " Converting ", CONFILE, ".adoc to:\n ->"
CMDPRINT = ''.join(CMDPRINT)

if ('a' in CMDLIST) or ('d' in CMDLIST):
    OP_DOCX = 1
    CMDPRINT = CMDPRINT + ' docx'
else:
    OP_DOCX = 0

if ('a' in CMDLIST) or ('e' in CMDLIST):
    OP_EPUB = 1
    CMDPRINT = CMDPRINT + ' epub'
else:
    OP_EPUB = 0

if ('a' in CMDLIST) or ('h' in CMDLIST):
    OP_HTML = 1
    CMDPRINT = CMDPRINT + ' html'
else:
    OP_HTML = 0

if ('a' in CMDLIST) or ('m' in CMDLIST):
    OP_MARKDOWN = 1
    CMDPRINT = CMDPRINT + ' markdown'
else:
    OP_MARKDOWN = 0

if ('a' in CMDLIST) or ('p' in CMDLIST):
    OP_PDF = 1
    CMDPRINT = CMDPRINT + ' pdf'
else:
    OP_PDF = 0

if ('a' in CMDLIST) or ('t' in CMDLIST):
    OP_TXT = 1
    CMDPRINT = CMDPRINT + ' plain_text'
else:
    OP_TXT = 0

if ('a' in CMDLIST) or ('x' in CMDLIST):
    OP_XML = 1
    CMDPRINT = CMDPRINT + ' xml'
else:
    OP_XML = 0


ADOCFILE = CONFILE + ".adoc"
XMLFILE = CONFILE + ".xml"
MDFILE = CONFILE + ".md"
EPUBFILE = CONFILE + ".epub"
DOCXFILE = CONFILE + ".docx"
TXTFILE = CONFILE + ".txt"


print(" ---------------------------")
print(CMDPRINT, flush=True)

if OP_XML == 1:
    print(" docbook: ", end='', flush=True)
else:
    print(" Preparing ...", end='', flush=True)
FLAG = subprocess.run(['asciidoc', '-b', 'docbook', ADOCFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if FLAG.returncode == 0:
    print("Done")
else:
    print("FAILED")

if OP_HTML == 1:
    print(" html: ", end='', flush=True)
    FLAG = subprocess.run(["asciidoc", "-b", "html5", ADOCFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_PDF == 1:
    print(" pdf: ", end='', flush=True)
    FLAG = subprocess.run(['dblatex', XMLFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_EPUB == 1:
    print(" epub: ", end='', flush=True)
    FLAG = subprocess.run(['pandoc', '-f', 'docbook', '-t', 'epub', XMLFILE, '-o', EPUBFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_DOCX == 1:
    print(" docx: ", end='', flush=True)
    FLAG = subprocess.run(['pandoc', '--toc', PANDOCDOCX, '-f', 'docbook', '-t', 'docx', XMLFILE, '-o', DOCXFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_TXT == 1:
    print(" txt: ", end='', flush=True)
    FLAG = subprocess.run(['pandoc', ADOCFILE, '-t', 'plain', '-o', TXTFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_MARKDOWN == 1:
    print(" markdown: ", end='', flush=True)
    FLAG = subprocess.run(['pandoc', '-f', 'docbook', '-t', 'markdown_strict', XMLFILE, '-o', MDFILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if FLAG.returncode == 0:
        print("Done")
    else:
        print("FAILED")

if OP_XML == 1:
    print(" docbook: Done")
else:
    FLAG = subprocess.run(['rm', XMLFILE])

print(" ---------------------------")
