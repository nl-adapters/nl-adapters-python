from typing import Callable, Any


def function_to_docstring(func: Callable[..., Any]) -> Callable[..., Any]:
    


def _nl_adapter(
    func: Callable[..., Any],
    *,
    override_docstrings: bool = True,
) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        return result

    if override_docstrings:
        wrapper.__doc__ = "HI THERE!"
    return wrapper


def nl_adapter(
    *,
    override_docstrings: bool = True,
) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        return _nl_adapter(
            func,
            override_docstrings=override_docstrings
        )
    return decorator
