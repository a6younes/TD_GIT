import abc

class Team(abc.ABC):
  def init(self, members):
    self._members = members

  def len(self):
    return len(self._members)

  def getitem(self, index):
    return self._members[index]
