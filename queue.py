class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def is_empty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)

  def __repr__(self):
    return f"[{', '.join([item for item in self.items])}]"