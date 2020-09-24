# Telegram Bot  - Teste para Desenvolvedores Python (cloudia).</h3>
- Server: <a href="https://acpsbot.herokuapp.com/">Heroku</a>
- Telegram Bot: <a href="https://t.me/acps_bot">@acps_bot</a>


### Desenvolvimento
- Windows
- Python 3.6


### Bot Test
Substitua o conteúdo das variáveis ``bot_token`` e ``bot_user_name`` em bot_telegram\credentials.py caso você não tenha um bot para teste.

> bot_token = "1196389363:AAH2kb8zx3vigd2BfPJcP7C-yBGyYsrlDzQ"

> bot_user_name = "@acpsTest_bot"



### Para configurar o banco local
Substitua o valor de `app.config['SQLALCHEMY_DATABASE_URI']` em app.py:

> mysql://username:password@hostname/db_name


### Servidor local
1) Baixe o Ngrok https://ngrok.com/download
2) Extraia o arquivo .exe e abra o terminal na pasta que extraiu o .exe
3) Execute o comando no terminal: `ngrok.exe http 5000` . O número do comando representa o número da porta que o projeto flask funciona no seu computador. Caso seja outra porta, basta trocar o valor.
4) Copie o endereço https fornecido pelo Ngrok. Por exemplo: `https://dc1c4dbdff09.ngrok.io` e substitua o conteúdo da variável `URL` em bot_telegram\credentials.py: `URL = "https://dc1c4dbdff09.ngrok.io/"`
5) Execute o comando na pasta do projeto ``python app.py run`` para iniciar o projeto.
6) Abra o link que obteve no item 4. Aqui no exemplo é o `"https://dc1c4dbdff09.ngrok.io/"`.
7) Comece conversar com o bot.





