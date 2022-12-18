from typing import Optional, Type, Any, List

class Inventory:
    def __init__(path: Optional[str]) -> self: ...
    def add_dir(self, path: str, filter: Optional[str]): ...
    def connector(self, name: str, args: Optional[str]) -> Connector: ...
    def os(self, name: str, connector: Optional[Os], args: Optional[str]) -> Os: ...
    def available_os(self) -> List[str]: ...
    def available_connectors(self) -> List[str]: ...

class Connector:
    @property
    def max_address(self) -> int: ...
    @property
    def real_size(self) -> int: ...
    @property
    def readonly(self) -> bool: ...
    @property
    def ideal_batch_size(self) -> int: ...
    def phys_read(self, addr: int, type: Type[_CT]) -> Any: ...
    def phys_read_ptr(self, ptr: Any) -> Any: ...
    def phys_write(self, addr: int, type: Type[_CT], value: Any): ...

class Os:
    @property
    def arch(self) -> str: ...
    @property
    def base(self) -> int: ...
    @property
    def size(self) -> int: ...
    def process_info_list(self) -> List[ProcessInfo]: ...
    def process_from_name(self, name: str) -> Process: ...
    def process_from_pid(self, pid: int) -> Process: ...
    def process_from_info(self, info: ProcessInfo) -> Process: ...
    def process_from_addr(self, addr: int) -> Process: ...
    def module_info_list(self) -> List[ModuleInfo]: ...
    def module_from_name(self, name: str) -> ModuleInfo: ...
    def read(self, addr: int, type: Type[_CT]) -> Any: ...
    def read_ptr(self, ptr: Any) -> Any: ...
    def write(self, addr: int, type: Type[_CT], value: Any): ...
    def phys_read(self, addr: int, type: Type[_CT]) -> Any: ...
    def phys_read_ptr(self, ptr: Any) -> Any: ...
    def phys_write(self, addr: int, type: Type[_CT], value: Any): ...

class Process:
    def read(self, addr: int, type: Type[_CT]) -> Any: ...
    def read_ptr(self, ptr: Any) -> Any: ...
    def write(self, addr: int, type: Type[_CT], value: Any): ...
    def module_info_list(self) -> List[ModuleInfo]: ...
    def module_from_name(self, name: str) -> ModuleInfo: ...

class ProcessInfo:
    @property
    def address(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def pid(self) -> int: ...

class ModuleInfo:
    @property
    def address(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def base(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def path(self) -> str: ...
