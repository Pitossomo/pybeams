class Distributed_Load:
  
  def __init__(self, start_position, end_position, start_value, end_value):
    self.start_position = start_position
    self.end_position = end_position
    self.start_value = start_value
    self.end_value = end_value
  
  def __str__(self):
    return f"""Distributed Load
      start_position: {start_position}, end_position: {end_position}
      start_value: {start_value}, end_value: {end_value}"""  