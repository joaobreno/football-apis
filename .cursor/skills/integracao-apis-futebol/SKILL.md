---
name: integracao-apis-futebol
description: Padrão do repositório test-football-api para integrar APIs de futebol — sempre consultar documentação antes de implementar. Use ao adicionar provedores, notebooks, clientes HTTP ou ao alterar chamadas a APIs de futebol neste projeto.
---

# Integração de APIs de futebol (este repositório)

## Regra principal

Antes de escrever ou alterar código que chama uma API de futebol:

1. **Documentação no repositório** — Procurar em pastas do provedor (ex.: `api-football/`, `docs/`) e arquivos `.md` ou exemplos locais.
2. **Documentação oficial** — Se não houver material local suficiente, consultar a URL oficial do provedor (navegador, `WebFetch` ou `WebSearch` ou ferramentas MCP adequadas).

Não assumir formato de resposta, nomes de campos, limites de rate ou autenticação sem confirmar na documentação.

## Skills por provedor

Cada API tem uma skill dedicada em `.cursor/skills/<provedor>/` com links e notas específicas. Ao trabalhar com um provedor, **ler essa skill** e seguir as fontes indicadas.

- **API-Football** — `.cursor/skills/api-football/`

Ao adicionar um novo provedor, criar uma nova pasta em `.cursor/skills/<nome-do-provedor>/` com `SKILL.md` e a URL (ou caminho) da documentação.

## Organização do código (README)

Manter **uma pasta por provedor** no repositório, com notebooks e experimentos alinhados à documentação verificada.
