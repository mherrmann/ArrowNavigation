from fman import DirectoryPaneCommand
from fman.fs import is_dir

class OpenIfDirectory(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			if is_dir(file_under_cursor):
				self.pane.set_path(file_under_cursor)
			elif file_under_cursor[-4:]==".zip":
				self.pane.run_command("open")
	def is_visible(self):
		return False
