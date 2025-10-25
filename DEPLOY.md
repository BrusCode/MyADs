# 🚀 Guia de Deploy no Easypanel

Este guia detalha o processo completo de deploy da **Ads Dashboard Platform** no Easypanel.

## 📋 Pré-requisitos

Antes de iniciar o deploy, você precisará:

1. **Conta no Easypanel** (https://easypanel.io/)
2. **Repositório GitHub** com o código do projeto
3. **Credenciais das APIs**:
   - Google Ads Developer Token
   - Google OAuth Client ID e Secret
   - Meta App ID e Secret
   - Credenciais SMTP para envio de emails

## 🔧 Passo 1: Preparar o Repositório

### 1.1 Fork ou Clone o Repositório

```bash
git clone https://github.com/seu-usuario/ads-dashboard-platform.git
cd ads-dashboard-platform
```

### 1.2 Configure o Git (se necessário)

```bash
git config user.name "Seu Nome"
git config user.email "seu-email@example.com"
```

### 1.3 Faça Push para seu Repositório

```bash
git remote set-url origin https://github.com/seu-usuario/ads-dashboard-platform.git
git push -u origin main
```

## 🌐 Passo 2: Configurar Projeto no Easypanel

### 2.1 Criar Novo Projeto

1. Acesse o painel do Easypanel
2. Clique em **"Create Project"**
3. Dê um nome ao projeto: `ads-dashboard-platform`
4. Clique em **"Create"**

### 2.2 Conectar ao GitHub

1. No projeto criado, clique em **"Add Service"**
2. Selecione **"GitHub"**
3. Autorize o Easypanel a acessar seu repositório
4. Selecione o repositório `ads-dashboard-platform`
5. Selecione a branch `main`

## 🗄️ Passo 3: Configurar Banco de Dados

### 3.1 Adicionar PostgreSQL

1. No projeto, clique em **"Add Service"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name**: `postgres`
   - **Version**: `14`
   - **Database Name**: `adsdashboard`
   - **Username**: `adsdashboard`
   - **Password**: Gere uma senha forte
4. Clique em **"Create"**

### 3.2 Adicionar Redis

1. No projeto, clique em **"Add Service"**
2. Selecione **"Redis"**
3. Configure:
   - **Name**: `redis`
   - **Version**: `7`
   - **Password**: Gere uma senha forte
4. Clique em **"Create"**

## 🔐 Passo 4: Configurar Variáveis de Ambiente

### 4.1 Acessar Configurações do Backend

1. Clique no serviço **Backend** (FastAPI)
2. Vá para a aba **"Environment Variables"**

### 4.2 Adicionar Variáveis de Ambiente

Adicione as seguintes variáveis (copie do `.env.example` e ajuste os valores):

```env
# Environment
ENVIRONMENT=production

# Database (use a URL fornecida pelo Easypanel)
DATABASE_URL=postgresql://adsdashboard:SUA_SENHA@postgres:5432/adsdashboard

# Redis (use a URL fornecida pelo Easypanel)
REDIS_URL=redis://:SUA_SENHA_REDIS@redis:6379/0

# JWT (IMPORTANTE: Gere uma chave secreta forte)
SECRET_KEY=sua-chave-secreta-super-forte-min-32-caracteres-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=seu-google-ads-developer-token
GOOGLE_ADS_CLIENT_ID=seu-google-oauth-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=seu-google-oauth-client-secret
GOOGLE_ADS_REDIRECT_URI=https://seu-dominio.easypanel.host/api/v1/ad-accounts/google-ads/callback

# Meta Ads API
META_APP_ID=seu-meta-app-id
META_APP_SECRET=seu-meta-app-secret
META_REDIRECT_URI=https://seu-dominio.easypanel.host/api/v1/ad-accounts/meta-ads/callback

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha-de-app
SMTP_FROM_EMAIL=noreply@seudominio.com
SMTP_FROM_NAME=Ads Dashboard Platform

# CORS (adicione seu domínio)
CORS_ORIGINS=https://seu-dominio.easypanel.host,https://www.seudominio.com

# Sentry (opcional)
SENTRY_DSN=seu-sentry-dsn
```

### 4.3 Configurar Frontend

1. Clique no serviço **Frontend** (React)
2. Vá para a aba **"Environment Variables"**
3. Adicione:

```env
VITE_API_URL=https://seu-dominio.easypanel.host
VITE_GOOGLE_CLIENT_ID=seu-google-oauth-client-id.apps.googleusercontent.com
VITE_META_APP_ID=seu-meta-app-id
```

## 🔨 Passo 5: Configurar Build e Deploy

### 5.1 Backend (FastAPI)

1. No serviço Backend, vá para **"Build Settings"**
2. Configure:
   - **Build Context**: `./backend`
   - **Dockerfile Path**: `./backend/Dockerfile`
   - **Build Target**: `production`
   - **Port**: `8000`

### 5.2 Frontend (React)

1. No serviço Frontend, vá para **"Build Settings"**
2. Configure:
   - **Build Context**: `./frontend`
   - **Dockerfile Path**: `./frontend/Dockerfile`
   - **Build Target**: `production`
   - **Port**: `80`

### 5.3 Celery Worker

1. Adicione um novo serviço **"Custom"**
2. Configure:
   - **Name**: `celery-worker`
   - **Image**: Use a mesma imagem do backend
   - **Command**: `celery -A app.tasks.celery_app worker --loglevel=info --concurrency=4`
   - **Environment Variables**: Mesmas do backend

### 5.4 Celery Beat

1. Adicione um novo serviço **"Custom"**
2. Configure:
   - **Name**: `celery-beat`
   - **Image**: Use a mesma imagem do backend
   - **Command**: `celery -A app.tasks.celery_app beat --loglevel=info`
   - **Environment Variables**: Mesmas do backend

## 🌍 Passo 6: Configurar Domínio

### 6.1 Domínio Easypanel (Gratuito)

O Easypanel fornece um domínio gratuito:
- Backend: `https://seu-projeto-backend.easypanel.host`
- Frontend: `https://seu-projeto-frontend.easypanel.host`

### 6.2 Domínio Personalizado (Opcional)

1. No serviço Frontend, vá para **"Domains"**
2. Clique em **"Add Domain"**
3. Digite seu domínio: `www.seudominio.com`
4. Configure o DNS:
   - Tipo: `CNAME`
   - Nome: `www`
   - Valor: `seu-projeto.easypanel.host`
5. Aguarde propagação do DNS (até 24h)

## 🗃️ Passo 7: Executar Migrations

### 7.1 Acessar Terminal do Backend

1. No serviço Backend, clique em **"Terminal"**
2. Execute:

```bash
alembic upgrade head
```

### 7.2 Criar Usuário Admin (Opcional)

Crie um script Python para criar o primeiro usuário admin:

```bash
python -c "from app.database import SessionLocal; from app.models import User, UserRole; from passlib.context import CryptContext; pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto'); db = SessionLocal(); user = User(email='admin@example.com', hashed_password=pwd_context.hash('admin123'), full_name='Admin', role=UserRole.SUPER_ADMIN, is_active=True, is_verified=True); db.add(user); db.commit(); print('Admin user created')"
```

## ✅ Passo 8: Verificar Deploy

### 8.1 Testar Backend

Acesse: `https://seu-projeto-backend.easypanel.host/docs`

Você deve ver a documentação Swagger da API.

### 8.2 Testar Frontend

Acesse: `https://seu-projeto-frontend.easypanel.host`

Você deve ver a página de login.

### 8.3 Verificar Logs

1. No Easypanel, vá para cada serviço
2. Clique em **"Logs"**
3. Verifique se não há erros

## 🔄 Passo 9: Configurar CI/CD (Opcional)

O Easypanel faz deploy automático quando você faz push para o GitHub.

Para configurar:

1. Vá para **"Settings"** do projeto
2. Ative **"Auto Deploy"**
3. Selecione a branch `main`

Agora, sempre que você fizer push para `main`, o Easypanel fará deploy automaticamente.

## 🛡️ Passo 10: Segurança

### 10.1 Gerar SECRET_KEY Forte

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 10.2 Configurar HTTPS

O Easypanel configura HTTPS automaticamente com Let's Encrypt.

### 10.3 Configurar Backup

1. No PostgreSQL, vá para **"Backups"**
2. Configure backup automático diário
3. Escolha retenção de 7 dias

## 📊 Passo 11: Monitoramento

### 11.1 Configurar Sentry (Opcional)

1. Crie conta no Sentry: https://sentry.io/
2. Crie novo projeto Python
3. Copie o DSN
4. Adicione `SENTRY_DSN` nas variáveis de ambiente

### 11.2 Verificar Métricas

O Easypanel fornece métricas básicas:
- CPU Usage
- Memory Usage
- Network Traffic

Acesse em **"Metrics"** de cada serviço.

## 🆘 Troubleshooting

### Problema: Backend não inicia

**Solução:**
1. Verifique logs do backend
2. Confirme que `DATABASE_URL` está correta
3. Verifique se PostgreSQL está rodando

### Problema: Migrations falham

**Solução:**
```bash
# No terminal do backend
alembic downgrade -1
alembic upgrade head
```

### Problema: Frontend não conecta ao Backend

**Solução:**
1. Verifique `VITE_API_URL` no frontend
2. Confirme que `CORS_ORIGINS` no backend inclui o domínio do frontend

### Problema: Celery não processa jobs

**Solução:**
1. Verifique logs do Celery Worker
2. Confirme que `REDIS_URL` está correta
3. Reinicie o serviço Celery

## 📞 Suporte

Se precisar de ajuda:

1. **Documentação Easypanel**: https://easypanel.io/docs
2. **Issues no GitHub**: https://github.com/seu-usuario/ads-dashboard-platform/issues
3. **Email**: suporte@seudominio.com

---

**Parabéns! Sua aplicação está no ar! 🎉**

Acesse: `https://seu-projeto-frontend.easypanel.host`

