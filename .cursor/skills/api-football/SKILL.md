---
name: api-football
description: Integração com API-Football (API-Sports) v3 — autenticação, base URL, endpoints e limites conforme documentação oficial. Use ao implementar ou depurar requisições API-Football, chaves RapidAPI/api-sports, dados de ligas/jogos/jogadores ou pastas api-football neste repositório.
---

# API-Football (v3)

## Consultar documentação (obrigatório)

Sempre validar endpoints, parâmetros, códigos de resposta e modelos de dados na documentação oficial:

**https://www.api-football.com/documentation-v3**

Ordem sugerida:

1. **Local** — Arquivos em `api-football/` (ou pasta do provedor neste repo): notebooks, `README`, `docs/`, exports salvos.
2. **Oficial** — Página acima (ou subpáginas da mesma documentação v3). Se `WebFetch` falhar (timeout, bloqueio), usar `WebSearch` com termos como `api-football documentation v3` + nome do endpoint.

Não inventar paths de API, query params ou headers sem bater com a documentação.

## Contexto útil (verificar na doc se mudar)

A API é a versão **v3** do ecossistema API-Sports / API-Football. Planos (RapidAPI vs site direto), **base URL** e **header de autenticação** exatos variam conforme o canal de assinatura — a documentação v3 descreve as opções atuais.

Após consultar a doc, alinhar o código ao host e ao esquema de autenticação indicados para o teu plano.

## Neste repositório

- Manter experimentos na pasta do provedor (ex.: `api-football/`), como descrito no `README.md` da raiz.
- Ao adicionar novos endpoints, citar na mensagem de commit ou no notebook a secção da documentação consultada, quando fizer sentido.

## Recursos adicionais

Para detalhes extensos que não couberem no contexto, a própria documentação v3 permanece a fonte da verdade; evitar duplicar listas enormes de endpoints aqui.
