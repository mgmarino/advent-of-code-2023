import re
from dataclasses import dataclass
from functools import partial
from operator import attrgetter
from typing import Iterator


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class PartNumber:
    value: int
    start: Coordinates
    stop: Coordinates


@dataclass
class Symbol:
    value: str
    coordinates: Coordinates


@dataclass
class DataSet:
    part_numbers: list[PartNumber]
    symbols: list[Symbol]

    @staticmethod
    def part_number_is_adjacent_to_symbol(p: PartNumber, s: Symbol) -> bool:
        y_range = p.start.y
        return (y_range - 1 <= s.coordinates.y <= y_range + 1) and (
            p.start.x - 1 <= s.coordinates.x <= p.stop.x + 1
        )

    @property
    def included_part_numbers(self) -> Iterator[PartNumber]:
        def _check_is_adjacent_to_any_symbols(p: PartNumber) -> bool:
            for s in self.symbols:
                if self.part_number_is_adjacent_to_symbol(p, s):
                    return True
            return False

        yield from filter(_check_is_adjacent_to_any_symbols, self.part_numbers)

    @property
    def sum_of_included_part_numbers(self) -> int:
        return sum(map(attrgetter("value"), self.included_part_numbers))

    @property
    def included_gear_ratios(self) -> list[tuple[PartNumber]]:
        def _check_part_numbers(s: Symbol) -> Iterator[PartNumber]:
            yield from filter(
                partial(self.part_number_is_adjacent_to_symbol, s=s), self.part_numbers
            )

        for s in filter(lambda x: x.value == "*", self.symbols):
            if len(val := tuple(_check_part_numbers(s))) == 2:
                yield val

    @property
    def sum_of_gear_ratios(self) -> int:
        return sum(map(lambda x: x[0].value * x[1].value, self.included_gear_ratios))


_numbers = re.compile(r"(\d+)")
_symbols = re.compile(r"([^0-9\.\n])")


def find_part_numbers_in_line(line: str, y: int) -> Iterator[PartNumber]:
    for match in _numbers.finditer(line):
        yield PartNumber(
            value=int(match.group(0)),
            start=Coordinates(x=match.start(0), y=y),
            stop=Coordinates(x=match.end(0) - 1, y=y),
        )


def find_part_numbers(all_lines: Iterator[str]) -> Iterator[PartNumber]:
    for idx, l in enumerate(all_lines):
        yield from find_part_numbers_in_line(l, idx)


def find_symbols_in_line(line: str, y: int) -> Iterator[Symbol]:
    for match in _symbols.finditer(line):
        yield Symbol(
            value=match.group(0), coordinates=Coordinates(x=match.start(0), y=y)
        )


def find_symbols(all_lines: Iterator[str]) -> Iterator[Coordinates]:
    for idx, l in enumerate(all_lines):
        yield from find_symbols_in_line(l, idx)


def parse_all_lines(all_lines: Iterator[str]) -> DataSet:
    data_set = DataSet(
        part_numbers=list(find_part_numbers(all_lines)),
        symbols=list(find_symbols(all_lines)),
    )
    return data_set


def part_one(all_lines: Iterator[str]) -> int:
    return parse_all_lines(all_lines).sum_of_included_part_numbers


def part_two(all_lines: Iterator[str]) -> int:
    return parse_all_lines(all_lines).sum_of_gear_ratios
