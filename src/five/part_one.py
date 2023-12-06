from collections import defaultdict
from dataclasses import dataclass, field, fields
from typing import Optional


@dataclass
class SrcDestMapping:
    src_start: int
    dest_start: int
    span: int

    def __contains__(self, src: int) -> bool:
        return self.src_start <= src < self.src_start + self.span

    def __getitem__(self, __key: int) -> int:
        return (__key - self.src_start) + self.dest_start


@dataclass
class DefaultMap:
    mappings: list[SrcDestMapping] = field(default_factory=list)

    def add_mapping(self, src_dest_mapping: SrcDestMapping):
        self.mappings.append(src_dest_mapping)

    def __getitem__(self, __key: int) -> int:
        for m in self.mappings:
            if __key in m:
                return m[__key]
        return __key


@dataclass
class Almanac:
    seeds: set[int]
    seed_to_soil: DefaultMap
    soil_to_fertilizer: DefaultMap
    fertilizer_to_water: DefaultMap
    water_to_light: DefaultMap
    light_to_temperature: DefaultMap
    temperature_to_humidity: DefaultMap
    humidity_to_location: DefaultMap

    def find_next_map_name(self, prev_map: str) -> Optional[str]:
        next_map_root = prev_map.split("_to_")[-1]
        for f in fields(self):
            if f.name.startswith(next_map_root):
                return f.name
        return None

    def _location_of_seed(self, seed: int) -> int:
        current_field = "seed_to_soil"
        current_idx = seed
        while current_field is not None:
            current_idx = getattr(self, current_field)[current_idx]
            current_field = self.find_next_map_name(current_field)
        return current_idx

    @property
    def locations_of_seed(self) -> dict[int, int]:
        return {s: self._location_of_seed(s) for s in self.seeds}


def parse_lines(all_lines: list[str]) -> Almanac:
    all_lines = iter(all_lines)
    seed_set = set(map(int, next(all_lines).split(": ")[-1].split(" ")))

    current_map = None
    all_maps = defaultdict(DefaultMap)
    for li in all_lines:
        if li.strip() == "":
            continue
        if ":" in li:
            current_map = li.split(" ")[0]
        else:
            dest, src, ran = tuple(map(int, li.split(" ")))
            all_maps[current_map].add_mapping(
                SrcDestMapping(src_start=src, dest_start=dest, span=ran)
            )

    return Almanac(
        seeds=seed_set, **{k.replace("-", "_"): v for k, v in all_maps.items()}
    )


def part_one(all_lines: list[str]) -> int:
    almanac = parse_lines(all_lines)
    return min(almanac.locations_of_seed.values())
