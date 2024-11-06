# -*- coding: utf-8 -*-
import sys
import os
import unittest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    
    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
