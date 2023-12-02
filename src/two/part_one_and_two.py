from dataclasses import asdict, dataclass, fields
from functools import cached_property, reduce
from operator import attrgetter, mul
from typing import Iterator


@dataclass
class Cubes:
    red: int = 0
    blue: int = 0
    green: int = 0

    def __le__(self, other: "Cubes") -> bool:
        return all(
            [s <= o for s, o in zip(asdict(self).values(), asdict(other).values())]
        )


@dataclass
class Game:
    id: int
    cube_sets: list[Cubes]

    @cached_property
    def max_cubes(self) -> Cubes:
        return Cubes(
            **{
                f.name: max(map(attrgetter(f.name), self.cube_sets))
                for f in fields(Cubes)
            }
        )

    @cached_property
    def power(self):
        return reduce(mul, asdict(self.max_cubes).values(), 1)


def parse_line(line: str) -> Game:
    id_data, sets = line.split(": ")
    game_id = int(id_data.split(" ")[1])

    def _parse_set(parsed_set: list[str]) -> list[tuple[str]]:
        return [c.split(" ") for c in parsed_set]

    def _cubes(parsed_cubes: list[tuple[str]]) -> Cubes:
        return Cubes(
            **{
                color.strip(): int(val)
                for val, color in _parse_set(parsed_cubes.split(", "))
            }
        )

    return Game(
        id=game_id,
        cube_sets=[_cubes(one_set) for one_set in sets.split("; ")],
    )


def parse_all_lines(all_lines: Iterator[str]) -> Iterator[Game]:
    return map(parse_line, all_lines)


def get_sum_of_ids_of_accepted_games(games: Iterator[Game], max_cubes: Cubes) -> int:
    return sum([v.id for v in games if v.max_cubes <= max_cubes])


def get_sum_of_power_of_games(games: Iterator[Game]) -> int:
    return sum([v.power for v in games])


def part_one(all_lines: Iterator[str], max_cubes: Cubes) -> int:
    return get_sum_of_ids_of_accepted_games(parse_all_lines(all_lines), max_cubes)


def part_two(all_lines: Iterator[str]) -> int:
    return get_sum_of_power_of_games(parse_all_lines(all_lines))
