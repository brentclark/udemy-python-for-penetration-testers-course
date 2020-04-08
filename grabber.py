#import wx
import pyscreenshot as ImageGrab

#import os
import ftplib
im = ImageGrab.grab(backend='gnome-screenshot')
im.save('/tmp/grabbed.png')

# w      = wx.App()
# screen = wx.ScreenDC()
# size   = screen.GetSize()
# bmap   = wx.Bitmap(size[0], size[1])
# memo   = wx.MemoryDC(bmap)
# memo.Blit(0,0,size[0],size[1],screen,0,0)

# del memo

# bmap.SaveFile("/tmp/grabbed.png", wx.BITMAP_TYPE_PNG)

ftpsession = ftplib.FTP("10.0.0.104", "admin", 'password')
file_      = open("/tmp/grabbed.png", 'rb')
ftpsession.storbinary("STOR/tmp/grabbed.png", file_)

file_.close()
ftpsession.quit()