
# pma.py --maxTransitions 100 synchronous socket
# 84 states, 100 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def send_return(): pass
def send_call(): pass
def recv_call(): pass
def recv_return(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': ''}},
  1 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': ''}},
  2 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': ''}},
  3 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'a'}},
  4 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bb'}},
  5 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'b'}},
  6 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'a'}},
  7 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bb'}},
  8 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'b'}},
  9 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'b'}},
  10 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'b'}},
  11 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'b'}},
  12 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'ba'}},
  13 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbb'}},
  14 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'ba'}},
  15 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbb'}},
  16 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'a'}},
  17 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bb'}},
  18 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'a'}},
  19 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'a'}},
  20 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'bb'}},
  21 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'bb'}},
  22 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aa'}},
  23 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'abb'}},
  24 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'ab'}},
  25 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bba'}},
  26 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbbb'}},
  27 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'aa'}},
  28 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'abb'}},
  29 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'ab'}},
  30 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bba'}},
  31 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbbb'}},
  32 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'ba'}},
  33 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbb'}},
  34 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'ba'}},
  35 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'ba'}},
  36 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'bbb'}},
  37 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'bbb'}},
  38 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'baa'}},
  39 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'babb'}},
  40 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bab'}},
  41 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbba'}},
  42 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbbbb'}},
  43 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'baa'}},
  44 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'babb'}},
  45 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bab'}},
  46 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbba'}},
  47 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbbbb'}},
  48 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aa'}},
  49 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'abb'}},
  50 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'ab'}},
  51 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bba'}},
  52 : {'synchronous': 0, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbbb'}},
  53 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'aa'}},
  54 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'aa'}},
  55 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'abb'}},
  56 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'abb'}},
  57 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'ab'}},
  58 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'ab'}},
  59 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'bba'}},
  60 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'bba'}},
  61 : {'synchronous': 1, 'socket': {'send_arg': 'a', 'recv_arg': 0, 'buffers': 'bbbb'}},
  62 : {'synchronous': 1, 'socket': {'send_arg': 'bb', 'recv_arg': 0, 'buffers': 'bbbb'}},
  63 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aaa'}},
  64 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aabb'}},
  65 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aab'}},
  66 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'abba'}},
  67 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'abbbb'}},
  68 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'abbb'}},
  69 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'aba'}},
  70 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbaa'}},
  71 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbabb'}},
  72 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbab'}},
  73 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbbba'}},
  74 : {'synchronous': 2, 'socket': {'send_arg': '', 'recv_arg': 0, 'buffers': 'bbbbbb'}},
  75 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'aaa'}},
  76 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'aabb'}},
  77 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'aab'}},
  78 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'abba'}},
  79 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'abbbb'}},
  80 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'abbb'}},
  81 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'aba'}},
  82 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbaa'}},
  83 : {'synchronous': 3, 'socket': {'send_arg': '', 'recv_arg': 4, 'buffers': 'bbabb'}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [0]
unsafe = []
frontier = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (send_call, ('a',), None), 1),
  (0, (send_call, ('bb',), None), 2),
  (1, (send_return, (1,), None), 3),
  (2, (send_return, (2,), None), 4),
  (2, (send_return, (1,), None), 5),
  (3, (recv_call, (4,), None), 6),
  (4, (recv_call, (4,), None), 7),
  (5, (recv_call, (4,), None), 8),
  (6, (recv_return, ('a',), None), 0),
  (7, (recv_return, ('bb',), None), 0),
  (7, (recv_return, ('b',), None), 9),
  (8, (recv_return, ('b',), None), 0),
  (9, (send_call, ('a',), None), 10),
  (9, (send_call, ('bb',), None), 11),
  (10, (send_return, (1,), None), 12),
  (11, (send_return, (2,), None), 13),
  (11, (send_return, (1,), None), 4),
  (12, (recv_call, (4,), None), 14),
  (13, (recv_call, (4,), None), 15),
  (14, (recv_return, ('b',), None), 16),
  (15, (recv_return, ('bb',), None), 9),
  (15, (recv_return, ('b',), None), 17),
  (16, (send_call, ('a',), None), 18),
  (16, (send_call, ('bb',), None), 19),
  (17, (send_call, ('a',), None), 20),
  (17, (send_call, ('bb',), None), 21),
  (18, (send_return, (1,), None), 22),
  (19, (send_return, (2,), None), 23),
  (19, (send_return, (1,), None), 24),
  (20, (send_return, (1,), None), 25),
  (21, (send_return, (2,), None), 26),
  (21, (send_return, (1,), None), 13),
  (22, (recv_call, (4,), None), 27),
  (23, (recv_call, (4,), None), 28),
  (24, (recv_call, (4,), None), 29),
  (25, (recv_call, (4,), None), 30),
  (26, (recv_call, (4,), None), 31),
  (27, (recv_return, ('a',), None), 16),
  (28, (recv_return, ('a',), None), 17),
  (29, (recv_return, ('a',), None), 9),
  (30, (recv_return, ('bb',), None), 16),
  (30, (recv_return, ('b',), None), 32),
  (31, (recv_return, ('bb',), None), 17),
  (31, (recv_return, ('b',), None), 33),
  (32, (send_call, ('a',), None), 34),
  (32, (send_call, ('bb',), None), 35),
  (33, (send_call, ('a',), None), 36),
  (33, (send_call, ('bb',), None), 37),
  (34, (send_return, (1,), None), 38),
  (35, (send_return, (2,), None), 39),
  (35, (send_return, (1,), None), 40),
  (36, (send_return, (1,), None), 41),
  (37, (send_return, (2,), None), 42),
  (37, (send_return, (1,), None), 26),
  (38, (recv_call, (4,), None), 43),
  (39, (recv_call, (4,), None), 44),
  (40, (recv_call, (4,), None), 45),
  (41, (recv_call, (4,), None), 46),
  (42, (recv_call, (4,), None), 47),
  (43, (recv_return, ('b',), None), 48),
  (44, (recv_return, ('b',), None), 49),
  (45, (recv_return, ('b',), None), 50),
  (46, (recv_return, ('bb',), None), 32),
  (46, (recv_return, ('b',), None), 51),
  (47, (recv_return, ('bb',), None), 33),
  (47, (recv_return, ('b',), None), 52),
  (48, (send_call, ('a',), None), 53),
  (48, (send_call, ('bb',), None), 54),
  (49, (send_call, ('a',), None), 55),
  (49, (send_call, ('bb',), None), 56),
  (50, (send_call, ('a',), None), 57),
  (50, (send_call, ('bb',), None), 58),
  (51, (send_call, ('a',), None), 59),
  (51, (send_call, ('bb',), None), 60),
  (52, (send_call, ('a',), None), 61),
  (52, (send_call, ('bb',), None), 62),
  (53, (send_return, (1,), None), 63),
  (54, (send_return, (2,), None), 64),
  (54, (send_return, (1,), None), 65),
  (55, (send_return, (1,), None), 66),
  (56, (send_return, (2,), None), 67),
  (56, (send_return, (1,), None), 68),
  (57, (send_return, (1,), None), 69),
  (58, (send_return, (2,), None), 68),
  (58, (send_return, (1,), None), 23),
  (59, (send_return, (1,), None), 70),
  (60, (send_return, (2,), None), 71),
  (60, (send_return, (1,), None), 72),
  (61, (send_return, (1,), None), 73),
  (62, (send_return, (2,), None), 74),
  (62, (send_return, (1,), None), 42),
  (63, (recv_call, (4,), None), 75),
  (64, (recv_call, (4,), None), 76),
  (65, (recv_call, (4,), None), 77),
  (66, (recv_call, (4,), None), 78),
  (67, (recv_call, (4,), None), 79),
  (68, (recv_call, (4,), None), 80),
  (69, (recv_call, (4,), None), 81),
  (70, (recv_call, (4,), None), 82),
  (71, (recv_call, (4,), None), 83),
)
