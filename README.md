# Traductor IA — LangChain + OpenAI

Aplicación de traducción usando LangChain y OpenAI, desplegable en Vercel.

## Estructura
```
traductor/
├── api/
│   └── index.py        # Backend FastAPI
├── public/
│   └── index.html      # Frontend
├── requirements.txt
├── vercel.json
└── README.md
```

## Despliegue en Vercel

### 1. Instala Vercel CLI
```bash
npm install -g vercel
```

### 2. Sube el proyecto a GitHub
```bash
git init
git add .
git commit -m "Traductor IA"
git remote add origin https://github.com/TU_USUARIO/traductor-ia
git push -u origin main
```

### 3. Despliega en Vercel
```bash
vercel
```
O desde https://vercel.com → "Import Project" → selecciona tu repo de GitHub.

### 4. Configura la variable de entorno
En Vercel → Settings → Environment Variables:
- **Name:** `OPENAI_API_KEY`
- **Value:** tu API key de OpenAI

### 5. Redespliega
```bash
vercel --prod
```

## Prueba local
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="tu-key"
uvicorn api.index:app --reload
```
Abre http://localhost:8000
