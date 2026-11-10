# Geração de Texto com GPT-2 e FastAPI

API desenvolvida com FastAPI que recebe uma frase em JSON e utiliza o modelo `gpt2` da HuggingFace, através da biblioteca `transformers`, para gerar uma continuação do texto.

## Estrutura

```
.
├── main.py           # criação da aplicação e carregamento do modelo na inicialização
├── models.py         # modelos Pydantic de requisição e resposta
├── routes.py         # endpoints da API
├── services.py       # pipeline de geração de texto do transformers
└── requirements.txt
```

## Requisitos

- Python 3.12 ou superior
- Cerca de 2 GB livres para as dependências e o modelo

## Como executar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Na primeira execução o modelo `gpt2` é baixado automaticamente do HuggingFace Hub. O modelo é carregado uma única vez, na inicialização da aplicação, e reaproveitado em todas as requisições.

A documentação interativa fica disponível em http://127.0.0.1:8000/docs.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |
| POST | `/generate` | Gera a continuação de um texto |

### POST /generate

Corpo da requisição:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `text` | string | sim | Frase de entrada (1 a 1000 caracteres) |
| `max_new_tokens` | int | não | Quantidade máxima de tokens gerados (1 a 200, padrão 50) |
| `temperature` | float | não | Criatividade da geração (maior que 0 e até 2, padrão 0.7) |

Exemplo:

```bash
curl -X POST http://127.0.0.1:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Once upon a time", "max_new_tokens": 30}'
```

Resposta:

```json
{
  "model": "gpt2",
  "input_text": "Once upon a time",
  "continuation": " he was able to talk about the importance of it...",
  "generated_text": "Once upon a time he was able to talk about the importance of it..."
}
```

Como a geração usa amostragem, cada requisição pode retornar um texto diferente. Entradas vazias ou parâmetros fora dos limites retornam status `422`.
