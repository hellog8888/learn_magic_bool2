import sys

class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for x in lst_in:
            self.inbox_list.append(MailItem(x.split('; ')[0], x.split('; ')[1], x.split('; ')[2]))


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        if fl_read:
            self.is_read = True
        else:
            self.is_read = False

    def __bool__(self):
        return self.is_read

mail = MailBox()
mail.receive()

mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(lambda x: x, mail.inbox_list))