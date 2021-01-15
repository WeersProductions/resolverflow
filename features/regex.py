import re

# Patterns based on two sources. Many alterations have been made.
# - Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later) Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b) Copyright 2004 Manfred Stienstra (the original version)
# - Marko. A markdown parser with high extensibility. Author: Frost Ming <mianghong@gmail.com>


# === BLOCK ELEMENTS ==================================================
# Precedence: you start with the highest number = highest priority

    # 1
    # Paragraph
    # 2
    # 3
    # 4
    # CodeBlock
    # 5
    # HTMLBlock
    # SetextHeading
    # ListItem
    # LinkRefDef
    # BlankLine
    # Document = virtual
    # 6
    # Quote
    # Heading
    # List
    # 7
    # FencedCode
    # 8
    # ThematicBreak

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
#   [Google][3]
REFERENCE_RE = re.compile(LINK_START_RE + REFERENCE_END_RE, re.DOTALL | re.UNICODE)

# Links 1/2
#   [text](url) or [text](<url>) or [text](url "title")
LINK_RE = re.compile(LINK_START_RE + LINK_END_RE, re.DOTALL | re.UNICODE)

# Images
#   ![alttxt](http://x.com/) or ![alttxt](<http://x.com/>)
IMAGE_LINK_RE = IMAGE_START_RE + LINK_END_RE # image link
#   ![alt text][2]
IMAGE_REFERENCE_RE = IMAGE_START_RE + REFERENCE_END_RE  # image ref
#   ![ref]
SHORT_IMAGE_REFERENCE_RE = IMAGE_START_RE # short image ref
INLINE_IMAGE_RE = '(' + IMAGE_LINK_RE + ')|(' + IMAGE_REFERENCE_RE + ')|(' + SHORT_IMAGE_REFERENCE_RE + ')'

# References 2/2
#   [Google]
SHORT_REFERENCE_RE = LINK_START_RE # short ref

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
HTML_RE = r'(<([a-zA-Z/][^<>]*|!--(?:(?!<!--|-->).)*--)>)' #TODO this now finds start tags, end tags, and self-closing tags. Change that a start+end tag pair count as 1.
ENTITY_RE = r'(&(?:\#[0-9]+|\#x[0-9a-fA-F]+|[a-zA-Z0-9]+);)' # ampersands in HTML

# Stand-alone * or _
NOT_STRONG_RE = r'((^|\s)(\*|_)(\s|$))' #TODO check if these need attention, it seems they are just ignored

# Asterisks
#   ***strongem*** or ***em*strong**
EM_STRONG_RE = re.compile(r'(\*)\1{2}(.+?)\1(.*?)\1{2}', re.DOTALL | re.UNICODE)
#   ***strong**em*
STRONG_EM_RE = re.compile(r'(\*)\1{2}(.+?)\1{2}(.*?)\1', re.DOTALL | re.UNICODE)
#   **strong*em***
STRONG_EM3_RE = re.compile(r'(\*)\1(?!\1)([^*]+?)\1(?!\1)(.+?)\1{3}', re.DOTALL | re.UNICODE)
#   **strong**
STRONG_RE = re.compile(r'(\*{2})(.+?)\1', re.DOTALL | re.UNICODE)
#   *emphasis*
EMPHASIS_RE = re.compile(r'(\*)([^\*]+)\1', re.DOTALL | re.UNICODE)

# Underscores
#   ___strongem___ or ___em_strong__
EM_STRONG2_RE = re.compile(r'(_{3})(.+?)\1', re.DOTALL | re.UNICODE)
#   __strong__
STRONG2_RE = re.compile(r'(_{2})(.+?)\1', re.DOTALL | re.UNICODE)
#   _emphasis_
EMPHASIS2_RE = re.compile(r'(_)([^_]+)\1', re.DOTALL | re.UNICODE)



