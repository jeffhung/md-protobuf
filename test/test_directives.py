import pytest
from md_protobuf.generator import titlize_directives

@pytest.mark.parametrize("text,expected", [
# ------------------------------------
( """@description""" ,
"""
**Description**
""" ),
# ------------------------------------
( """@description""" ,
"""
**Description**
""" ),
# ------------------------------------
( """@description""" ,
"""
**Description**
""" ),
# ------------------------------------
( """
@description""" ,
"""

**Description**
""" ),
# ------------------------------------
( """

@description""" ,
"""


**Description**
""" ),
# ------------------------------------
( """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.
@description
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.

**Description**

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
# ------------------------------------
( """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.

@description
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.


**Description**

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
# ------------------------------------
( """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.
@description

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.

**Description**


Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
# ------------------------------------
( """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.

@description

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.


**Description**


Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
# ------------------------------------
( """@table FOO_BAR""" ,
"""
**Table**: `FOO_BAR`
""" ),
# ------------------------------------
( """
@table FOO_BAR""" ,
"""

**Table**: `FOO_BAR`
""" ),
# ------------------------------------
( """
@table FOO_BAR
""" ,
"""

**Table**: `FOO_BAR`

""" ),
# ------------------------------------
( """@table FOO_BAR
@search_index foo_bar""" ,
"""
**Table**: `FOO_BAR`


**Search Index**: `foo_bar`
""" ),
# ------------------------------------
( """
@table FOO_BAR
@search_index foo_bar""" ,
"""

**Table**: `FOO_BAR`


**Search Index**: `foo_bar`
""" ),
# ------------------------------------
( """
@table FOO_BAR

@search_index foo_bar""" ,
"""

**Table**: `FOO_BAR`



**Search Index**: `foo_bar`
""" ),
# ------------------------------------
])
def test_titlize_directives(text, expected):
    result = titlize_directives(text)
    assert result == expected

