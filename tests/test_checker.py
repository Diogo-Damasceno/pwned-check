"""Testes da lógica de hash e de matching contra resposta fake."""

from pwned_check.checker import count_for_suffix, sha1_hex, split_hash
from pwned_check.hibp import check_password_offline, load_local_hashes


def test_sha1_hex_known_value():
    # SHA-1 de "password" em maiúsculas hex.
    assert sha1_hex("password") == "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"


def test_sha1_hex_is_uppercase():
    h = sha1_hex("abc")
    assert h == h.upper()


def test_split_hash_lengths():
    full = sha1_hex("password")
    prefix, suffix = split_hash(full)
    assert len(prefix) == 5
    assert prefix + suffix == full


def test_count_for_suffix_found():
    response = "1E4C9B93F3F0682250B6CF8331B7EE68FD8:120\n" \
               "ABCDEF000000000000000000000000000000:3\n"
    suffix = sha1_hex("password")[5:]
    assert count_for_suffix(response, suffix) == 120


def test_count_for_suffix_not_found():
    response = "ABCDEF000000000000000000000000000000:3\n"
    suffix = sha1_hex("password")[5:]
    assert count_for_suffix(response, suffix) == 0


def test_count_for_suffix_case_insensitive():
    response = "1e4c9b93f3f0682250b6cf8331b7ee68fd8:42\n"
    suffix = sha1_hex("password")[5:]
    assert count_for_suffix(response, suffix) == 42


def test_check_password_offline(tmp_path):
    h = sha1_hex("secret")
    f = tmp_path / "hashes.txt"
    f.write_text(h + "\n")
    hashes = load_local_hashes(str(f))
    assert check_password_offline("secret", hashes) is True
    assert check_password_offline("other", hashes) is False
