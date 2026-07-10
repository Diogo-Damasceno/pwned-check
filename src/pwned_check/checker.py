"""Núcleo do verificador de senhas vazadas.

Implementa o cálculo de hash e a lógica de matching por sufixo (k-anonymity),
isolável para testes sem rede nem arquivos.
"""

import hashlib


PREFIX_LEN = 5


def sha1_hex(password: str) -> str:
    """Retorna o SHA-1 da senha em maiúsculas hexadecimais."""
    digest = hashlib.sha1(password.encode("utf-8")).hexdigest()
    return digest.upper()


def split_hash(full_hash: str) -> tuple:
    """Divide o hash em (prefixo, sufixo) segundo o comprimento do prefixo."""
    prefix = full_hash[:PREFIX_LEN]
    suffix = full_hash[PREFIX_LEN:]
    return prefix, suffix


def count_for_suffix(range_response: str, suffix: str) -> int:
    """Procura o sufixo na resposta do range HIBP e devolve a contagem.

    A resposta vem como 'SUFIXO:CONTAGEM' por linha. Retorna 0 se ausente.
    """
    target = suffix.upper()
    for line in range_response.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")
        if len(parts) != 2:
            continue
        if parts[0].upper() == target:
            return int(parts[1])
    return 0
