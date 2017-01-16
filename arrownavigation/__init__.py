from fman import DirectoryPaneCommand
from os.path import isdir, realpath

class OpenDirectory(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor and isdir(file_under_cursor):
			self.pane.set_path(realpath(file_under_cursor))