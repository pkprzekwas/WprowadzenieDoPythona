
class Todo:
    def __init__(self, content):
        self.content = content
        self.is_finished = False

    def __str__(self):
        return 'zadanie: {}'.format(self.content)
