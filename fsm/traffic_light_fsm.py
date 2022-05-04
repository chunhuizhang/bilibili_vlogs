from transitions import Machine
from graphviz import Digraph
import enum
from datetime import datetime
import os
import time

class Matter(object):
    pass


def hunger_state():
    # The states
    states = ['hungry', 'satisfied', 'full', 'sick']

    # And some transitions between states.
    transitions = [{'trigger': 'eat', 'source': 'hungry', 'dest': 'satisfied'},
                   {'trigger': 'eat', 'source': 'satisfied', 'dest': 'full'},
                   {'trigger': 'eat', 'source': 'full', 'dest': 'sick'},
                   {'trigger': 'rest', 'source': ['satisfied', 'full', 'sick'],
                    'dest': 'hungry'}]

    # Initialize
    machine = Matter()
    fsm = Machine(machine, states=states, transitions=transitions, initial=states[0],
                  auto_transitions=False)
    return fsm

class States(enum.Enum):
    ERROR = 0
    RED = 1
    YELLOW = 2
    GREEN = 3

def traffic_light_fsm():


    transitions = [
                   ['timer_le_20', States.RED, States.RED],
                   ['timer_eq_20', States.RED, States.GREEN],
                   ['timer_le_15', States.GREEN, States.GREEN],
                   ['timer_eq_15', States.GREEN, States.YELLOW],
                   ['timer_le_5', States.YELLOW, States.YELLOW],
                   ['timer_eq_5', States.YELLOW, States.RED],
               ]

    fsm = Machine(states=States,
                  transitions=transitions,
                  initial=States.RED,
                  auto_transitions=False)
    return fsm


def vis(fsm, name):
    dot = Digraph(comment=name)

    for label, event in fsm.events.items():
        for event_transitions in event.transitions.values():
            for transition in event_transitions:
                dot.edge(transition.source, transition.dest, label)
    dot.render('{}.dot'.format(name))


if __name__ == '__main__':
    fsm = traffic_light_fsm()
    vis(fsm, 'traffic-light')
    start = datetime.now()

    while True:
        time.sleep(1)
        cur = datetime.now()
        duration = cur - start
        duration_secs = duration.seconds % 40
        if 0 < duration_secs < 20:
            if fsm.state == States.YELLOW:
                fsm.timer_eq_5()
            fsm.timer_le_20()
            print(cur, fsm.state)
        elif duration_secs == 20:
            fsm.timer_eq_20()
            print(cur, fsm.state)
        elif 20 < duration_secs < 35:
            fsm.timer_le_15()
            print(cur, fsm.state)
        elif duration_secs == 35:
            fsm.timer_eq_15()
            print(cur, fsm.state)
        elif duration_secs < 40:
            fsm.timer_le_5()
            print(cur, fsm.state)
        else:
            fsm.timer_eq_5()
            print(cur, fsm.state)
