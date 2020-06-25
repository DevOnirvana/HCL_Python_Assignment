#This is the class that implements the Singleton design pattern
#We use a decorator of this class to decorate other classes that implement this pattern
class Singleton:

  def __init__(self, klass):
    self.klass = klass
    self.instance = None

  def __call__(self, *args, **kwds):
    if self.instance is None:
      self.instance = self.klass(*args, **kwds)
    return self.instance