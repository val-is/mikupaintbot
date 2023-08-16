import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk

import keyboard

# read screen

keyboard.wait('b') # TODO make hotkey
# ex:
# keyboard.add_hotkey('a, b', lambda: ...)

screen = Gdk.get_default_root_window().get_screen()
w = screen.get_active_window()
pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
pb.savev("test.png", "png", (), ())

# parse map



# solve map

# click to solve