donors: address[100]
donorIndex: num
entered: bool[address]
pot: wei_value
start_time: timestamp
length: timedelta
end_time: timestamp

def index(_length: timedelta):
  self.start_time = block.timestamp
  self.donorIndex = 0
  self.length = _length
  self.end_time = self.start_time + self.length
  
@payable
def enter():
  assert block.timestamp < self.end_time
  self.entered[msg.sender] = True
  self.pot += msg.value
  self.donors[donorIndex] = msg.sender

def get_end():
  return self.end_time
 
def donate():
  
