import gtk, webkit, gobject, sys

class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Web Stalker Browser")
      self.set_size_request(1000,600)
      self.set_position(gtk.WIN_POS_CENTER)
      vbox = gtk.VBox(False, 5)
      scw = gtk.ScrolledWindow(None, None)
      web = webkit.WebView()

      url = sys.argv[1]
      web.open(url)
      scw.add(web)
      vbox.add(scw)

      gobject.threads_init()
      self.add(vbox)
      self.connect("destroy", gtk.main_quit)
      self.show_all()

if __name__ == '__main__':
	PyApp()
	gtk.main()