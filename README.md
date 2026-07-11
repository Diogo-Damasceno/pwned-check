# pwned-check

Verificador defensivo de vazamento de senhas baseado em **k-anonymity** (modelo
do [Have I Been Pwned](https://haveibeenpwned.com/)). A senha **nunca** sai da
sua máquina: apenas os 5 primeiros caracteres do SHA-1 são enviados à API.

> ⚠️ Ferramenta **educacional e defensiva**. Use apenas para verificar suas próprias
> senhas ou em contextos com autorização.

## Instalação

Pré-requisitos: **Python 3.10+**.

```bash
git clone https://github.com/Diogo-Damasceno/pwned-check.git
cd pwned-check
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

Após instalar, o comando do projeto fica disponível dentro do venv.
Para usar fora dele, crie um atalho:

```bash
mkdir -p ~/.local/bin
ln -sf "$(pwd)/.venv/bin/pwned-check" ~/.local/bin/pwned-check
```

> Dica: se `~/.local/bin` não estiver no teu `PATH`, rode
> `export PATH="$HOME/.local/bin:$PATH"` (e adicione ao `~/.bashrc`/`~/.zshrc`).


## Uso

```bash
# verifica uma senha (enviado só o prefixo SHA-1 de 5 chars)
pwned-check "MinhaSenhaForte123!"

# sem argumento, digite oculto (recomendado — não fica no histórico)
pwned-check
```

## Licença

MIT — veja `LICENSE`.
