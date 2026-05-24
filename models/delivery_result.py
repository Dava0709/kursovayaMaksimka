from dataclasses import dataclass
from typing import List


@dataclass
class DeliveryResult:
    adapter_name: str
    messages: List[str]
