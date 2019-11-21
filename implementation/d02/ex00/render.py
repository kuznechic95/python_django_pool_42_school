#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import sys
import os
import re


class ReadFile:
	"""read files and checks errors for reading"""
	def __init__(self, filename):
		self.filename = filename
		self.file_str = None

	def read_file(self):
		try:
			with open(self.filename) as file:
				self.file_str = file.read()
		except FileNotFoundError as e:
			print('File "{}" does not exist. Error: {}'.format(e.filename, e))
			sys.exit(1)
		except PermissionError as e:
			print('You do not have enough permission for reading file "{}". Error: {}'.format(e.filename, e))
			sys.exit(1)
		except IsADirectoryError as e:
			# os.path.isfile()
			print('The "{}" is a directory, but must be file. Error: {}'.format(e.filename, e))
			sys.exit(1)
		except Exception as e:
			print('Unknown error while reading file "{}". Error: {}'.format(self.filename, e))
			sys.exit(1)


class Render(ReadFile):
	"""inherits ReadFile. reads template file while initializing. returns str that contains file data
		gets settings dictionary while initializing
		in write_html replaces keys in *.template with values from setting.py (using settings dictionary)
	"""
	def __init__(self, template_filename, settings_filename):
		super().__init__(template_filename)
		self.param_dict = Settings(settings_filename).param_dict

	def process_line(self, line):
		html_line = line
		# print(self.param_dict)
		for key in self.param_dict:
			html_line = html_line.replace("{" + key + "}", self.param_dict[key])
		return html_line

	def write_html(self, html_filename):
		# print(self.param_dict)
		self.read_file()
		# print(self.file_str)
		line_list = self.file_str.split('\n')
		# print(line_list)
		try:
			with open(html_filename, "w") as file_html:
				for line in line_list:
					html_line = self.process_line(line)
					file_html.write("".join((html_line, "\n")))
		except FileNotFoundError as e:
			print('File "{}" does not exist. Error: {}'.format(e.filename, e))
			sys.exit(1)
		except PermissionError as e:
			print('You do not have enough permission for writing file "{}". Error: {}'.format(e.filename, e))
			sys.exit(1)
		except Exception as e:
			print('Unknown error while writing file "{}". Error: {}'.format(file_html, e))
			sys.exit(1)


class Settings(ReadFile):
	"""inherits ReadFile. reads settings file while initializing. returns str that contains file data"""
	def __init__(self, filename):
		super().__init__(filename)
		self.param_dict = dict()
		self.process_file()

	def process_file(self):
		self.read_file()
		line_list = self.file_str.split('\n')
		line_list = filter(None, line_list)
		# print('line_list={}'.format(line_list))
		for line in line_list:
			cat__value = line.split("=")
			self.param_dict[cat__value[0].strip(" ")] = cat__value[1].strip("\" \n")


def render():
	"""analyzes arg number, extension; creates name for output .html file; calls main class"""
	if len(sys.argv) != 2:
		print("usage: render.py <file_name>.template")
		sys.exit(1)
	filename = sys.argv[1]
	# filename = "myCV.template"
	if re.match("\w+.template", filename):
		file, file_extension = os.path.splitext(filename)
		settings_filename = "settings.py"
		if file_extension == ".template":
			render_instance = Render(filename, settings_filename)
			render_instance.write_html(file + ".html")
	else:
		print('Error: file "{}" must have *.template file extension'.format(filename))

if __name__ == '__main__':
	render()
