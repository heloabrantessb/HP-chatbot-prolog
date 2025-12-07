1. ### Clonar projeto
```bash
git clone https://github.com/heloabrantessb/HP-chatbot-prolog.git
```
2. ### Definir variáveis 
Mude o nome do arquivo **.env.example** para apenas **.env** e em seguida preencha as informações de conexão.

```txt
HOST = 
USER = 
PASSWORD =  
DATABASE = 
```

3. ### Subir containers Docker
```bash
docker compose up --build -d
```

4. ### Entrar no container
```bash
docker exec -it chatbot-prolog bash
```

5. ### Testar se está funcionando
```bash
python main.py
```

