import wx 
import wx.html2 
import requests
class whBrowser(wx.Dialog): 
  def __init__(self, *args, **kwds): 
    wx.Dialog.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    sizer.Add(self.browser, 1, wx.EXPAND, 10) 
    self.SetSizer(sizer) 
    self.SetSize((350, 480)) 

if __name__ == '__main__': 
  window = wx.App() 
  dialog = whBrowser(None, -1) 
  dialog.browser.LoadURL("http://music.163.com/style/swf/widget.swf?sid=2602222983&type=0&auto=0&width=310&height=430")
  dialog.Show() 
  window.MainLoop() 