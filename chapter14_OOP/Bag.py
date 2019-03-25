class Bag:
    def __init__(self, color='black',
                 size=3, content={}):
        self.color = color
        self.size = size
        self.content = content

    def __str__(self):
        return 'color: {}\tsize: {}\tcontent:{}'.format(
            self.color, self.size, self.content
        )

    def is_empty(self):
        if len(self.content.items()) == 0:
            return True
        else:
            return False

    def empty(self):
        self.content.clear()


bag1 = Bag()
bag2 = Bag(content={'pen': 1,  'laptop': 1, 'candy':3})
bag3 = Bag(color='red', size=7)
print('bag1', bag1)
print('bag2', bag2)
print('bag3', bag3)

print('bag1 is empty?', bag1.is_empty())
print('bag2 is empty?', bag2.is_empty())
print('bag3 is empty?', bag3.is_empty())

bag2.empty()
print('bag2 is empty?', bag2.is_empty())