from fman import DirectoryPaneCommand
from fman.fs import is_dir

class OpenIfDirectory(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor and is_dir(file_under_cursor):
			self.pane.set_path(file_under_cursor)
	def is_visible(self):
		return False