import pytest
from md_protobuf.generator import first_sentence

@pytest.mark.parametrize("expected,text", [
# first sentence in same line
( "", "" ),
( "foo.", "foo." ),
( "foo", "foo" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
"""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
"""Lorem Ipsum is simply dummy text of the printing and typesetting
industry.  Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting
industry.  Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting",
"""
Lorem Ipsum is simply dummy text of the printing and typesetting
@see http://example.com""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting",
"""Lorem Ipsum is simply dummy text of the printing and typesetting
@see http://example.com""" ),
( "",
"""@see http://example.com
Lorem Ipsum is simply dummy text of the printing and typesetting""" ),
( "",
"""
@see http://example.com
Lorem Ipsum is simply dummy text of the printing and typesetting""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
"""Lorem Ipsum is simply dummy text of the printing and typesetting
industry

Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book.""" ),
( "The language code as in `foo.h`",
"""The language code as in `foo.h`""" ),
( "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
"""Lorem Ipsum is simply dummy text of the printing and typesetting industry.""" ),
    ])
def test_first_sentence(expected, text):
    result = first_sentence(text)
    assert result == expected

