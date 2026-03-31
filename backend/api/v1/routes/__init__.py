from .health import router as health_router
from .income import router as income_router
from .income_categories import router as income_categories_router


__all__ = ["health_router", "income_router", "income_categories_router"]
