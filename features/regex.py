import re

# Patterns loosely based on two sources. Every pattern is either fully created by us or made through much adaptation.
# - Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later) Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b) Copyright 2004 Manfred Stienstra (the original version)
# - Marko. A markdown parser with high extensibility. Author: Frost Ming <mianghong@gmail.com>

# === BLOCK ELEMENTS ==================================================
# Ordered by precedence: you start with the highest number = highest priority

CODE_BLOCK_RE = r'(?<=\n) {4}.*\n?'  # TODO does not detect code block at start of string
HTML_BLOCK_RE = r' {0,3}(<[sS][cC][rR][iI][pP][tT]>.*</[sS][cC][rR][iI][pP][tT]>|<[pP][rR][eE]>.*</[pP][rR][eE]>|<[sS][tT][yY][lL][eE]>.*</[sS][tT][yY][lL][eE]>)'
SETEXT_HEADING_RE = r'(?<=\n).*?\n[=-]+[ ]*(\n|(?!.))'
REFERENCE_LIST_RE = r'(?<=\n) {0,3}(\[(?!\s*\])(?:\\\\|\\[\[\]]|[^\[\]])+\]):\s*(<(?:\\.|[^\n\\<>])*>|[^<\s]\S*)\s*(?:(?<=\s)(\"(?:\\\\|\\\"|[^\"])*\"|\'(?:\\\\|\\\'|[^\'])*\'|\((?:\\\\|\\\)|[^\(\)])*\)))?[^\n\S]*\n?'
QUOTE_RE = r'(?<=\n) {0,3}>( (.|\n.)+|(?!.))(\n\n)?'  # r'(?<=\n) {0,3}>( (.|\n.)+)?(\n\n)?' #r'(?<=\n) {0,3}> ?(.|\n.)*(\n\n)?' #r'(?<=\n) {0,3}>[^\n\S]?(.|\n.)*(\n\n)?'# TODO does not detect quote at start of string
HEADING_RE = r'(?<=\n) {0,3}(#{1,6})((?=\s)[^\n]*?|[^\n\S]*)(?:(?<=\s)(?<!\\)#+)?[^\n\S]*\n?'  # TODO does not detect heading at start of string
LIST_RE = r'(?<=\n) {0,3}(\d{1,9}[.)]|[*\-+])[ \t\n\r\f][^\n\s]*\n?'  # TODO does not detect list items at start of string
FENCED_CODE_RE = r' {0,3}(`{3,}|~{3,})[^\n\S]*((.|\n)*?)( {0,3})(`{3,}|~{3,})'
THEME_BREAK_RE = r'(?<=\n) {0,3}([-_*][^\n\S]*){3,}\n?'  # TODO does not detect theme breaks at start of string

# === INLINE ELEMENTS ==================================================

# --- Builing blocks for the inline elements

NOIMG = r'(?<!\!)'
BRACKETED = r'\[([^\]]*)\]'
LINK_START_RE = NOIMG + BRACKETED
IMAGE_START_RE = r'\!' + BRACKETED
# Matches (<link> "title") or (continuoustext)
LINK_END_RE = r'''\(\s*(?:(<[^<>]*>)\s*(?:('[^']*'|"[^"]*")\s*)?\)|[^\s\)]*\))'''
REFERENCE_END_RE = BRACKETED

# --- Inline elements in order of precedence

# Codespans
#   `e=f()` or ``e=f("`")``
CODESPAN_RE = r'(?:(?<!\\)((?:\\{2})+)(?=`+)|(?<!\\)(`+)(.+?)(?<!`)\2(?!`))'

# Escape formatting
#   \<
ESCAPE_RE = r'\\(.)'

# References 1/2
# Note references are the suggested method for adding links and images for StackOverflow posts.
# If a reference doesn't point to anything, StackOverflow does not recognise nor format it.
#   [Google][3]
REFERENCE_RE = LINK_START_RE + REFERENCE_END_RE

# Links 1/2
#   [text](url) or [text](<url>) or [text](url "title")
LINK_RE = LINK_START_RE + LINK_END_RE

# Images
#   ![alttxt](http://x.com/) or ![alttxt](<http://x.com/>)
IMAGE_LINK_RE = IMAGE_START_RE + LINK_END_RE  # image link
#   ![alt text][2]
IMAGE_REFERENCE_RE = IMAGE_START_RE + REFERENCE_END_RE  # image ref
#   ![ref]
IMAGE_SHORT_REFERENCE_RE = IMAGE_START_RE  # short image ref
INLINE_IMAGE_RE = '(' + IMAGE_LINK_RE + ')|(' + IMAGE_REFERENCE_RE + ')|(' + IMAGE_SHORT_REFERENCE_RE + ')'

# References 2/2
#   [Google]
SHORT_REFERENCE_RE = LINK_START_RE  # short ref

# Links 2/2
#   <http://www.123.com>
AUTOLINK_RE = r'<((?:[Ff]|[Hh][Tt])[Tt][Pp][Ss]?://[^<>]*)>'

# Emails
#   <me@example.com>
AUTOMAIL_RE = r'<([^<> !]*@[^@<> ]*)>'

# Line breaks
#   Two spaces at end of line
LINE_BREAK_RE = r'  \n'

# Direct HTML 
#   <...>
HTML_RE = r'(<([a-zA-Z/][^<>]*|!--(?:(?!<!--|-->).)*--)>)'  # TODO this now finds start tags, end tags, and self-closing tags. Change that a start+end tag pair count as 1.
ENTITY_RE = r'(&(?:\#[0-9]+|\#x[0-9a-fA-F]+|[a-zA-Z0-9]+);)'  # ampersands in HTML

# Stand-alone * or _
NOT_STRONG_RE = r'((^|\s)(\*|_)(\s|$))'  # TODO check if these need attention, it seems they are just ignored

# Asterisks
#   ***strongem*** or ***em*strong**
EM_STRONG_RE = r'(\*)\1{2}(.+?)\1(.*?)\1{2}'
#   ***strong**em*
STRONG_EM_RE = r'(\*)\1{2}(.+?)\1{2}(.*?)\1'
#   **strong*em***
STRONG_EM3_RE = r'(\*)\1(?!\1)([^*]+?)\1(?!\1)(.+?)\1{3}'
#   **strong**
STRONG_RE = r'(\*{2})(.+?)\1'
#   *emphasis*
EMPHASIS_RE = r'(\*)([^\*]+)\1'

# Underscores
#   ___strongem___ or ___em_strong__
EM_STRONG2_RE = r'(_{3})(.+?)\1'
#   __strong__
STRONG2_RE = r'(_{2})(.+?)\1'
#   _emphasis_
EMPHASIS2_RE = r'(_)([^_]+)\1'
