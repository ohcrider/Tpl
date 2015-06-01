# -*- coding: utf-8 -*-
'''
    tpl plugin core code
    ~~~~~~~~~
    :copyright: (c) 2015 by fewspider(fewspider@gmail.com).
    :license: BSD, see LICENSE for more details.
'''
import sublime, sublime_plugin, subprocess

class TplCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        dct = self.view.window().extract_variables()
        file_extension = dct.get('file_extension', '')
        file_path = dct.get('file', '')

        settings = sublime.load_settings('Tpl.sublime-settings')
        node_path = settings.get('node_path', '')
        tpl_path = settings.get('tpl_path', '')

        message = ''
        
        if file_extension == 'html':
            message = subprocess.check_output([node_path, tpl_path, file_path], universal_newlines=True)
        else:
            message = 'invalidate file extension:%s' % file_extension
        self.show_console_panel(edit, message)
        
    def show_console_panel(self, edit, message):
        pt = self.view.window().get_output_panel("console_panel")
        pt.set_read_only(False) 
        pt.insert(edit, 0, message)
        pt.set_read_only(True)
        self.view.window().run_command("show_panel", {"panel": "output.console_panel"})