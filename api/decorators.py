from django.conf import settings
from rest_framework.response import Response


def _is_request_from_levio_backend(request):
    """Проверяет, что запрос пришёл с разрешённого адреса LEVIO_BACKEND_URL."""
    allowed_base = (settings.LEVIO_BACKEND_URL or "").strip().rstrip("/")
    if not allowed_base:
        return False
    origin = request.META.get("HTTP_ORIGIN", "").rstrip("/")
    referer = request.META.get("HTTP_REFERER", "").rstrip("/")
    return origin == allowed_base or referer == allowed_base or referer.startswith(allowed_base + "/")


def require_levio_backend_origin(view_func):
    """Декоратор: разрешает запрос только с адреса LEVIO_BACKEND_URL, иначе 403."""

    def wrapper(*args, **kwargs):
        request = args[1] if len(args) >= 2 else args[0]
        if not _is_request_from_levio_backend(request):
            return Response(
                {
                    "detail": "Запрос разрешён только с адреса, указанного в LEVIO_BACKEND_URL.",
                    "debug": {
                        "origin": request.META.get("HTTP_ORIGIN", "(не указан)"),
                        "referer": request.META.get("HTTP_REFERER", "(не указан)"),
                        "expected": (settings.LEVIO_BACKEND_URL or "").strip().rstrip("/") or "(не задан LEVIO_BACKEND_URL)",
                    },
                },
                status=403,
            )
        return view_func(*args, **kwargs)

    return wrapper
