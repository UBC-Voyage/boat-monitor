import pygame
from osmviz.animation import SimViz

class BoatViz(SimViz):
  def __init__(self,label,image,getLatLonAtTimeFunc,
               getAngleAtTimeFunc,time_window,bounding_box,
               drawing_order=0):

    SimViz.__init__(self,drawing_order)
    self.label = label
    self.base_image = pygame.image.load(image)
    self.image = self.base_image
    self.time_window = time_window
    self.bounding_box = bounding_box
    self.getLocationAtTime = getLatLonAtTimeFunc
    self.getAngleAtTime = getAngleAtTimeFunc


  def getTimeInterval(self):
    return self.time_window

  def getBoundingBox(self):
    return self.bounding_box

  def getLabel(self):
    return self.label

  def setState(self,simtime,getXY):
    self.xy = None
    self.image = pygame.transform.rotate(self.base_image, self.getAngleAtTime(simtime)-90)
    self.width = self.image.get_rect().width
    self.height = self.image.get_rect().height
    ll = self.getLocationAtTime(simtime);
    if ll is None:
      return
    x,y = getXY(*ll)
    self.xy = x,y

  def drawToSurface(self,surf):
    if self.xy:
      x,y=self.xy
      w,h = self.width,self.height
      x,y = x-w/2 , y-h/2
      surf.blit(self.image, (x,y))

  def mouseIntersect(self,mousex,mousey):
    if not self.xy:
      return False
    x,y = self.xy
    w,h = self.width,self.height
    return abs(x-mousex)<w/2 and abs(y-mousey)<h/2
