"""
RanZiz AI Execution Context
Version 1.0
"""


class ExecutionContext:

    def __init__(
        self,
        initial=None
    ):

        self._data = dict(
            initial or {}
        )

    def set(
        self,
        key,
        value
    ):

        self._data[key] = value

        return value

    def get(
        self,
        key,
        default=None
    ):

        return self._data.get(
            key,
            default
        )

    def has(
        self,
        key
    ):

        return key in self._data

    def remove(
        self,
        key
    ):

        return self._data.pop(
            key,
            None
        )

    def merge(
        self,
        values
    ):

        if values:

            self._data.update(
                values
            )

        return self

    def clear(self):

        self._data.clear()

    def keys(self):

        return list(
            self._data.keys()
        )

    def values(self):

        return list(
            self._data.values()
        )

    def items(self):

        return list(
            self._data.items()
        )

    def all(self):

        return dict(
            self._data
        )

    def copy(self):

        return ExecutionContext(
            self._data
        )

    def __contains__(
        self,
        key
    ):

        return key in self._data

    def __len__(self):

        return len(
            self._data
        )

    def __repr__(self):

        return (
            f"ExecutionContext("
            f"{len(self)} values)"
        )
