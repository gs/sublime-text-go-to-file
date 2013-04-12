import sublime, sublime_plugin
import os, string
import re

class GoToFile(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            # Collect the texts that may possibly be filenames
            quoted_text = self.get_quoted_selection(region).split(os.sep)[-1]
            selected_text = self.get_selection(region)
            whole_line = self.get_line(region)
            clipboard = sublime.get_clipboard().strip()

            candidates = [quoted_text, selected_text, whole_line, clipboard]
            for text in candidates:
                if len(text) == 0:
                    continue

                self.potential_files = self.get_filename(text)
                if len(self.potential_files) > 0:
                    break

            if len(self.potential_files) > 1:
                self.view.window().show_quick_panel(self.potential_files, self.open_file)
            elif len(self.potential_files) == 1:
                print("Opening file '%s'" % (self.potential_files[0]))
                self.view.window().open_file(self.potential_files[0])
            else:
                sublime.error_message("No file found!")

    def open_file(self, selected_index):
        if selected_index != -1:
            file = self.potential_files[selected_index]
            print("Opening file '%s'" % (file))
            self.view.window().open_file(file)

    def get_selection(self, region):
        return self.view.substr(region).strip()

    def get_line(self, region):
        return self.view.substr(self.view.line(region)).strip()

    def get_quoted_selection(self, region):
        text = self.view.substr(self.view.line(region))
        position = self.view.rowcol(region.begin())[1]
        quoted_text = self.expand_within_quotes(text, position, '"')
        if not quoted_text:
            quoted_text = self.expand_within_quotes(text, position, '\'')
        return quoted_text

    def expand_within_quotes(self, text, position, quote_character):
        open_quote = text.rfind(quote_character, 0, position)
        close_quote = text.find(quote_character, position)
        return text[open_quote+1:close_quote] if (open_quote > 0 and close_quote > 0) else ''

    def get_filename(self, text):
        results = []
        directories = self.view.window().folders()
        for directory in directories:
            for dirname, _, files in self.walk(directory):
                for file in files:
                    if re.search(text, file):
                        results += [dirname + os.sep + file]
        return results

    def walk(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files
