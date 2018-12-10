import pygame
from osmviz.animation import SimViz

HUD_BG = pygame.Color(200, 200, 200)
BLACK = pygame.Color(0, 0, 0)

class HudViz(SimViz):
  """
 LineViz draws a line between two (optionally moving) locations.
  """

  def __init__(self, getHudTextFunc, font=None,
               fontsize=12, drawingOrder=0):
    """
    getLocAtTime 1 and 2 represent the location of the 1st and 2nd
    endpoint of this lasso, respectively. They should take a single
    argument (time) and return the (lat,lon) of that endpoint.
    """
    SimViz.__init__(self, drawingOrder);

    pygame.font.init()

    if (font):
        self.font = pygame.font.Font(font, fontsize)
    else:
        self.font = pygame.font.Font(pygame.font.get_default_font(), fontsize)

    self.fontsize = fontsize
    self.getHudText = getHudTextFunc
    self.text = "Initializing..."

  def setState(self, simtime, getXY):
    self.text = self.getHudText(simtime)

  def drawToSurface(self, surf):
      x = 0
      for line in self.text:
          surf.blit(self.font.render(line, True, BLACK, HUD_BG),(0,x))
          x = int(x + self.fontsize)

  ## So long as we are passing LassoViz's in as part of the scene_viz
  ## list to a Simulation, we don't need to implement the getLabel,
  ## getBoundingBox, or mouseIntersect methods.
