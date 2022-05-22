class Unit:

    def __init__(self, content=None):
        self.content = content
        self.next_content = None


class LinkedList:

    def __init__(self):
        self.begin = None

    def append(self, new_content):
        new_unit = Unit(new_content)
        if self.begin is None:
            self.begin = new_unit
            return
        last_unit = self.begin
        while last_unit.next_content:
            last_unit = last_unit.next_content
        last_unit.next_content = new_unit

    def get(self, content_index):
        last_unit = self.begin
        unit_index = 0
        while unit_index <= content_index:
            if unit_index == content_index:
                return last_unit.content
            unit_index = unit_index + 1
            last_unit = last_unit.next_content

    def remove(self, del_index):
        begin_content = self.begin
        if begin_content is not None:
            if del_index == 0:
                self.begin = begin_content.next_content
                begin_content = None
                return
        while begin_content is not None:
            if del_index == 0:
                break
            previous_content = begin_content
            begin_content = begin_content.next_content
            del_index -= 1
        if begin_content == None:
            return
        previous_content.next_content = begin_content.next_content
        begin_content = None

    def show(self):
        elem = self.begin
        print('[', end=' ')
        while elem is not None:
            print(elem.content, end=' ')
            elem = elem.next_content
        print(']')
