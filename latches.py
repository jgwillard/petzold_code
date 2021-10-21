from base import Level, LogicComponent
from gates import And, Nor, Not, Split


class FlipFlop(LogicComponent):
    """
    An RS flip-flop
    """

    def __init__(self, name):
        super().__init__(name)
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.r = self.nor_a.input_a
        self.s = self.nor_b.input_b
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = Level.HI


class OneBitLatch(LogicComponent):
    """
    A level-triggered D-type flip-flop
    """

    def __init__(self, name):
        super().__init__(name)
        self.splitter_clock = Split(f"{name}#splitter_clock")
        self.splitter_data = Split(f"{name}#splitter_data")
        self.and_a = And(f"{name}#and_a")
        self.and_b = And(f"{name}#and_b")
        self.inverter = Not(f"{name}#inverter")
        self.nor_a = Nor(f"{name}#nor_a")
        self.nor_b = Nor(f"{name}#nor_b")
        self.clock = self.splitter_clock.input
        self.data = self.splitter_data.input
        self.splitter_clock.output_a.connections.append(self.and_a.input_b)
        self.splitter_clock.output_b.connections.append(self.and_b.input_a)
        self.splitter_data.output_a.connections.append(self.inverter.input)
        self.inverter.output.connections.append(self.and_a.input_a)
        self.splitter_data.output_b.connections.append(self.and_b.input_b)
        self.and_a.output.connections.append(self.nor_a.input_a)
        self.and_b.output.connections.append(self.nor_b.input_b)
        self.nor_a.output.connections.append(self.nor_b.input_a)
        self.nor_b.output.connections.append(self.nor_a.input_b)
        self.q = self.nor_a.output
        self.q_bar = self.nor_b.output
        self.q_bar.val = Level.HI


class EightBitLatch(LogicComponent):
    """
    A latch capable of storing a single 8-bit value
    """

    def __init__(self, name):
        super().__init__(name)
        self.latch_0 = OneBitLatch("{name}#latch_0")
        self.latch_1 = OneBitLatch("{name}#latch_1")
        self.latch_2 = OneBitLatch("{name}#latch_2")
        self.latch_3 = OneBitLatch("{name}#latch_3")
        self.latch_4 = OneBitLatch("{name}#latch_4")
        self.latch_5 = OneBitLatch("{name}#latch_5")
        self.latch_6 = OneBitLatch("{name}#latch_6")
        self.latch_7 = OneBitLatch("{name}#latch_7")
        self.d_0 = self.latch_0.data
        self.d_1 = self.latch_1.data
        self.d_2 = self.latch_2.data
        self.d_3 = self.latch_3.data
        self.d_4 = self.latch_4.data
        self.d_5 = self.latch_5.data
        self.d_6 = self.latch_6.data
        self.d_7 = self.latch_7.data
        self.q_0 = self.latch_0.q
        self.q_1 = self.latch_1.q
        self.q_2 = self.latch_2.q
        self.q_3 = self.latch_3.q
        self.q_4 = self.latch_4.q
        self.q_5 = self.latch_5.q
        self.q_6 = self.latch_6.q
        self.q_7 = self.latch_7.q
        self.clock = Split("{name}#clock")
        self.clock.output_a.connections.append(self.latch_0.clock)
        self.clock.output_a.connections.append(self.latch_1.clock)
        self.clock.output_a.connections.append(self.latch_2.clock)
        self.clock.output_a.connections.append(self.latch_3.clock)
        self.clock.output_a.connections.append(self.latch_4.clock)
        self.clock.output_a.connections.append(self.latch_5.clock)
        self.clock.output_a.connections.append(self.latch_6.clock)
        self.clock.output_a.connections.append(self.latch_7.clock)
