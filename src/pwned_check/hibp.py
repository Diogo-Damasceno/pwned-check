"""Consulta online (HIBP range API) e modo offline por arquivo local."""

import urllib.request

from .checker import match_suffix_count, sha1_hex, split_hash

HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/{prefix}"


def query_hibp(prefix: str) -> str:
    """Consulta a API de range da HIBP enviando apenas o prefixo de 5 chars."""
    url = HIBP_RANGE_URL.format(prefix=prefix.upper())
    req = urllib.request.Request(url, headers={"User-Agent": "pwned-check"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read().decode("utf-8")


def check_password_online(password: str) -> int:
    """Calcula hash, envia só o prefixo e retorna quantas vezes vazou."""
    prefix, suffix = split_hash(sha1_hex(password))
    return match_suffix_count(query_hibp(prefix), suffix)


def load_local_hashes(path: str) -> set:
    """Carrega um arquivo de hashes SHA-1 (um por linha, maiúsculas)."""
    hashes = set()
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            entry = line.strip().upper()
            if entry:
                hashes.add(entry)
    return hashes


def check_password_offline(password: str, hashes: set) -> bool:
    """Verifica a senha contra um conjunto local de hashes SHA-1."""
    return sha1_hex(password) in hashes
