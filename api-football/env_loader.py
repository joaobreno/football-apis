"""Carrega ``api-football/.env`` para ``os.environ`` (sem sobrescrever o que já existe).

``_loaded`` só passa a ``True`` depois de ler um ficheiro ``.env`` existente; se o ficheiro
ainda não existir na primeira tentativa, chamadas seguintes voltam a tentar.
"""

from __future__ import annotations

import os
from pathlib import Path

DOTENV_PATH = Path(__file__).resolve().parent / ".env"
_loaded = False


def load_local_env() -> None:
    global _loaded
    if _loaded:
        return
    if not DOTENV_PATH.is_file():
        # Não marcar `_loaded`: assim uma `.env` criada mais tarde (ou cwd corrigido) ainda é lida.
        return
    text = DOTENV_PATH.read_text(encoding="utf-8-sig")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if not key:
            continue
        val = value.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        os.environ.setdefault(key, val)
    _loaded = True
