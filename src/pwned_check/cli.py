"""Interface de linha de comando do pwned-check."""

import argparse
import sys

from .checker import sha1_hex, split_hash, match_suffix_count
from .hibp import check_password_offline, check_password_online, load_local_hashes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pwned-check",
        description="Verifica se uma senha aparece em vazamentos (k-anonymity)",
    )
    parser.add_argument("password", help="Senha a ser verificada")
    parser.add_argument(
        "--file",
        dest="hash_file",
        metavar="HASHES.txt",
        help="Arquivo local de hashes SHA-1 (modo offline puro)",
    )
    return parser


def build_result_message(count: int) -> str:
    """Monta a mensagem de saída com base na contagem de vazamentos."""
    if count > 0:
        return f"Vazada! Aparece em {count} vazamentos conhecidos."
    return "Não encontrada em vazamentos conhecidos."


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.hash_file:
        hashes = load_local_hashes(args.hash_file)
        if check_password_offline(args.password, hashes):
            print("Vazada (encontrada no arquivo local).")
            return 1
        print("Não encontrada no arquivo local.")
        return 0

    count = check_password_online(args.password)
    print(build_result_message(count))
    return 1 if count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
