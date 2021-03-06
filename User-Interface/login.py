import math
import os
import wx
import webbrowser
import wx.lib.buttons as buts
import sys
import random as r
from passlib.hash import sha512_crypt

# get current file directory
curdir = os.path.dirname(os.path.realpath(__file__))
GRID_SIZE = 75


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init frame
        self.InitFrame()

    def InitFrame(self):
        frame = MainFrame(parent=None, title="", pos=(100, 100))
        frame.SetSize(wx.Size(600, 500))
        frame.Show()


class MainFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()

    def OnInit(self):
        self.boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('white')

        self.customTitleBar = CustomTitleBar(self)
        self.boxSizer.Add(self.customTitleBar, 0, wx.EXPAND)
        self.customTitleBar.Hide()

        self.panel = MainPanel(parent=self)
        self.boxSizer.Add(self.panel, 1, wx.EXPAND)
        self.panel.Show()

        picturePathFile = open(curdir + "/picturepointsname.txt", "r")
        picturePath = picturePathFile.readline()
        self.image = wx.Image(picturePath, wx.BITMAP_TYPE_ANY)
        self.picturePointsSelectPanel = PicturePointsSelectPanel(parent=self, img=self.image)
        self.boxSizer.Add(self.picturePointsSelectPanel, 1, wx.EXPAND)
        self.picturePointsSelectPanel.Hide()

        self.nineGridPanel = NineGridPanel(self)
        self.boxSizer.Add(self.nineGridPanel, 1, wx.EXPAND)
        self.nineGridPanel.Hide()

        self.SetSizer(self.boxSizer)

        # Blank icon workaround
        bmp = wx.Bitmap(1, 1)
        bmp.SetMaskColour(wx.BLACK)
        icon = wx.Icon(bmp)
        self.SetIcon(icon)


class MainPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.__do_layout()

    def __do_layout(self):
        SEGOE_12 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        SEGOE_13 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        SEGOE_16 = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')

        boxSizer = wx.BoxSizer(wx.VERTICAL)

        boxSizer.Add((-1, 20))

        # add a hello message to the panel
        headerText = wx.StaticText(self, label="Login using the method of your choice")
        headerText.SetFont(SEGOE_16)
        boxSizer.Add(headerText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 20))

        bmp = wx.Image(curdir + "/images/PinButton.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        pinButton = wx.BitmapButton(self, wx.ID_ANY, bmp, style=wx.BORDER_NONE)
        pinButton.SetBackgroundColour(wx.WHITE)
        pinButton.SetWindowStyleFlag(wx.BU_LEFT)
        pinButton.Bind(wx.EVT_BUTTON, self.openNineGridFrame)
        boxSizer.Add(pinButton, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 15))

        bmp = wx.Image(curdir + "/images/PictureButton.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        picButton = wx.BitmapButton(self, -1, bmp, style=wx.BORDER_NONE)
        picButton.SetBackgroundColour(wx.WHITE)
        picButton.Bind(wx.EVT_BUTTON, lambda event: self.openPicturePointsSelectFrame(event))
        boxSizer.Add(picButton, 0, wx.LEFT, 30)

        self.SetSizer(boxSizer)
        boxSizer.Layout()

    def openNineGridFrame(self, event):
        parent = self.GetParent()
        parent.panel.Hide()
        parent.SetWindowStyleFlag(wx.BORDER_NONE)
        parent.customTitleBar.Show()
        parent.customTitleBar.Layout()
        parent.nineGridPanel.Show()
        parent.Fit()
        parent.nineGridPanel.Layout()

    def openPicturePointsSelectFrame(self, event):
        parent = self.GetParent()
        parent.panel.Hide()
        #parent.SetSize(wx.Size(parent.image.Width, parent.image.Height))
        parent.SetWindowStyleFlag(wx.BORDER_NONE)
        parent.customTitleBar.Show()
        parent.customTitleBar.Layout()
        parent.picturePointsSelectPanel.Show()
        parent.Fit()
        parent.picturePointsSelectPanel.Layout()
        parent.Maximize(True)


class PicturePointsSelectPanel(wx.Panel):
    selection = []

    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self, parent, img):
        super().__init__(parent=parent)
        self.img = img
        self.bmpImg = self.img.ConvertToBitmap()
        self.sbmpImg = wx.StaticBitmap(self, -1, self.bmpImg, (1, 1), (self.img.GetWidth(), self.img.GetHeight()))
        self.sbmpImg.Bind(wx.EVT_LEFT_DOWN, self.onClick)
        self.selection = []
        # self.expected = []
        self.offsets = []
        # self.getExpectedPassword()
        self.getOffsets()

    def getOffsets(self):
        offsetsFile = open(curdir + "/picturepointsoffset.txt", "r")
        for i in range(4):
            offset = offsetsFile.readline()
            self.offsets.append(offset.strip())

    def onClick(self, event):
        pos = event.GetPosition()
        self.selection.append(pos)
        parentCustomTitleBar = self.GetParent().customTitleBar
        children = parentCustomTitleBar.sizerTitleBar.GetChildren()
        dotsWidget = children[1].GetWindow()
        if (len(self.selection) == 1):
            dotsWidget.SetLabel("⚫ ⚪ ⚪ ⚪")
        if (len(self.selection) == 2):
            dotsWidget.SetLabel("⚫ ⚫ ⚪ ⚪")
        if (len(self.selection) == 3):
            dotsWidget.SetLabel("⚫ ⚫ ⚫ ⚪")
        if (len(self.selection) == 4):
            dotsWidget.SetLabel("⚫ ⚫ ⚫ ⚫")
            self.selected_grids = []
            pswd_file = open(curdir + "/picturepointspassword.txt", "r")
            file_pswd = pswd_file.read()

            for i in range(4):
                offsetXY = self.offsets[i].split()
                # Move the user's selection closer to the center of the expected grid box
                transformedSelectionX = self.selection[i].x + int(offsetXY[0])
                transformedSelectionY = self.selection[i].y + int(offsetXY[1])
                gridBoxX = math.ceil(transformedSelectionX / GRID_SIZE)
                gridBoxY = math.ceil(transformedSelectionY / GRID_SIZE)
                self.selected_grids.append(str(gridBoxX) + " " + str(gridBoxY))

            if (sha512_crypt.verify(''.join(self.selected_grids), file_pswd)):
                print('Authentication successful')
                sys.exit(0)
            else:
                incorrectSelection = wx.MessageDialog(None,
                                                      "The password entered does not match the one stored. Retry?",
                                                      " ", wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)
                # They want to retry
                if (incorrectSelection.ShowModal() == wx.ID_OK):
                    self.selection = []
                    self.bmpImg = self.img.ConvertToBitmap()
                    self.sbmpImg.SetBitmap(self.bmpImg)
                    dotsWidget.SetLabel("⚪ ⚪ ⚪ ⚪")
                else:
                    self.GetParent().Close()



class NineGridFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        panel = NineGridPanel(self)
        box_sizer.Add(panel, 1, wx.EXPAND)

        self.SetSizer(box_sizer)
        box_sizer.Fit(self)

        # Blank icon workaround
        bmp = wx.Bitmap(1, 1)
        bmp.SetMaskColour(wx.BLACK)
        icon = wx.Icon(bmp)
        self.SetIcon(icon)


class NineGridPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)

        self.curdir = os.path.dirname(os.path.realpath(__file__))
        self.selected_pictures = []

        # get labels
        self.labels = []
        with open(self.curdir + '/9gridlabels.txt', 'r') as f:
            for line in f:
                self.labels.append(line.split())

        self.buttons = []

        for i in range(9):

            # create buttons
            picture_label = self.labels[0][i]
            pictures = os.listdir(self.curdir + '/images/9_grid/' + picture_label)
            picture_number = pictures.pop(r.randint(0, len(pictures) - 1))
            self.buttons.append(wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir + "/images/9_grid/{0}/{1}".format(picture_label, picture_number))))

            # set labels
            self.buttons[i].SetSize(self.buttons[i].GetBestSize())
            self.buttons[i].Bind(wx.EVT_BUTTON, self.button_handler)
            self.buttons[i].SetLabel(picture_label)

        self.box_sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.box_sizer_1)

        self.grid_sizer_1 = wx.GridBagSizer(0, 0)

        for i in range(3):
            for j in range(3):
                self.grid_sizer_1.Add(self.buttons[(i * 3) + j], (i + 1, j), (1, 1), 0, 0)

        self.grid_sizer_1.AddGrowableRow(0)
        self.grid_sizer_1.AddGrowableRow(1)
        self.grid_sizer_1.AddGrowableRow(2)
        self.grid_sizer_1.AddGrowableCol(0)
        self.grid_sizer_1.AddGrowableCol(1)
        self.grid_sizer_1.AddGrowableCol(2)
        self.box_sizer_1.Add(self.grid_sizer_1, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 25, 0)
        self.Layout()
        # end wxGlade

    def button_handler(self, event):
        label = event.GetEventObject().GetLabel()
        self.selected_pictures.append(label)
        parentCustomTitleBar = self.GetParent().customTitleBar
        children = parentCustomTitleBar.sizerTitleBar.GetChildren()
        dotsWidget = children[1].GetWindow()
        
        if len(self.selected_pictures) == 4:
            dotsWidget.SetLabel("⚫ ⚫ ⚫ ⚫")
            pswd_file = open(curdir + "/9gridpassword.txt", "r+")
            file_pswd = pswd_file.read()

            print(self.selected_pictures)

            if (sha512_crypt.verify(''.join(self.selected_pictures), file_pswd)):
                print('Authentication successful')
                sys.exit(0)
            else:
                self.selected_pictures = []
                dotsWidget.SetLabel("⚪ ⚪ ⚪ ⚪")
                wx.MessageBox("Authentication failed", " ", wx.OK | wx.ICON_INFORMATION)

                # go back to first set of pictures
                for i in range(9):
                    picture_label = self.labels[len(self.selected_pictures)][i]
                    pictures = os.listdir(self.curdir + '/images/9_grid/' + picture_label)
                    picture_number = pictures.pop(r.randint(0, len(pictures) - 1))

                    self.buttons[i].SetBitmapLabel(wx.Bitmap(self.curdir + "/images/9_grid/{0}/{1}".format(picture_label, picture_number)))
                    self.buttons[i].SetLabel(picture_label)

        else:
            if (len(self.selected_pictures) == 1):
                dotsWidget.SetLabel("⚫ ⚪ ⚪ ⚪")
            if (len(self.selected_pictures) == 2):
                dotsWidget.SetLabel("⚫ ⚫ ⚪ ⚪")
            if (len(self.selected_pictures) == 3):
                dotsWidget.SetLabel("⚫ ⚫ ⚫ ⚪")
            
            # set next set of buttons
            for i in range(9):
                picture_label = self.labels[len(self.selected_pictures)][i]
                pictures = os.listdir(self.curdir + '/images/9_grid/' + picture_label)
                picture_number = pictures.pop(r.randint(0, len(pictures) - 1))

                self.buttons[i].SetBitmapLabel(wx.Bitmap(self.curdir + "/images/9_grid/{0}/{1}".format(picture_label, picture_number)))
                self.buttons[i].SetLabel(picture_label)


class CustomTitleBar(wx.Panel):
    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)

        # Creating the custom title bar
        self.btnExit = wx.Button(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.panelBody = wx.Panel(self, wx.ID_ANY)
        self.Bind(wx.EVT_BUTTON, self.OnBtnExitClick, self.btnExit)
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        closeImg = wx.Image(curdir + "/images/CloseIcon.png", wx.BITMAP_TYPE_ANY)
        closeImgIcon = closeImg.Scale(13, 13, wx.IMAGE_QUALITY_HIGH)
        closeImgIcon = closeImgIcon.ConvertToBitmap()
        self.btnExit.SetBitmap(closeImgIcon)
        self.btnExit.SetBackgroundColour(wx.WHITE)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        # Sizers:
        self.sizerTitleBar = wx.FlexGridSizer(1, 3, 0, 0)

        # Titlebar:
        self.progressDots = wx.StaticText(self, wx.ID_ANY, "⚪ ⚪ ⚪ ⚪", size=wx.Size(100, -1))
        self.progressDots.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.sizerTitleBar.Add(50, -1)
        self.sizerTitleBar.Add(self.progressDots, 0, wx.ALIGN_CENTER, 0)
        self.sizerTitleBar.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, -20)
        #self.sizerTitleBar.AddGrowableRow(0)
        self.sizerTitleBar.AddGrowableCol(1)

        self.SetSizer(self.sizerTitleBar)
        self.Layout()

    def OnBtnExitClick(self, event):
        self.GetParent().Close()

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
