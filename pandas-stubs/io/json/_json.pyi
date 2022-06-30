from collections import abc
import sys
from typing import (
    Any,
    Callable,
    Optional,
    Union,
    overload,
)

from pandas.core.frame import DataFrame
from pandas.core.series import Series as Series

from pandas._typing import (
    FilePathOrBuffer,
    JSONSerializable as JSONSerializable,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

loads = ...
dumps = ...
TABLE_SCHEMA_VERSION: str = ...

def to_json(
    path_or_buf,
    obj,
    orient: Optional[str] = ...,
    date_format: str = ...,
    double_precision: int = ...,
    force_ascii: bool = ...,
    date_unit: str = ...,
    default_handler: Optional[Callable[[Any], JSONSerializable]] = ...,
    lines: bool = ...,
    compression: Optional[str] = ...,
    index: bool = ...,
    indent: int = ...,
): ...

class Writer:
    obj = ...
    orient = ...
    date_format = ...
    double_precision = ...
    ensure_ascii = ...
    date_unit = ...
    default_handler = ...
    index = ...
    indent = ...
    is_copy = ...
    def __init__(
        self,
        obj,
        orient: Optional[str],
        date_format: str,
        double_precision: int,
        ensure_ascii: bool,
        date_unit: str,
        index: bool,
        default_handler: Optional[Callable[[Any], JSONSerializable]] = ...,
        indent: int = ...,
    ) -> None: ...
    def write(self): ...

class SeriesWriter(Writer): ...
class FrameWriter(Writer): ...

class JSONTableWriter(FrameWriter):
    schema = ...
    obj = ...
    date_format = ...
    orient = ...
    index = ...
    def __init__(
        self,
        obj,
        orient: Optional[str],
        date_format: str,
        double_precision: int,
        ensure_ascii: bool,
        date_unit: str,
        index: bool,
        default_handler: Optional[Callable[[Any], JSONSerializable]] = ...,
        indent: int = ...,
    ): ...

@overload
def read_json(
    path: FilePathOrBuffer,
    orient: Optional[str] = ...,
    dtype=...,
    convert_axes=...,
    convert_dates: bool = ...,
    keep_default_dates: bool = ...,
    numpy: bool = ...,
    precise_float: bool = ...,
    date_unit: Optional[str] = ...,
    encoding: Optional[str] = ...,
    lines: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[
        Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]
    ] = ...,
    *,
    typ: Literal["series"],
) -> Series: ...
@overload
def read_json(
    path: FilePathOrBuffer,
    orient: Optional[str] = ...,
    dtype=...,
    convert_axes=...,
    convert_dates: bool = ...,
    keep_default_dates: bool = ...,
    numpy: bool = ...,
    precise_float: bool = ...,
    date_unit: Optional[str] = ...,
    encoding: Optional[str] = ...,
    lines: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[
        Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]
    ] = ...,
    *,
    typ: Literal["frame"],
) -> DataFrame: ...
@overload
def read_json(
    path: FilePathOrBuffer,
    orient: Optional[str] = ...,
    typ: Optional[str] = ...,
    dtype=...,
    convert_axes=...,
    convert_dates: bool = ...,
    keep_default_dates: bool = ...,
    numpy: bool = ...,
    precise_float: bool = ...,
    date_unit: Optional[str] = ...,
    encoding: Optional[str] = ...,
    lines: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[
        Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]
    ] = ...,
) -> Union[Series, DataFrame]: ...

class JsonReader(abc.Iterator):
    path_or_buf = ...
    orient = ...
    typ = ...
    dtype = ...
    convert_axes = ...
    convert_dates = ...
    keep_default_dates = ...
    numpy = ...
    precise_float = ...
    date_unit = ...
    encoding = ...
    compression = ...
    lines = ...
    chunksize = ...
    nrows_seen: int = ...
    should_close: bool = ...
    data = ...
    def __init__(
        self,
        filepath_or_buffer,
        orient,
        typ,
        dtype,
        convert_axes,
        convert_dates,
        keep_default_dates,
        numpy,
        precise_float,
        date_unit,
        encoding,
        lines,
        chunksize,
        compression,
    ) -> None: ...
    def read(self): ...
    def close(self) -> None: ...
    def __next__(self): ...

class Parser:
    json = ...
    orient = ...
    dtype = ...
    min_stamp = ...
    numpy = ...
    precise_float = ...
    convert_axes = ...
    convert_dates = ...
    date_unit = ...
    keep_default_dates = ...
    obj = ...
    def __init__(
        self,
        json,
        orient,
        dtype=...,
        convert_axes: bool = ...,
        convert_dates: bool = ...,
        keep_default_dates: bool = ...,
        numpy: bool = ...,
        precise_float: bool = ...,
        date_unit=...,
    ) -> None: ...
    def check_keys_split(self, decoded) -> None: ...
    def parse(self): ...

class SeriesParser(Parser): ...
class FrameParser(Parser): ...
