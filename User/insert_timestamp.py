#coding=utf-8

import datetime
import sublime_plugin

class insert_timestamp(sublime_plugin.TextCommand):
  def run(self, edit):

    # el u del davant defineix la string com a unicode
    # http://www.sublimetext.com/forum/viewtopic.php?f=3&t=7114
    timestamp_str = u'# Dídac # ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #for region in the selection
    #(i.e. if you have multiple regions selected,
    # insert the timestamp in all of them)
    for r in self.view.sel():
      #put in the timestamp
      #(if text is selected, it'll be
      # replaced in an intuitive fashion)
      if r.size() > 0:
        self.view.replace(edit, r, timestamp_str)
      else:
        self.view.insert(edit, r.begin(), timestamp_str)