# -*- coding: utf-8 -*-
import sys
import os
import unittest

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gilded_rose import Item, GildedRose

AGED_BRIE = "Aged Brie"

class GildedRoseTest(unittest.TestCase):

    def test_item_quality_is_never_more_than_50(self):
        # unsing Aged Brie as an example since it increases in quality
        # by the way, sulfuras has a quality of 80, but that is irrelevant for this test
        items = [Item(AGED_BRIE, 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


    def test_aged_brie_increases_in_quality(self):
        items = [Item(AGED_BRIE, 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_increases_in_quality_twice_as_fast(self):
        items = [Item(AGED_BRIE, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
