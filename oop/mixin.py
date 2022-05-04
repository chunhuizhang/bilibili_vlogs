
class State:
    def __init__(self):
        print('State init')
        self.first_state = 'main state'


class Event:
    def __init__(self):
        print('Event init')
        self.event_name = 'main event'


class HappyState(State, Event):
    def __init__(self):
        super().__init__()
        super(State, self).__init__()
        print('HappyState init')
        self.second_state = 'happy state'


if __name__ == '__main__':
    hs = HappyState()


