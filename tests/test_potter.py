import pytest
from libs.potter import Potter

potter = Potter()
def testBasics():
  assert 0 == potter.get_price([])
  assert 8 == potter.get_price([1])
  assert 8 == potter.get_price([2])
  assert 8 == potter.get_price([3])
  assert 8 == potter.get_price([4])
  assert 8 * 3 == potter.get_price([1, 1, 1])
  
