import pygame
from osmviz.animation import SimViz

class LineViz(SimViz):
  """
 LineViz draws a line between two (optionally moving) locations.
  """

  def __init__(self, getLocAtTime1, getLocAtTime2,
               linecolor=pygame.Color("red"), linewidth=3,
               drawingOrder=0):
    """
    getLocAtTime 1 and 2 represent the location of the 1st and 2nd
    endpoint of this lasso, respectively. They should take a single
    argument (time) and return the (lat,lon) of that endpoint.
    """
    SimViz.__init__(self, drawingOrder);
    self.xy1 = None
    self.xy2 = None
    self.linecolor = linecolor
    self.linewidth = linewidth
    self.getLoc1 = getLocAtTime1
    self.getLoc2 = getLocAtTime2

  def setState(self, simtime, getXY):
    self.xy1 = getXY(*self.getLoc1(simtime))
    self.xy2 = getXY(*self.getLoc2(simtime))

  def drawToSurface(self, surf):
    pygame.draw.line(surf, self.linecolor, self.xy1, self.xy2,
                     self.linewidth)

  ## So long as we are passing LassoViz's in as part of the scene_viz
  ## list to a Simulation, we don't need to implement the getLabel,
  ## getBoundingBox, or mouseIntersect methods.
