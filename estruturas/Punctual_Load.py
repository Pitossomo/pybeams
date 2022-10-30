class Punctual_Load:
  
  def __init__(self, position, value):
    self.position = position
    self.value = value
  
  def __str__(self):
    return f'Punctual Load - position: {self.position}, value: {self.value}'