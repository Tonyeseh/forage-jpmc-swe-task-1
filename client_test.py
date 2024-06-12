import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       stock, bid_price, ask_price, price = getDataPoint(quote)
       self.assertAlmostEqual(bid_price, quote['top_bid']['price'])
       self.assertAlmostEqual(ask_price, quote['top_ask']['price'])
       self.assertEqual(stock, quote['stock'])
       self.assertAlmostEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       stock, bid_price, ask_price, price = getDataPoint(quote)
       self.assertAlmostEqual(bid_price, quote['top_bid']['price'])
       self.assertAlmostEqual(ask_price, quote['top_ask']['price'])
       self.assertEqual(stock, quote['stock'])
       self.assertAlmostEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
     prices = [{'ABC': 117.38, 'DEF': 116.505, 'ratio': 1.0075104072786576}, {'ABC': 117.38, 'DEF': 116.325, 'ratio': 1.0090694175800559}]
     for price in prices:
        self.assertAlmostEqual(getRatio(price['ABC'], price['DEF']), price['ratio'])

  def test_getRatio_calculateRatioPrice_bEqualZero(self):
     prices = [{'ABC': 117.38, 'DEF': 0,}, {'ABC': 117.38, 'DEF': 0,}]
     for price in prices:
        self.assertAlmostEqual(getRatio(price['ABC'], price['DEF']), None)


if __name__ == '__main__':
    unittest.main()
