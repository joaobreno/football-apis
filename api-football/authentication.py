"""
Autenticação API-Football v3 (API-Sports).

Não existe fluxo de login com utilizador/senha: cada pedido GET envia a chave no
cabeçalho `x-apisports-key`. A função `verify_api_key` faz um pedido leve a
`/timezone` para confirmar que a chave é aceite (equivalente prático a um
«login» para reutilizar nos notebooks).

Variáveis de ambiente vêm de ``os.environ`` e do ficheiro ``api-football/.env``
via ``env_loader`` (sem sobrescrever chaves já definidas). Ver ``.env.example``.

Documentação: https://www.api-football.com/documentation-v3
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_BASE_URL = "https://www.example.com"
_ENV_KEYS = ("API_FOOTBALL_KEY", "APISPORTS_KEY", "X_APISPORTS_KEY")
_DEFAULT_TIMEOUT_S = 30.0


@dataclass(frozen=True)
class ApiKeyVerification:
    """Resultado de `verify_api_key` (HTTP + corpo JSON da API)."""

    ok: bool
    http_status: int
    data: dict[str, Any]


def resolve_api_key(explicit: str | None = None) -> str:
    """Devolve a chave a partir do argumento, ``os.environ`` ou ``.env`` local."""
    load_local_env()
    if explicit is not None and explicit.strip():
        return explicit.strip()
    for name in _ENV_KEYS:
        v = os.environ.get(name)
        if v and v.strip():
            return v.strip()
    raise ValueError(
        "Chave API em falta: defina API_FOOTBALL_KEY em api-football/.env "
        "(veja .env.example), exporte no ambiente, ou passe api_key=. "
        "Nomes aceites: " + ", ".join(_ENV_KEYS)
    )


def auth_headers(api_key: str | None = None) -> dict[str, str]:
    """
    Cabeçalhos para subscrição direta em api-sports.io (dashboard API-Football).

    Nos notebooks: ``requests.get(url, headers=auth_headers())``.
    """
    key = resolve_api_key(api_key)
    return {"x-apisports-key": key}


def _join_url(base: str, path: str) -> str:
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


def get_json(
    path: str,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = _DEFAULT_TIMEOUT_S,
) -> tuple[int, dict[str, Any]]:
    """
    GET autenticado; devolve (status_http, dict_json).

    `path` pode ser ``timezone`` ou ``/timezone``.
    Se `headers` for passado, é usado em vez de `auth_headers(api_key)`.
    """
    load_local_env()
    root = (base_url or os.environ.get("API_FOOTBALL_BASE_URL", DEFAULT_BASE_URL)).rstrip("/")
    url = _join_url(root, path)
    hdrs = headers if headers is not None else auth_headers(api_key)
    req = Request(url, headers=hdrs, method="GET")
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
            status = getattr(resp, "status", 200)
            return int(status), json.loads(raw)
    except HTTPError as e:
        body = e.read().decode(errors="replace")
        try:
            parsed: dict[str, Any] = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"_raw": body}
        return int(e.code), parsed
    except URLError as e:
        raise ConnectionError(str(e.reason or e)) from e


def verify_api_key(
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = _DEFAULT_TIMEOUT_S,
) -> ApiKeyVerification:
    """
    Confirma que a chave é válida com GET `/timezone` (dados de referência, documentação v3).

    Considera sucesso: HTTP 200 e lista `errors` vazia no JSON (padrão da API).
    """
    status, data = get_json(
        "/timezone",
        api_key=api_key,
        base_url=base_url,
        headers=headers,
        timeout=timeout,
    )
    errs = data.get("errors")
    ok = status == 200 and not (errs or [])
    return ApiKeyVerification(ok=ok, http_status=status, data=data)


from env_loader import load_local_env  # noqa: E402


if __name__ == "__main__":
    out = verify_api_key()
    print("ok:", out.ok, "http:", out.http_status)
    if out.data.get("errors"):
        print("errors:", out.data["errors"])
    else:
        n = len(out.data.get("response") or [])
        print("timezones na resposta:", n)

