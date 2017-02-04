# -*- coding: utf-8 -*-

import gtk, socket, gobject

hosts = []
Accept_Language = []
Accept_Encoding = []
User_Agent = []
Accept = []
Referer = []
Connection = []
Method = []
HTTP_Version = []
Get_Method = []
Cache_Control = []
Cookie = []
DNT = []


with open('Stalker.log', 'rb') as file:
    raw_data = file.readlines()
    file.close()
    for i in raw_data:
        if 'Host:' in i:
            host = i[5:].strip().replace(" ", '')
            hosts.append(host)
        if 'Accept-Language:' in i:
            ac = i[17:].strip()
            Accept_Language.append(ac)
        if 'GET' in i:
            Method.append('GET')
            Get_Method.append(i[4:].strip().replace("HTTP/1.1", ''))
        if 'HTTP/1.1' in i:
            HTTP_Version.append('HTTP/1.1')
        if 'Accept-Encoding:' in i:
            Accept_Encoding.append(i[17:].strip())
        if 'Accept:' in i:
            Accept.append(i[8:].strip())
        if 'User-Agent:' in i:
            User_Agent.append(i[12:].strip())
        if 'DNT:' in i:
            DNT.append(i[4:].strip())
        if 'Connection:' in i:
            Connection.append(i[11:].strip())
        if 'Referer:' in i:
            Referer.append(i[9:].strip())
        if 'Cache-Control:' in i:
            Cache_Control.append(i[14:].strip())
        if 'Cookie:' in i:
            Cookie.append(i[7:].strip())


print(hosts)


class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Web Stalker")
      self.set_size_request(400,600)
      self.set_position(gtk.WIN_POS_CENTER)
      vbox = gtk.VBox(False, 5)
      scw = gtk.ScrolledWindow(None, None)
      
      data_store = gtk.TreeStore(str, str)

      len_hosts = len(hosts)
      for i in range(len_hosts):
          try:
              try:
                  row = data_store.append(None,[Method[i], hosts[i]])
                  data_store.append(row, ['HTTP Version:', HTTP_Version[i]])
                  data_store.append(row, ['Request:', Get_Method[i]])
                  data_store.append(row, ['User-Agent:', User_Agent[i]])
                  data_store.append(row, ['Referer:', Referer[i]])
                  data_store.append(row, ['Cookie:', Cookie[i]])
                  data_store.append(row, ['Accept-Language:', Accept_Language[i]])
                  data_store.append(row, ['Accept-Encoding:', Accept_Encoding[i]])
                  data_store.append(row, ['Connection', Connection[i]])
                  data_store.append(row, ['Accept:', Accept[i]])
                  data_store.append(row, ['DNT:', DNT[i]])
              except IndexError: pass
          except UnboundLocalError: pass

      data_tree_view = gtk.TreeView(data_store)

      for i, colt in enumerate(["Method", "Address"]):
          renderer = gtk.CellRendererText()
          column = gtk.TreeViewColumn(colt, renderer, text=i)
          fro = data_tree_view.append_column(column)
          scw.add(data_tree_view)
          vbox.add(scw)

      gobject.threads_init()
      self.add(vbox)
      self.connect("destroy", gtk.main_quit)
      self.show_all()

PyApp()
gtk.main()