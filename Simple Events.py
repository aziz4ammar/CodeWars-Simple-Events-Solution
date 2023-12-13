class Event:

    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)

    def unsubscribe(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)

    def emit(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)