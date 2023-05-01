"""
For this exercise you will be strengthening your page-fu mastery. You will complete the
PaginationHelper class, which is a utility class helpful for querying paging information
related to an array.
The class is designed to take in an array of values and an integer indicating how many
items will be allowed per each page.
The types of values contained within the collection/array are not relevant.
The following are some examples of how this class is used:
"""


# TODO: complete this class


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages_index = 0
        # self.list_of_items_per_page = []
        # self.amaunt_of_pages_with_items = 0

    # returns the number of items within the entire collection
    def item_count(self):
        len_l = len(self.collection)
        return len_l

    # returns the number of pages
    def page_count(self):
        # x = self.amaunt_of_pages_with_items
        x = self.item_count() // self.items_per_page + (self.item_count() % self.items_per_page > 0)
        return x

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, pages_index):
        len_l = self.item_count()
        list_of_items_per_page = []
        amaunt_of_pages_with_items = 0
        while len_l >= self.items_per_page:
            len_l -= self.items_per_page
            list_of_items_per_page.append(self.items_per_page)
            amaunt_of_pages_with_items += 1
        list_of_items_per_page.append(len_l % self.items_per_page)
        # print(self.list_of_items_per_page)

        if list_of_items_per_page[-1] == 0:
            pass
        try:
            return list_of_items_per_page[pages_index]
        except:
            return -1

        # походу має брати індекс позиції айтемсів у списку, який має формуватись вище. сам список
        # хоча можна спробувати сформувати список тут.
        # на першій a single page буде items per page айтемів (4),
        # але на helper.page_item_count(1) == 2

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if type(self.collection) == range:
            l = list(self.collection)
            l = l.copy()
        else:
            l = self.collection.copy()
        if item_index >= len(l) or item_index < 0:
            return -1
        else:
            itemsPerP = self.items_per_page
            list_of_keys = []
            cnt = 0
            while cnt < itemsPerP:
                list_of_keys.append((l[0:itemsPerP]))
                del l[0:itemsPerP]
                cnt += 1
            l = self.collection
            # print(l[item_index])
            for el in list_of_keys:
                if l[item_index] in el:
                    return list_of_keys.index(el)
                elif l[item_index] not in el:
                    pass

            # 5 айтем має бути на сторінці другій (по індексу це 1)
        # а 2 айтем буде на 0


# список має виглядати так [4,2] бо елементів є 6.
# якби було 25, то було б [4,4,4,4,4,4,1]
# десь потрібно забирати 4 в циклі і ставити її в список

collection = range(1, 25)
helper = PaginationHelper(collection, 4)

# helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
# print(helper.page_count())  # should == 2
# print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# print(helper.page_index(5))  # should == 1 (zero based index)
# print(helper.page_index(2))  # should == 0
# print(helper.page_index(20))  # should == -1
# print(helper.page_index(-10))  # should == -1 because negative indexes are invalid
# , 'g', 'i', 't', 'h', 'k', 'l', 'm'

"""
SAMPLE TESTS

collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')
"""


def func(list_of_items, amount_of_items_per_page):
    amperpage = amount_of_items_per_page
    list_of_items_per_page = []
    x = 0
    len_l = len(list_of_items)
    while len_l >= amperpage:
        len_l -= amperpage
        list_of_items_per_page.append(amperpage)
        x += 1

    list_of_items_per_page.append(len_l % amperpage)
    if list_of_items_per_page[-1] != 0:
        x += 1
    elif list_of_items_per_page[-1] == 0:
        the_last_page_has_items = list_of_items_per_page[-1]
        print(the_last_page_has_items)
    else:
        print(-1)
    print('amaunt of pages with items x=', x)
    print('list_of_items_per_page=', list_of_items_per_page)


# func(['a', 'b', 'c', 'd', 'e', 'f', 'i', 'g',"h",'t'], 3)

# print(22 // 4)
# print(22 % 4)

original_list = [[1, 2], [3, 4]]
new_list = original_list.copy()

print(id(original_list[0]))  # prints a unique identifier for the first element in original_list
print(id(new_list[0]))


# TODO: complete this class

class PaginationHelper1:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) / self.items_per_page
        else:
            return len(self.collection) / self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return item_index / self.items_per_page


class PaginationHelper2:

    def __init__(self, collection, items_per_page):
        """
        The constructor takes in an list of items and a integer indicating how many items fit within a single page
        """
        self._items_per_page = items_per_page
        self._pages = tuple(len(collection[i:i + items_per_page]) for i in range(0, len(collection), items_per_page))

    def item_count(self):
        """Returns the number of items within the entire collection"""
        return sum(self._pages)

    def page_count(self):
        """Returns the number of pages"""
        return len(self._pages)

    def page_item_count(self, page_index):
        """
        Returns the number of items on the current page. page_index is zero based
        This method should return -1 for page_index values that are out of range
        """
        try:
            return self._pages[page_index]
        except IndexError:
            return -1

    def page_index(self, item_index):
        """
        Determines what page an item is on. Zero based indexes.
        This method should return -1 for item_index values that are out of range
        """
        return item_index // self._items_per_page if 0 <= item_index < self.item_count() else -1


class PaginationHelper3:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1


class PaginationHelper4:

    def __init__(self, collection: list, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return __import__('math').ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        if self.item_count() % self.items_per_page and page_index == self.page_count() - 1:
            return self.item_count() - self.items_per_page * (self.page_count() - 1)
        return self.items_per_page if page_index in range(self.page_count()) else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page if item_index in range(self.item_count()) else -1


from math import ceil


# TODO: complete this class
class PaginationHelper5:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.len_col = len(self.collection)  # 6
        self.var = self.len_col / self.items_per_page  # print(6/4) = 1.5

    def item_count(self):
        return self.len_col

    def page_count(self):
        return ceil(self.var)  # ceil() округлить до більшого ближнього числа

    def page_item_count(self, page_index):  # кількість елементів на поточній сторінці
        if int(self.var) == page_index: return self.len_col % self.items_per_page  # якщо кількість сторінок така сама
        # як індекс, то поверне остачу від (ділення довижини списку на кількість айтемс за сторінку) print(6%4)== 2
        return self.items_per_page if int(self.var) > page_index else -1  # якщо кількічть сторінок з айтемсами більша
        # за індекс сторінки, то поверне кількість айтемсів за сторінку, інакше -1

    def page_index(self, item_index):  # визначає, на якій сторінці знаходиться елемент під індексом.
        # Індекси від нуля.
        return int(item_index / self.items_per_page) if item_index in range(self.len_col) else -1
# вивести результат округлення до меншого((індекс айтема) поділити на (кількість айтемів за сторінку))
# якщо індекс айтему в діапазоні довжини колекції, інакше -1
        # int(5/4)
print(int(6 / 4))
print(6 % 4)


class PaginationHelper6:
    def __init__(self, collection, items_per_page):
        self.items = collection
        self.items_per_page = items_per_page
        self.items_count = len(collection)
        self.pages_count = (len(collection) // items_per_page) + bool(len(collection) % items_per_page)

    def item_count(self):
        return self.items_count

    def page_count(self):
        return self.pages_count

    def page_item_count(self, page_index):
        if page_index == self.pages_count - 1:
            return self.items_count % self.items_per_page
        elif 0 <= page_index < self.pages_count - 1:
            return self.items_per_page
        else:
            return -1

    def page_index(self, item_index):
        return item_index // self.items_per_page if 0 <= item_index < self.items_count else -1
