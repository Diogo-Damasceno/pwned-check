# pwned-check

Verificador defensivo de vazamento de senhas baseado em **k-anonymity** (modelo
do [Have I Been Pwned](https://haveibeenpwned.com/)). A senha **nunca** sai da
sua máquina: apenas os 5 primeiros caracteres do SHA-1 são enviados à API.

## Aviso ético

Ferramenta **educacional e defensiva**. Use apenas para verificar suas próprias
senhas ou em contextos com autorização. Não a utilize para perseguir, expor ou
atacar terceiros. O autor não se responsabiliza por uso indevido.

## Instalação

```bash
pip install -e .
```

Requer Python 3.10+ (apenas biblioteca padrão; nenhuma dependência externa).

## Uso

### Online (HIBP range API)
```bash
pwned-check "minhaSenha123"
```

### Offline (arquivo local de hashes)
```bash
pwned-check --file hashes.txt "minhaSenha123"
```

No modo offline, o arquivo deve conter um hash SHA-1 (maiúsculas) por linha.

## Como funciona

1. Calcula `SHA-1` da senha (em maiúsculas hexadecimais).
2. Envia **só os 5 primeiros caracteres** (prefixo) à API pública da HIBP.
3. Confere o sufixo na lista de respostas retornadas (k-anonymity).

Como a API só recebe o prefixo, ela não sabe qual senha você está testando.

## Testes

```bash
pip install pytest
pytest tests/
```

## Licença

MIT — Copyright (c) 2026 Diogo Damasceno. Veja `LICENSE`.
