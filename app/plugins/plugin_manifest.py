from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class PluginManifest:
    name: str
    version: str
    description: str
    author: Optional[str] = None

    # Entry point function
    entrypoint: Optional[Callable] = None

    # Permissions / capabilities
    allow_network: bool = False
    allow_filesystem: bool = False
    allow_llm_access: bool = False