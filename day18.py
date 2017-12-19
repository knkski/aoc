from collections import defaultdict
from multiprocessing import Queue, pool as mp_pool
from queue import Empty

with open('day18.txt') as f:
    lines = [l.strip() for l in f.readlines()]


def program(name, into_queue=None, outof_queue=None):
    registers = defaultdict(int)

    registers['p'] = name

    current = 0
    total_sent = 0
    last_played = None

    while True:
        line = lines[current]

        try:
            instruction, register, value = line.split(' ')
        except ValueError:
            instruction, register = line.split(' ')
            value = None

        def lookup(val):
            try:
                return int(val)
            except ValueError:
                return registers[val]

        if value is not None:
            value = lookup(value)

        if instruction == 'set':
            registers[register] = value

        elif instruction == 'add':
            registers[register] += value

        elif instruction == 'mul':
            registers[register] *= value

        elif instruction == 'mod':
            registers[register] %= value

        elif instruction == 'snd':
            total_sent += 1

            if into_queue:
                into_queue.put(lookup(register))
            else:
                last_played = lookup(register)

        elif instruction == 'rcv':
            if outof_queue:
                try:
                    registers[register] = outof_queue.get(timeout=1)
                except Empty:
                    return total_sent
            elif lookup(register) != 0:
                return last_played

        elif instruction == 'jgz':
            if lookup(register) > 0:
                current += value
                continue

        else:
            raise Exception('Unknown instruction!')

        current += 1


print(program(0))

pool = mp_pool.ThreadPool(processes=2)

queue0 = Queue()
queue1 = Queue()

prog0 = pool.apply_async(program, args=(0, queue0, queue1))
prog1 = pool.apply_async(program, args=(1, queue1, queue0))

prog0.get()
print(prog1.get())
