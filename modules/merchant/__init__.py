from .. import dependencies as praentdependencies

from typing import List, Callable, Any

dependencies: List[Callable[..., Any]] = (
    praentdependencies + []
)  # [Depends(permission_check)]
