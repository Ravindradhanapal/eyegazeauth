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
        panel = MainPanel(parent=self)

    def OnInit(self):
        self.SetBackgroundColour('white')
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
        SEGOE_18 = wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')

        boxSizer = wx.BoxSizer(wx.VERTICAL)

        boxSizer.Add((-1, 20))

        # add a hello message to the panel
        headerText = wx.StaticText(self, label="Set eye-gazing password")
        font18 = wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        headerText.SetFont(SEGOE_18)
        boxSizer.Add(headerText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 10))

        infoText = wx.StaticText(self, label="Use your eyes to enter your password")
        font13 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        infoText.SetFont(SEGOE_13)
        boxSizer.Add(infoText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 15))

        instrText = wx.StaticText(self, label="Select the password format of your preference:")
        font12 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        instrText.SetFont(SEGOE_12)
        boxSizer.Add(instrText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 10))

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
        picButton.Bind(wx.EVT_BUTTON, self.openPicturePointsFrame)
        boxSizer.Add(picButton, 0, wx.LEFT, 30)

        self.SetSizer(boxSizer)
        boxSizer.Layout()

    def openPicturePointsFrame(self, event):
        frame = PicturePointsFrame(title="")
        frame.SetSize(wx.Size(700, 600))
        # self.frame_number += 1

    def openNineGridFrame(self, event):
        frame = NineGridFrame(None, wx.ID_ANY, "")
        frame.Show()


class PicturePointsFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.OnInit()
        self.Show()

    def OnInit(self):
        panel = PicturePointsPanel(parent=self)
        self.SetBackgroundColour('white')
        # Blank icon workaround
        bmp = wx.Bitmap(1, 1)
        bmp.SetMaskColour(wx.BLACK)
        icon = wx.Icon(bmp)
        self.SetIcon(icon)


class PicturePointsPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.__do_layout()

    def __do_layout(self):
        SEGOE_12 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        SEGOE_13 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')
        SEGOE_18 = wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI')

        boxSizer = wx.BoxSizer(wx.VERTICAL)

        boxSizer.Add((-1, 20))

        headerText = wx.StaticText(self, label="Set eye-gazing picture points password")
        headerText.SetFont(SEGOE_18)
        boxSizer.Add(headerText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 10))

        infoText = wx.StaticText(self, label="Select a picture to use or choose your own:")
        infoText.SetFont(SEGOE_12)
        boxSizer.Add(infoText, 0, wx.LEFT, 30)

        boxSizer.Add((-1, 5))
        gridSizer = wx.GridSizer(rows=2, cols=3, hgap=5, vgap=5)

        sample1ImgName = curdir + "/images/sample1.jpg"
        sample1Img = wx.Image(sample1ImgName, wx.BITMAP_TYPE_ANY)
        sample1ImgIcon = sample1Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample1ImgIcon = sample1ImgIcon.ConvertToBitmap()
        sample1Button = wx.BitmapButton(self, -1, sample1ImgIcon, style=wx.BORDER_NONE)
        sample1Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample1Img, sample1ImgName))
        gridSizer.Add(sample1Button, 0)

        sample2ImgName = curdir + "/images/sample2.jpg"
        sample2Img = wx.Image(sample2ImgName, wx.BITMAP_TYPE_ANY)
        sample2ImgIcon = sample2Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample2ImgIcon = sample2ImgIcon.ConvertToBitmap()
        sample2Button = wx.BitmapButton(self, -1, sample2ImgIcon, style=wx.BORDER_NONE)
        sample2Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample2Img, sample2ImgName))
        gridSizer.Add(sample2Button, 0)

        sample3ImgName = curdir + "/images/sample3.jpg"
        sample3Img = wx.Image(sample3ImgName, wx.BITMAP_TYPE_ANY)
        sample3ImgIcon = sample3Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample3ImgIcon = sample3ImgIcon.ConvertToBitmap()
        sample3Button = wx.BitmapButton(self, -1, sample3ImgIcon, style=wx.BORDER_NONE)
        sample3Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample3Img, sample3ImgName))
        gridSizer.Add(sample3Button, 0)

        sample4ImgName = curdir + "/images/sample4.jpg"
        sample4Img = wx.Image(sample4ImgName, wx.BITMAP_TYPE_ANY)
        sample4ImgIcon = sample4Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample4ImgIcon = sample4ImgIcon.ConvertToBitmap()
        sample4Button = wx.BitmapButton(self, -1, sample4ImgIcon, style=wx.BORDER_NONE)
        sample4Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample4Img, sample4ImgName))
        gridSizer.Add(sample4Button, 0)

        sample5ImgName = curdir + "/images/sample5.jpg"
        sample5Img = wx.Image(sample5ImgName, wx.BITMAP_TYPE_ANY)
        sample5ImgIcon = sample5Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample5ImgIcon = sample5ImgIcon.ConvertToBitmap()
        sample5Button = wx.BitmapButton(self, -1, sample5ImgIcon, style=wx.BORDER_NONE)
        sample5Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample5Img, sample5ImgName))
        gridSizer.Add(sample5Button, 0)

        sample6ImgName = curdir + "/images/sample6.jpg"
        sample6Img = wx.Image(sample6ImgName, wx.BITMAP_TYPE_ANY)
        sample6ImgIcon = sample6Img.Scale(192, 108, wx.IMAGE_QUALITY_HIGH)
        sample6ImgIcon = sample6ImgIcon.ConvertToBitmap()
        sample6Button = wx.BitmapButton(self, -1, sample6ImgIcon, style=wx.BORDER_NONE)
        sample6Button.Bind(wx.EVT_BUTTON,
                           lambda event: self.openPicturePointsSelectFrame(event, sample6Img, sample6ImgName))
        gridSizer.Add(sample6Button, 0)

        boxSizer.Add(gridSizer, 0, wx.LEFT, 30)
        boxSizer.Add((-1, 30))

        chooseImgButton = wx.Button(self, label="Choose your own", style=wx.BORDER_NONE)
        chooseImgButton.SetBackgroundColour(wx.Colour(200, 200, 200))
        chooseImgButton.SetFont(SEGOE_12)
        chooseImgButton.Bind(wx.EVT_BUTTON, self.onOpenFile)
        boxSizer.Add(chooseImgButton, 0, wx.LEFT, 30)

        self.SetSizer(boxSizer)
        boxSizer.Layout()

    def openPicturePointsSelectFrame(self, event, img, imgName):
        frame = PicturePointsSelectFrame(img=img, imgName=imgName, title="")
        frame.SetSize(wx.Size(img.Width, img.Height))
        #wx.MessageBox("To set your password, click a series of 4 points on the image", " ", wx.OK | wx.ICON_INFORMATION)

    def onOpenFile(self, event):
        wildcard = "Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png|" \
                   "All files (*.*)|*.*"
        # wildcard = "BMP and GIF files (*.bmp;*.gif)|*.bmp;*.gif|PNG files (*.png)|*.png"
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            chosenImg = wx.Image(path, wx.BITMAP_TYPE_ANY)
            self.openPicturePointsSelectFrame(event, chosenImg)
        dlg.Destroy()


class PicturePointsSelectFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, img, imgName, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, pos=(0, 0))
        self.OnInit(img, imgName)
        self.Show()

    def OnInit(self, img, imgName):
        panel = PicturePointsSelectPanel(parent=self, img=img, imgName=imgName)
        self.SetBackgroundColour('white')
        # Blank icon workaround
        bmp = wx.Bitmap(1, 1)
        bmp.SetMaskColour(wx.BLACK)
        icon = wx.Icon(bmp)
        self.SetIcon(icon)
        wx.MessageBox("To set your password, click a series of 4 points on the image", " ", wx.OK | wx.ICON_INFORMATION)


class PicturePointsSelectPanel(wx.Panel):
    selection = []

    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self, parent, img, imgName):
        super().__init__(parent=parent)
        self.img = img
        self.imgName = imgName
        self.bmpImg = self.img.ConvertToBitmap()
        self.sbmpImg = wx.StaticBitmap(self, -1, self.bmpImg, (1, 1), (self.img.GetWidth(), self.img.GetHeight()))
        self.sbmpImg.Bind(wx.EVT_LEFT_DOWN, self.onClick)
        self.selection = []
        self.Show(True)

    def onClick(self, event):
        pos = event.GetPosition()
        self.selection.append(pos)
        dc = wx.MemoryDC(self.bmpImg)
        dc.SetBrush(wx.Brush(wx.GREEN))
        dc.DrawCircle(pos.x, pos.y, 7)
        dc.SelectObject(wx.NullBitmap)
        self.sbmpImg.SetBitmap(self.bmpImg)
        if (len(self.selection) == 4):
            happySelection = wx.MessageDialog(None, "Are you happy with your selection?", " ",
                                              wx.YES | wx.NO | wx.ICON_INFORMATION)
            if happySelection.ShowModal() == wx.ID_NO:
                self.selection = []
                self.bmpImg = self.img.ConvertToBitmap()
                self.sbmpImg.SetBitmap(self.bmpImg)
            else:
                print("Save selection")
                picname_file = open(curdir + "/picturepointsname.txt", "w+")
                picname_file.seek(0)
                picname_file.write(self.imgName)

                self.calcAndSaveGridOffset(self.selection)
                self.GetParent().Close()
                wx.MessageBox("Password has been saved", " ", wx.OK | wx.ICON_INFORMATION)

    def calcAndSaveGridOffset(self, selections):
        pswdFile = open(curdir + "/picturepointspassword.txt", "w+")
        pswdFile.seek(0)
        offsetFile = open(curdir + "/picturepointsoffset.txt", "w+")
        offsetFile.seek(0)

        self.selected_grids = []
        
        for selection in selections:
            
            print("SAVED", selection.x, selection.y)
            gridBoxX = math.ceil(selection.x / GRID_SIZE)
            gridBoxY = math.ceil(selection.y / GRID_SIZE)
            print("SAVED", gridBoxX, gridBoxY)
            self.selected_grids.append(str(gridBoxX) + " " + str(gridBoxY))
            
            # x and y value of the center of the grid box containing this selected point
            gridBoxCenterX = gridBoxX * GRID_SIZE - (math.floor(GRID_SIZE/2))
            gridBoxCenterY = gridBoxY * GRID_SIZE - (math.floor(GRID_SIZE/2))
            offsetX = gridBoxCenterX - selection.x
            offsetY = gridBoxCenterY - selection.y

            offsetFile.write(str(offsetX) + " " + str(offsetY) + '\n')
        
        pswd_hash = sha512_crypt.hash(''.join(self.selected_grids))
        pswdFile.write(pswd_hash)
        sys.exit(0)

class NineGridFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        panel = NineGridPanel(self)
        box_sizer.Add(panel, 1, wx.EXPAND)

        self.SetSizer(box_sizer)
        box_sizer.Fit(self)

        self.SetBackgroundColour('white')

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

        image_labels = os.listdir(self.curdir + '/images/9_grid')

        self.buttons = []
        self.labels = []
        for i in range(9):
            picture_label = image_labels.pop(r.randint(0, len(image_labels) - 1))
            self.labels.append(picture_label)
            pictures = os.listdir(self.curdir + '/images/9_grid/' + picture_label)
            picture_number = pictures.pop(r.randint(0, len(pictures) - 1))

            self.buttons.append(wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(self.curdir + "/images/9_grid/{0}/{1}".format(picture_label, picture_number))))

        # save labels
        with open(curdir + '/9gridlabels.txt', 'w') as f:
            f.write(' '.join(self.labels) + '\n')

        for i in range(9):
            self.buttons[i].SetSize(self.buttons[i].GetBestSize())
            self.buttons[i].Bind(wx.EVT_BUTTON, self.button_handler)
            self.buttons[i].SetLabel(self.labels[i])


        # begin wxGlade: MyFrame.__do_layout
        self.box_sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.box_sizer_1)

        self.grid_sizer_1 = wx.GridBagSizer(5, 5)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, 'Select the first picture')
        self.label_1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Segoe UI'))
        self.grid_sizer_1.Add(self.label_1, (0, 0), (1, 3))

        for i in range(3):
            for j in range(3):
                self.grid_sizer_1.Add(self.buttons[(i * 3) + j], (i + 1, j), (1, 1), 0, 0)

        self.grid_sizer_1.AddGrowableRow(1)
        self.grid_sizer_1.AddGrowableRow(2)
        self.grid_sizer_1.AddGrowableRow(3)
        self.grid_sizer_1.AddGrowableCol(0)
        self.grid_sizer_1.AddGrowableCol(1)
        self.grid_sizer_1.AddGrowableCol(2)
        self.box_sizer_1.Add(self.grid_sizer_1, 0, wx.ALL|wx.EXPAND, 30, 0)

        self.Layout()
        # end wxGlade

    def button_handler(self, event):
        label = event.GetEventObject().GetLabel()
        lst = ['first', 'second', 'third', 'fourth']
        self.selected_pictures.append(label)

        if len(self.selected_pictures) == 4:
            happySelection = wx.MessageDialog(None, "Your password is: " + ' '.join(self.selected_pictures), " ",
                                              wx.YES | wx.NO)
            if happySelection.ShowModal() == wx.ID_NO:
                self.selected_pictures = []
                self.label_1.SetLabel('Select the {s} picture'.format(s=lst[len(self.selected_pictures)]))

                # new random buttons and reset 9gridlabels file
                labels = self.random_buttons()
                with open(curdir + '/9gridlabels.txt', 'w') as f:
                    f.write(' '.join(labels) + '\n')

            else:
                pswd_hash = sha512_crypt.hash(''.join(self.selected_pictures))

                pswd_file = open(curdir + "/9gridpassword.txt", "w+")
                pswd_file.seek(0)
                pswd_file.write(pswd_hash)
                self.GetParent().Close()
                wx.MessageBox("Password has been saved", " ", wx.OK | wx.ICON_INFORMATION)
                sys.exit(0)
        else:
            self.label_1.SetLabel('Select the {s} picture'.format(s=lst[len(self.selected_pictures)]))
            
            labels = self.random_buttons()
            
            with open(curdir + '/9gridlabels.txt', 'a') as f:
                f.write(' '.join(labels) + '\n')

    def random_buttons(self):
        image_labels = os.listdir(self.curdir + '/images/9_grid')
        labels = []
        for button in self.buttons:
            picture_label = image_labels.pop(r.randint(0, len(image_labels) - 1))
            labels.append(picture_label)
            pictures = os.listdir(self.curdir + '/images/9_grid/' + picture_label)
            picture_number = pictures.pop(r.randint(0, len(pictures) - 1))

            button.SetBitmapLabel(wx.Bitmap(self.curdir + "/images/9_grid/{0}/{1}".format(picture_label, picture_number)))
            button.SetLabel(picture_label)
        
        return labels
                





if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
