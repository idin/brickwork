from IPython.core import display as core


def display_url(url, text):
	result = core.HTML(f'<a href="{url}">{text}</a>')
	try:
		display(result)
	except:
		pass

	return result
