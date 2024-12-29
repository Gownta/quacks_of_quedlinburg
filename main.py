#!/usr/bin/python3

from dataclasses import dataclass, field


@dataclass
class Token:
    num: int
    cost: int

    # Return True/False if Alive/Overboiled
    def place(self, pot):
        pass

    @classmethod
    def resolve(self, pot):
        pass


@dataclass
class Pot:
    tokens: [Token] = field(default_factory=list)
    max_whites: int = 7
    n_whites: int = 0


@dataclass
class Bag:
    tokens: [Token] = field(default_factory=list)


def main():
    pot = Pot()

main()
