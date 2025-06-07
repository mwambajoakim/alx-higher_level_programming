#!/usr/bin/python3
"""This module indents text based on specific characters"""


def text_indentation(text):
	"""Indents text after specific characters

		Args:
			text: The text to be indented
	"""
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	special_chars = [".", "?", ":"]
	line = ""
	for t in text:
		line += t
		if t in special_chars:
			print(line.strip())
			print()
			line = ""
	if line:
		print(line.strip(), end="")
