from dataclasses import dataclass, asdict


@dataclass
class User:
    id: str
    name: str

    @classmethod
    def load(cls, data):
        return cls(**data)

    def dump(self):
        return asdict(self)
