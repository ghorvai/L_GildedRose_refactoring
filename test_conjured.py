# -*- coding: utf-8 -*-
import sys
import os
import unittest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gilded_rose import Item, GildedRose

CONJURED = "Conjured Mana Cake"

class GildedRoseTest(unittest.TestCase):

    def test_conjured_quality_decreases_twice_as_fast(self):
        items = [Item(CONJURED, 1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
