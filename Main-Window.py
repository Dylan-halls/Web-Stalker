# -*- coding: utf-8 -*-

import gtk, gobject, os, webkit

hosts = []
Accept_Language = []
Accept_Encoding = []
Source_Address = []
typ = []
Dst_Address = []
Source_Port = []
Dst_Port = []
Load = []
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

Status_Line = []
Age = []
E_Tag = []
Location = []
Proxy_Authenticate = []
Retry_After = []
Server = []
Vary = []
WWW_Authenticate = []
Cache_Control = []
Connection = []
Date = []
Pragma = []
Trailer = []
Transfer_Encoding = []
Upgrade = []
Via = []
Warning = []
Keep_Alive = []
Allow = []
Content_Encoding = []
Content_Language = []
Content_Length = []
Content_Location = []
Content_MD5 = []
Content_Range = []
Content_Type = []
Expires = []
Last_Modified = []
Headers = []
Additional_Headers = []

with open('Stalker.log', 'r') as file:
    raw_data = file.readlines()
    file.close()
    for i in raw_data:
        
        #Request list makers
        
        if 'Host:' in i:
            host = i[5:].strip().replace(" ", '')
            hosts.append(host)
        if 'Accept-Language:' in i:
            ac = i[17:].strip()
            Accept_Language.append(ac)
        if 'GET' in i:
            Method.append('GET')
            Get_Method.append(i[4:].strip().replace("HTTP/1.1", ''))
        if 'POST' in i:
            Method.append('POST')
            Get_Method.append(i[5:].strip().replace("HTTP/1.1", ''))
        if 'Load:' in i:
            Load.append(i[6:].strip())
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
        if 'Source-Address:' in i:
            Source_Address.append(i[16:].strip())
        if 'Destination-Address:' in i:
            Dst_Address.append(i[21:].strip())
        if 'Destination_Port:' in i:
            Dst_Port.append(i[17:].strip())
        if 'Source_Port:' in i:
            Source_Port.append(i[13:].strip())
        if 'HTTP-Type:' in i:
            typ.append(i[11:])
        
        #Responce list makers
        
        if "HTTP/1.1 " in i:
            Status_Line.append(i)
        if "Age:" in  i:
            Age.append(i[5:])
        if "ETag" in i:
            E_Tag.append(i[7:])
        if "Location" in i:
            Location.append(i[10:])
        if "Proxy-Authenticate" in i:
            Proxy_Authenticate.append(i[20:])
        if "Retry-After" in i:
            Retry_After.append(i[13:])
        if "Server" in i:
            Server.append(i[8:])
        if "Vary" in i:
            Vary.append(i[6:])
        if "WWW-Authenticate" in i:
            WWW_Authenticate.append(i[18:])
        if "Cache-Control" in i:
            Cache_Control.append(i[15:])
        if "Connection" in i:
            Connection.append(i[12:])
        if "Date: " in i:
            Date.append(i[6:])
        if "Pragma" in i:
            Pragma.append(i[8:])
        if "Trailer" in i:
            Trailer.append(i[9:])
        if "Transfer-Encoding" in i:
            Transfer_Encoding.append(i[19:])
        if "Upgrade" in i:
            Upgrade.append(i[9:])
        if "Via" in i:
            Via.append(i[5:])
        if "Warning" in i:
            Warning.append(i[9:])
        if "Keep-Alive" in i:
            Keep_Alive.append(i[12:])
        if "Allow" in i:
            Allow.append(i[7:])
        if "Content-Encoding" in i:
            Content_Encoding.append(i[18:])
        if "Content-Language" in i:
            Content_Language.append(i[18:])
        if "Content-Length" in i:
            Content_Length.append(i[16:])
        if "Content-Location" in i:
            Content_Location.append(i[18:])
        if "Content-MD5" in i:
            Content_MD5.append(i[11:])
        if "Content-Range" in i:
            Content_Range.append(i[15:])
        if "Content-Type" in i:
            Content_Type.append(i[14:])
        if "Expires" in i:
            Expires.append(i[9:])
        if "Last-Modified" in i:
            Last_Modified.append(i[15:])
        if "Headers" in i:
            Headers.append(i[9:])
        if "Additional-Headers" in i:
            Additional_Headers.append(i[20:])

class PyApp(gtk.Window):
   
   def open_window(self, url):
      url = address_bar.get_text()
      os.system('python Web-Window.py '+url)

   def passer(self):
      web = webkit.WebView()
      try:
        web.open(address_bar.get_text())
      except NameError: pass
      return web
   
   def saver(self, text):
      file_name = save_bar.get_text()
      start_iter = textbuffer.get_start_iter()
      end_iter = textbuffer.get_end_iter()
      file_data = textbuffer.get_text(start_iter, end_iter, True)  
      with open(file_name, 'w') as file:
         file.write(file_data)
         file.close()

   def __init__(self):
      global address_bar, save_bar, TextBox1, textbuffer
      super(PyApp, self).__init__()
      web = webkit.WebView()
      self.set_icon_from_file('stalker-icon.jpg')
      self.set_title("Web Stalker")
      self.set_size_request(1000,600)
      self.set_position(gtk.WIN_POS_CENTER)

      vbox = gtk.VBox(False, 5)
      hbox = gtk.HBox()
      whbox = gtk.HBox()

      la = gtk.Label()
      la.set_markup('<big><b>Web Stalker</b></big>\n  <small><b>Version: 1.0.0</b></small>')
      whbox.add(la)

      addr_b = gtk.Label()
      addr_b.set_markup('<b>Website: </b>')

      sav_f_as = gtk.Label()
      sav_f_as.set_markup('<b>Save As: </b>')

      save_bar = gtk.Entry()
      #save_bar.set_text('File Name')

      vbox.pack_start(hbox)
      
      TextBox1 = gtk.TextView()
      textbuffer = TextBox1.get_buffer()
      notee = gtk.ScrolledWindow(None, None)
      notee.add(TextBox1)

      hbox.pack_start(whbox)
      hbox.pack_start(notee)
      
      navigation = gtk.HBox()
      fs = gtk.HBox()
      save = gtk.ToolButton(gtk.STOCK_SAVE)
      save.connect('clicked', self.saver)
      fs.pack_start(sav_f_as, False)
      fs.pack_start(save_bar)
      fs.pack_start(save, False)
      forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
      forward.connect('clicked', self.open_window)
      address_bar = gtk.Entry()
      #address_bar.set_text('Address')
      navigation.pack_start(addr_b, False)
      navigation.pack_start(address_bar)
      navigation.pack_start(forward, False)
      vbox.pack_start(fs, False)
      vbox.pack_start(navigation, False)
      address_bar.connect('activate', self.passer)
      
      scw = gtk.ScrolledWindow(None, None)
      
      data_store = gtk.TreeStore(str, str, str)

      len_hosts = len(hosts)
      for i in range(len_hosts):
          try:
              try:
                  if typ[i] == 'HTTP Request\n':
                      row = data_store.append(None,['HTTP Request', Method[i], hosts[i]])
                      data_store.append(row, ['', 'Source Mac:', Source_Address[i]])
                      data_store.append(row, ['', 'Destination Mac:', Dst_Address[i]])
                      data_store.append(row, ['', 'Source Port:', Source_Port[i]])
                      data_store.append(row, ['', 'Destination Port:', Dst_Port[i]])
                      data_store.append(row, ['', '         HTTP Version:', HTTP_Version[i]])
                      data_store.append(row, ['', '         Request:', Get_Method[i]])
                      if Method[i] == 'POST':
                          data_store.append(row, ['', '         Load:', Load[i]])
                      data_store.append(row, ['', '         User-Agent:', User_Agent[i]])
                      data_store.append(row, ['', '         Referer:', Referer[i]])
                      data_store.append(row, ['', '         Cookie:', Cookie[i]])
                      data_store.append(row, ['', '         Accept-Language:', Accept_Language[i]])
                      data_store.append(row, ['', '         Accept-Encoding:', Accept_Encoding[i]])
                      data_store.append(row, ['', '         Connection', Connection[i]])
                      data_store.append(row, ['', '         Accept:', Accept[i]])
                      data_store.append(row, ['', '         DNT:', DNT[i]])
              except IndexError: pass
          except UnboundLocalError: pass

      len_r = len(Status_Line)
      for o in range(len_r):
        try:
            if typ[o] == 'HTTP Responce\n':
                row = data_store.append(None,['HTTP Responce', '', Source_Address[o]])
                data_store.append(row, ['', 'Source Mac:', Source_Address[o]])
                data_store.append(row, ['', 'Destination Mac:', Dst_Address[o]])
                data_store.append(row, ['', 'Source Port:', Source_Port[o]])
                data_store.append(row, ['', 'Destination Port:', Dst_Port[o]])
                data_store.append(row, ['', '         Status-Line:', Status_Line[o].strip()])
                data_store.append(row, ['', '         Server:', Server[o].strip()])
                data_store.append(row, ['', '         Via:', Via[o].strip()])
                data_store.append(row, ['', '         Location:', Location[o].strip()])
                data_store.append(row, ['', '         Content-Length:', Content_Length[o].strip()])

        except IndexError: pass

      data_tree_view = gtk.TreeView(data_store)

      for i, colt in enumerate(["Type", "Method", "Address"]):
          renderer = gtk.CellRendererText()
          renderer.set_property("background", "white")
          renderer.set_property("foreground", "black")
          renderer.set_property('editable', True)
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