#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Thu Feb 27 22:27:49 2020
#

import wx
import os
from passlib.hash import sha512_crypt

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class NineGridFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        panel = NineGridPanel(self)
        box_sizer.Add(panel, 1, wx.EXPAND)

        self.SetSizer(box_sizer)
        box_sizer.Fit(self)

class NineGridPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)

        self.curdir = os.path.dirname(os.path.realpath(__file__))
        self.selected_pictures = []
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/bicycle/bicycle1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/car/car1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/cat/cat1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/door/door1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_5 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/flower/flower1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_6 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/guitar/guitar1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_7 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/lamp/lamp1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_8 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/moon/moon1.jpg", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_9 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir+ "/images/tree/tree1.jpg", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_1.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_1.SetLabel('bicycle')

        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.bitmap_button_2.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_2.SetLabel('car')

        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.bitmap_button_3.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_3.SetLabel('cat')

        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.bitmap_button_4.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_4.SetLabel('door')

        self.bitmap_button_5.SetSize(self.bitmap_button_5.GetBestSize())
        self.bitmap_button_5.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_5.SetLabel('flower')

        self.bitmap_button_6.SetSize(self.bitmap_button_6.GetBestSize())
        self.bitmap_button_6.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_6.SetLabel('guitar')

        self.bitmap_button_7.SetSize(self.bitmap_button_7.GetBestSize())
        self.bitmap_button_7.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_7.SetLabel('lamp')

        self.bitmap_button_8.SetSize(self.bitmap_button_8.GetBestSize())
        self.bitmap_button_8.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_8.SetLabel('moon')

        self.bitmap_button_9.SetSize(self.bitmap_button_9.GetBestSize())
        self.bitmap_button_9.Bind(wx.EVT_BUTTON, self.button_handler)
        self.bitmap_button_1.SetLabel('tree')
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        self.grid_sizer_1 = wx.GridBagSizer(0, 0)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, 'Select the first picture')
        self.label_1.SetFont(wx.Font(25, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Arial'))
        self.label_1.SetMinSize(wx.Size(600, 39))
        self.grid_sizer_1.Add(self.label_1, (0, 0), (1, 3), wx.ALIGN_LEFT, 0)
        self.grid_sizer_1.Add(self.bitmap_button_1, (1, 0), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_2, (1, 1), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_3, (1, 2), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_4, (2, 0), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_5, (2, 1), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_6, (2, 2), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_7, (3, 0), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_8, (3, 1), (1, 1), 0, 0)
        self.grid_sizer_1.Add(self.bitmap_button_9, (3, 2), (1, 1), 0, 0)
        self.SetSizerAndFit(self.grid_sizer_1)
        self.grid_sizer_1.AddGrowableRow(1)
        self.grid_sizer_1.AddGrowableRow(2)
        self.grid_sizer_1.AddGrowableRow(3)
        self.grid_sizer_1.AddGrowableCol(0)
        self.grid_sizer_1.AddGrowableCol(1)
        self.grid_sizer_1.AddGrowableCol(2)
        self.Layout()
        # end wxGlade    

    def button_handler(self, event):
        label = event.GetEventObject().GetLabel()
        lst = ['first', 'second', 'third', 'fourth']
        self.selected_pictures.append(label)\

        if len(self.selected_pictures) == 4:
            self.label_1.SetLabel('Passwowrd set')
            pswd_hash = sha512_crypt.hash(''.join(self.selected_pictures))
            print("Hash: " + str(pswd_hash))
        else:
            self.label_1.SetLabel('Select the {s} picture'.format(s=lst[len(self.selected_pictures)]))


# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = NineGridFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
