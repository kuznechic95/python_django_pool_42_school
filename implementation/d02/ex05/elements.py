#!/usr/bin/python3
# -*-coding:utf-8 -*-

from elem import Elem, Text

class Html(Elem):

	def __init__(self, content=None, attr=dict(), tag='html', tag_type='double'):
		"""
		__init__() method.
		"""
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Head(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='head', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Body(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='body', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Title(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='title', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Meta(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='meta', tag_type='simple'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Img(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='img', tag_type='simple'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Table(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='table', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Th(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='th', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Tr(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='tr', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Td(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='td', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Ul(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='ul', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Ol(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='ol', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Li(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='li', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class H1(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='h1', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class H2(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='h2', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class P(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='p', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Div(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='div', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Span(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='span', tag_type='double'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Hr(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='hr', tag_type='simple'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


class Br(Elem):
	"""
	__init__() method.
	"""
	def __init__(self, content=None, attr=dict(), tag='br', tag_type='simple'):
		# print('tag={} type={}, attr={} type={}, content={} type={}'.format(tag, \
		# 	type(tag), attr, type(attr), content, type(content)))
		super().__init__(tag, attr, content, tag_type)


if __name__ == '__main__':
	e = Html([Head(Text('head_text')), Body(Text('body_text'))])
	print(e)