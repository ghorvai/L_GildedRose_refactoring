def general_case_update(item):
    """
    General case for updating items:
        - Decrease sell_in by 1
        - Decrease quality by 1 but not below 0
        - If sell_in < 0, quality becomes 0
    """
    item.sell_in -= 1
    if item.sell_in < 0:
        item.quality = 0
    elif item.quality > 0:
        item.quality -= 1

def aged_brie_update(item):
    """
    Aged Brie increases in quality by:
        - 1 every day, but not above 50.
        - 2 every day after sell_in < 0, but not above 50.
    """
    item.sell_in -= 1
    if item.quality < 50:
        item.quality += 1
    if item.sell_in < 0 and item.quality < 50:
        item.quality += 1 #this is the second increase in quality

def sulfuras_update(item):
    """Sulfuras never changes in quality or sell_in."""
    pass

def backstage_passes_update(item):
    """
    Backstage passes increase in quality until sell_in < 0 or quality == 50:
        - 1 every day, if sell_in >= 10.
        - 2 when 10 > sell_in >= 5.
        - 3 when 5 > sell_in >= 0.
    However, quality becomes 0 after sell_in < 0.
    """
    item.sell_in -= 1
    if item.sell_in < 0:
        item.quality = 0
    elif item.quality < 50:
        item.quality += 1
        if item.sell_in < 10:
            item.quality += 1
        if item.sell_in < 5:
            item.quality += 1

def conjured_update(item):
    """Conjured items degrade in quality twice as fast as normal items."""
    item.sell_in -= 1
    item.quality = max(item.quality - 2, 0)
            
UPDATE_FUNCTIONS = {
    "Aged Brie": aged_brie_update,
    "Sulfuras, Hand of Ragnaros": sulfuras_update,
    "Backstage passes to a TAFKAL80ETC concert": backstage_passes_update,
    "Conjured Mana Cake": conjured_update
}

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = UPDATE_FUNCTIONS.get(item.name, general_case_update)
            updater(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
