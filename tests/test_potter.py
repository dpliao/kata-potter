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

def testSimpleDiscounts():
  assert 8 * 2 * 0.95 == potter.get_price([0, 1])
  assert 8 * 3 * 0.9 == potter.get_price([0, 2, 4])
  assert 8 * 4 * 0.8 == potter.get_price([0, 1, 2, 4])
  assert 8 * 5 * 0.75 == potter.get_price([0, 1, 2, 3, 4])
