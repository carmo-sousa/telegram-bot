# Bot Telegram

![Sousa](https://img.shields.io/static/v1?label=Sousa&message=Telegram%20Bot&style=flat&color=E59500&labelColor=green)
![License](https://img.shields.io/github/license/Carmo-sousa/telegram-bot)
![Issues](https://img.shields.io/github/issues/Carmo-sousa/telegram-bot)

![Banner](assets/banner.svg)

Bot que gerência os seus usuários.
> *Feito para fins de estudo e não deve ser usado em produção.*
> *Sem segurança nenhuma.*

Esse projeto não foi bem planejado então não sei mais o que escrever aqui. Conforme for trabalhando nele eu volto.

## MVP

- [ ] Funções do BOT
  - [ ] Listar os usuários
  - [ ] Adicionar usuário
  - [ ] Editar usuário
  - [ ] Excluir usuário
- [ ] Comandos
  - [ ] `/list`
  - [ ] `/add`
  - [ ] `/edit`
  - [ ] `/update`
  - [ ] `/delete`
  - [ ] `/cancel`

## Setup

--------

1. Ter o [python 3.6](https://www.python.org/) ou superior.
2. Criar o arquivo `.env` na raiz do projeto com

  ```env
  TOKEN=<Trocar pelo token do seu bot>
  SPREADSHEET_ID=<Trocar pelo ID da sua planilha>
  RANGE_NAME = "nome_da_aba_da_planilha!Célula:Célula" # Ex: Exemplo!A1:B1
  ```

  > *O token você pode pegar com [BotFather](https://t.me/botfather) criando um novo bot.*
  > *O ID da planilha fica na URL dela*
> ![URL ID](assets/url_id.png)

3. Instalar as dependências do projeto com `pip install -r requirements.txt`

> *Se tiver o poetry configurado basta executar `poetry install`*.

4. Por fim rodar a aplicação com `python -m telegram-bot`.

## Contribuir

Quer contribuir com o projeto? [Confira o passo a passo](./CONTRIBUTING.md)
Quer ver o que está por vir? [Acompanhe aqui](https://github.com/Carmo-sousa/telegram-bot/projects)

## Versionamento

Tem mas não está certa(ainda).

## Histórico

<!-- Da uma olhada na aba [Releases](https://github.com/Carmo-sousa/telegram-bot/releases) pra acompanhar as alterações feitas no projeto. -->

Ainda não tem.

## Licença do Projeto

[MIT License](./LICENSE) © Rômulo do Carmo Sousa
