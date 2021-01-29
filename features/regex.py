import re

""" Regex to recognize Markdown formatted elements. """

# Patterns loosely based on two sources. Every pattern is either fully created by us or made through much adaptation.
# - Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later) Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b) Copyright 2004 Manfred Stienstra (the original version)
# - Marko. A markdown parser with high extensibility. Author: Frost Ming <mianghong@gmail.com>

# === BLOCK ELEMENTS ==================================================
# Ordered by precedence: you start with the highest number = highest priority
LINE_START = r'(?<!.)'
LINE_END = r'(?!.)'

CODE_BLOCK_RE = LINE_START + r' {4}.*' + LINE_END 
HTML_BLOCK_RE = r' {0,3}(<[sS][cC][rR][iI][pP][tT]>.*</[sS][cC][rR][iI][pP][tT]>|<[pP][rR][eE]>.*</[pP][rR][eE]>|<[sS][tT][yY][lL][eE]>.*</[sS][tT][yY][lL][eE]>)'
SETEXT_HEADING_RE = LINE_START + r'.*?\n[=-]+[ ]*(\n|(?!.))' + LINE_END
REFERENCE_LIST_RE = LINE_START + r'[ ]{0,3}\[([^\]]*)\]:[ ]*\n?[ ]*([^\s]+)[ ]*\n?[ ]*(([\"\'])(.*)\4|\((.*)\))?[ ]*' + LINE_END
QUOTE_RE = LINE_START + r' {0,3}>( (.|\n.)+|(?!.))(\n\n)?'
HEADING_RE = LINE_START + r' {0,3}(#{1,6})((?=\s)[^\n]*?|[^\n\S]*)(?:(?<=\s)(?<!\\)#+)?[^\n\S]*' + LINE_END
LIST_RE = LINE_START + r' {0,3}(\d{1,9}[.)]|[*\-+])[ \t\n\r\f][^\n\s]*' + LINE_END
FENCED_CODE_RE = r' {0,3}(`{3,}|~{3,})[^\n\S]*((.|\n)*?)( {0,3})(`{3,}|~{3,})'
THEME_BREAK_RE = LINE_START + r' {0,3}([-_*][^\n\S]*){3,}' + LINE_END

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
HTML_RE = r'(<([a-zA-Z/][^<>]*|!--(?:(?!<!--|-->).)*--)>)'
ENTITY_RE = r'(&(?:\#[0-9]+|\#x[0-9a-fA-F]+|[a-zA-Z0-9]+);)'  # ampersands in HTML

# Stand-alone * or _
NOT_STRONG_RE = r'((^|\s)(\*|_)(\s|$))'

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
