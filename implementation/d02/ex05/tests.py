#!/usr/bin/env python3
# coding: utf-8

import traceback
from elem import Elem, Text


def test_text():
    # What is Text?
    assert isinstance(Text(), str)
    # Default behaviour :
    assert str(Text()) == ''
    # With an argument :
    assert str(Text('')) == ''
    assert str(Text('foo')) == 'foo'
    # Pattern replacing :
    assert str(Text('\n')) == '\n<br />\n'
    assert str(Text('foo\nbar')) == 'foo\n<br />\nbar'
    # Escaping <, >, "...
    assert str(Text('<')) == '&lt;'
    assert str(Text('>')) == '&gt;'
    assert str(Text('"')) == '&quot;'
    print('Text behaviour : OK.')

    
def test_elem_basics():
    # Default behaviour :
    assert str(Elem()) == '<div></div>'
    # Arguments order :
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    # Argument names :
    assert str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')) == '<body>\n  <div></div>\n</body>'
    # With elem as content :
    assert str(Elem(content=Elem())) == '<div>\n  <div></div>\n</div>'
    # With list as content :
    assert str(Elem(content=[Text('foo'), Text('bar'), Elem()])) == '<div>\n  foo\n  bar\n \
 <div></div>\n</div>'
    print('Basic Elem behaviour : OK.')

    
def test_empty_texts():
    assert str(Elem(content=Text(''))) == '<div></div>'
    assert str(Elem(content=[Text(''), Text('')])) == '<div></div>'
    assert str(Elem(content=[Text('foo'), Text(''), Elem()])) == '<div>\n  foo\
\n  <div></div>\n</div>'
    print('Elem with empty texts : OK.')

    
def test_errors():
    # Type error if the content isn't made of Text or Elem.
    try:
        Elem(content=1)
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert str(Elem(content=Text(1))) == '<div>\n  1\n</div>'

    # Type error if the elements of the list aren't Text or Elem instances.
    try:
        Elem(content=['foo', Elem(), 1])
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert (str(Elem(content=[Text('foo'), Elem(), Text(1)]))
            == '<div>\n  foo\n  <div></div>\n  1\n</div>')

    # Same with add_method()
    try:
        elem = Elem()
        elem.add_content(1)
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    
    # Or with lists :
    try :
        elem = Elem()
        elem.add_content([1,])
        raise(Exception('incorrect behaviour'))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)

    # str can't be used :
    try:
        elem = Elem()
        elem.add_content(['',])
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    
    try:
        elem = Elem(content='')
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    print('Error cases : OK.')


def test_embedding():
    assert (str(Elem(content=Elem(content=Elem(content=Elem()))))
            == """<div>
  <div>
    <div>
      <div></div>
    </div>
  </div>
</div>""")
    print('Element embedding : OK.')


def test():
    test_text()
    test_elem_basics()
    test_embedding()
    test_empty_texts()
    test_errors()
    
if __name__ == '__main__':
    try :
        test()
        print('Tests succeeded!')
    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print('Tests failed!')
