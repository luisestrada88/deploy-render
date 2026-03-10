# gen-ai

1. [gan intro](https://docs.google.com/presentation/d/1Q8qyHsPRX2zkt_sUJHJ2PTe3l1FdXIL-i1Su4FCtju4/edit?usp=sharing)
2. [gan learning path](https://docs.google.com/presentation/d/1ea8k0oNk-X4CkvdxCbI1q_Z3Q13x6YC1xoLXN6o4BzY/edit?usp=sharing)
3. [AutoEncoders](https://docs.google.com/presentation/d/1NXnr4d4OAKTK7s5TiV0HO9yksxiQGcU5v7dhgzfJ8jY/edit?usp=sharing)

## API TensorFlow (Autoencoder)

### Ejecutar local

- `pip install -r requirements.txt`
- `python run.py`

### Endpoints

- `GET /health`
- `POST /reconstruct`

Body de ejemplo:

{
  "vector": [1, 0, 1]
}

### Docker

- `docker build -t gen-ai-autoencoder .`
- `docker run -p 8000:8000 gen-ai-autoencoder`

### Postman

1. Crear request `GET http://localhost:8000/health`
2. Crear request `POST http://localhost:8000/reconstruct`
3. Header: `Content-Type: application/json`
4. Body raw JSON:

{
  "vector": [1, 0, 1]
}

### Render

1. Subir el repositorio a GitHub
2. En Render: **New +** -> **Blueprint** (usa `render.yaml`) o **Web Service**
3. Si usas Web Service manual: Environment `Docker`
4. Deploy
5. Probar:
   - `GET https://TU-SERVICIO.onrender.com/health`
   - `POST https://TU-SERVICIO.onrender.com/reconstruct`
