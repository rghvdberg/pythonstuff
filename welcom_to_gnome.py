# from https://developer.gnome.org/gnome-devel-demos/stable/window.py.html.en
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys


class MyApplication(Gtk.Application):

    def do_activate(self):
        window = Gtk.Window(application=self)
        window.set_title("Welcom to GNOME")
        window.show_all()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
