# -*- coding: utf-8 -*-

# these items are treated differently:
SPECIAL_ITEM_NAMES = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]



class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # every item that is not a special item decreases in quality by 1 if quality > 0
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else: # if Age Brie or Backstage passes we increase quality by 1 if quality < 50
                # but if it is a "Backstage passe" we have more rules: 
                # if sell_in < 11 and quality < 50 increase quality by 1
                # if sell_in < 6 and quality < 50 increase quality by 1
                # this is meaningless, since all rules lead to the same result (which is adding 1 to quality)
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                # this means that if the item is not a "Sulfuras, Hand of Ragnaros" then we decrease sell_in by 1 every day (so it can go negative)
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                # if sell_in < 0 we decrease quality by 1 if it is not a special item
                # if item is eiter "Aged Brie" or "Backstage passes to a TAFKAL80ETC concert" we set quality to 0
                # if item is "Sulfuras, Hand of Ragnaros" we do nothing
                # but for "Aged Brie" we increase quality by 1 if quality < 50
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
