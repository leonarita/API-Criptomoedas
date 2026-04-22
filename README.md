# Projeto "API para Criptomoedas"

<br>

## Projeto desenvolvido na Digital Innovation One.

Esse projeto visa fazer requisições de uma API para criptomoedas utilizando `Javascript`.

<br>

## 🚨 Novo: Alerta automático de BTC

Foi adicionado um sistema de alerta automático que:

- roda a cada 5 minutos (GitHub Actions)
- envia mensagem no Discord
- mostra variação:
  - dia
  - semana
  - mês
  - 3 meses
  - ano

### 🔧 Como configurar

1. Crie um webhook no Discord
2. No GitHub, vá em:
   - Settings → Secrets → Actions
3. Crie o secret:

```
DISCORD_WEBHOOK_URL
```

4. Pronto 🎉

O bot começará a rodar automaticamente.

<br>

## Documentação de Apoio

Projeto Web utilizando a API Coin Market Cap <br>
- [Portal do desenvolvedor](https://pro.coinmarketcap.com/account) <br>
- [Documetação de autenticação](https://coinmarketcap.com/api/documentation/v1/#section/Authentication) <br>
- [Documentação API](https://coinmarketcap.com/api/documentation/v1/#) <br>
