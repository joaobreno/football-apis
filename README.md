# Testes de APIs — Dashboard Copa do Mundo

Este repositório reúne **experimentos e testes de integração com APIs de futebol**, no contexto de um projeto de **dashboard de visualização de estatísticas** voltado à **Copa do Mundo**.

## Objetivo

Validar endpoints, formatos de resposta, limites de uso e viabilidade dos dados antes de incorporá-los ao dashboard.

## Organização

A ideia é manter **uma pasta por provedor de API**, cada uma com **notebooks Python** (Jupyter ou similar) para:

- chamadas exploratórias aos endpoints;
- inspeção de payloads e modelagem dos dados;
- rascunhos de queries e agregações úteis ao dashboard.

Conforme novas fontes forem testadas, novos diretórios podem ser adicionados seguindo o mesmo padrão.

## API em teste (atual)

Por enquanto os testes concentram-se na **[API-Football](https://www.api-football.com/)** — documentação e planos em [api-football.com](https://www.api-football.com/).

Consulte a pasta correspondente a essa API (quando existir no repositório) para os notebooks e exemplos de uso.
