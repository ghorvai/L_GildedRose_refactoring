# -*- coding: utf-8 -*-
import sys
import os
import unittest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gilded_rose import Item, GildedRose

BACLSTAGE = "Backstage passes to a TAFKAL80ETC concert"

class GildedRoseTest(unittest.TestCase):
    def test_backstage_passes_quality_increases_by_1(self):
        items = [Item(BACLSTAGE, 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_increases_by_2(self):
        items = [Item(BACLSTAGE, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_quality_increases_by_3(self):
        items = [Item(BACLSTAGE, 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_quality_drops_to_0(self):
        items = [Item(BACLSTAGE, 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        



        
if __name__ == '__main__':
    unittest.main()
