# 🚀 Instalação no Easypanel - MyADs Platform

Este guia apresenta **duas opções** de instalação do MyADs Platform no Easypanel.

---

## 📋 Escolha sua Opção de Instalação

### Opção 1: Instalação Padrão (Recomendada) ⭐
- Deploy de cada serviço individualmente
- Maior controle e flexibilidade
- Escalabilidade independente
- **Branch**: `main`

### Opção 2: Instalação via Docker Compose
- Deploy de toda a stack de uma vez
- Mais simples e rápido
- Ideal para ambientes de desenvolvimento/staging
- **Branch**: `docker-compose`

---

## ⭐ OPÇÃO 1: Instalação Padrão (Branch: main)

### Vantagens
✅ Maior controle sobre cada serviço
✅ Escalabilidade independente (escale apenas o que precisa)
✅ Monitoramento individual de cada componente
✅ Rollback independente por serviço
✅ Melhor para produção

### Pré-requisitos

1. Conta no Easypanel (https://easypanel.io/)
2. Repositório GitHub: `BrusCode/MyADs`
3. Credenciais das APIs (Google Ads, Meta Ads, SMTP)

---

### Passo 1: Criar Projeto no Easypanel

1. Acesse o painel do Easypanel
2. Clique em **"New Project"**
3. Nome do projeto: `myads-platform`
4. Clique em **"Create"**

---

### Passo 2: Adicionar Banco de Dados PostgreSQL

1. No projeto, clique em **"Add Service"**
2. Selecione **"PostgreSQL"**
3. Configure:
   - **Name**: `postgres`
   - **Version**: `14`
   - **Database Name**: `adsdashboard`
   - **Username**: `adsdashboard`
   - **Password**: Gere uma senha forte (ex: `P@ssw0rd!2024MyAds`)
4. Clique em **"Create"**
5. **Anote a URL de conexão** fornecida pelo Easypanel

---

### Passo 3: Adicionar Redis

1. No projeto, clique em **"Add Service"**
2. Selecione **"Redis"**
3. Configure:
   - **Name**: `redis`
   - **Version**: `7`
   - **Password**: Gere uma senha forte (ex: `R3dis!2024MyAds`)
4. Clique em **"Create"**
5. **Anote a URL de conexão** fornecida pelo Easypanel

---

### Passo 4: Adicionar Backend (FastAPI)

1. No projeto, clique em **"Add Service"**
2. Selecione **"GitHub"**
3. Configure:
   - **Name**: `backend`
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `main`
   - **Build Context**: `./backend`
   - **Dockerfile Path**: `./backend/Dockerfile`
   - **Port**: `8000`

4. **Variáveis de Ambiente** (clique em "Environment Variables"):

```env
# Environment
ENVIRONMENT=production

# Database (use a URL do PostgreSQL criado)
DATABASE_URL=postgresql://adsdashboard:SUA_SENHA@postgres:5432/adsdashboard

# Redis (use a URL do Redis criado)
REDIS_URL=redis://:SUA_SENHA_REDIS@redis:6379/0

# JWT (IMPORTANTE: Gere uma chave forte)
SECRET_KEY=sua-chave-secreta-super-forte-min-32-caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=seu-developer-token
GOOGLE_ADS_CLIENT_ID=seu-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=seu-client-secret
GOOGLE_ADS_REDIRECT_URI=https://SEU-DOMINIO/api/v1/ad-accounts/google-ads/callback

# Meta Ads API
META_APP_ID=seu-app-id
META_APP_SECRET=seu-app-secret
META_REDIRECT_URI=https://SEU-DOMINIO/api/v1/ad-accounts/meta-ads/callback

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha-de-app
SMTP_FROM_EMAIL=noreply@seudominio.com
SMTP_FROM_NAME=MyADs Platform

# CORS (adicione seu domínio frontend)
CORS_ORIGINS=https://SEU-DOMINIO-FRONTEND

# Sentry (opcional)
SENTRY_DSN=
```

5. Clique em **"Create"**

---

### Passo 5: Adicionar Celery Worker

1. No projeto, clique em **"Add Service"**
2. Selecione **"GitHub"**
3. Configure:
   - **Name**: `celery-worker`
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `main`
   - **Build Context**: `./backend`
   - **Dockerfile Path**: `./backend/Dockerfile`
   - **Command Override**: `celery -A app.tasks.celery_app worker --loglevel=info --concurrency=4`

4. **Variáveis de Ambiente**: Use as mesmas do Backend

5. Clique em **"Create"**

---

### Passo 6: Adicionar Celery Beat (Scheduler)

1. No projeto, clique em **"Add Service"**
2. Selecione **"GitHub"**
3. Configure:
   - **Name**: `celery-beat`
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `main`
   - **Build Context**: `./backend`
   - **Dockerfile Path**: `./backend/Dockerfile`
   - **Command Override**: `celery -A app.tasks.celery_app beat --loglevel=info`

4. **Variáveis de Ambiente**: Use as mesmas do Backend

5. Clique em **"Create"**

---

### Passo 7: Adicionar Frontend (React)

1. No projeto, clique em **"Add Service"**
2. Selecione **"GitHub"**
3. Configure:
   - **Name**: `frontend`
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `main`
   - **Build Context**: `./frontend`
   - **Dockerfile Path**: `./frontend/Dockerfile`
   - **Port**: `80`

4. **Variáveis de Ambiente**:

```env
VITE_API_URL=https://SEU-DOMINIO-BACKEND
VITE_GOOGLE_CLIENT_ID=seu-google-oauth-client-id.apps.googleusercontent.com
VITE_META_APP_ID=seu-meta-app-id
```

5. Clique em **"Create"**

---

### Passo 8: Executar Migrations

1. Acesse o serviço **Backend**
2. Clique em **"Terminal"**
3. Execute:

```bash
alembic upgrade head
```

---

### Passo 9: Criar Usuário Admin

No terminal do Backend, execute:

```bash
python -c "
from app.database import SessionLocal
from app.models import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = SessionLocal()

user = User(
    email='admin@myads.com',
    hashed_password=pwd_context.hash('Admin@2024'),
    full_name='Administrador',
    role=UserRole.SUPER_ADMIN,
    is_active=True,
    is_verified=True
)

db.add(user)
db.commit()
print('✅ Admin criado!')
print('Email: admin@myads.com')
print('Senha: Admin@2024')
"
```

---

### Passo 10: Configurar Domínios

#### Backend

1. No serviço Backend, vá para **"Domains"**
2. Adicione: `api.seudominio.com`
3. Configure DNS:
   ```
   Tipo: CNAME
   Nome: api
   Valor: seu-projeto.easypanel.host
   ```

#### Frontend

1. No serviço Frontend, vá para **"Domains"**
2. Adicione: `app.seudominio.com` ou `www.seudominio.com`
3. Configure DNS:
   ```
   Tipo: CNAME
   Nome: app (ou www)
   Valor: seu-projeto.easypanel.host
   ```

---

### ✅ Instalação Concluída!

Acesse:
- **Frontend**: https://app.seudominio.com
- **Backend API**: https://api.seudominio.com
- **API Docs**: https://api.seudominio.com/docs

---

## 🐳 OPÇÃO 2: Instalação via Docker Compose (Branch: docker-compose)

### Vantagens
✅ Deploy mais simples e rápido
✅ Toda a stack configurada de uma vez
✅ Ideal para desenvolvimento/staging
✅ Fácil replicação de ambiente

### Desvantagens
⚠️ Menos flexibilidade para escalar
⚠️ Rollback afeta toda a stack
⚠️ Monitoramento menos granular

---

### Passo 1: Criar Projeto no Easypanel

1. Acesse o painel do Easypanel
2. Clique em **"New Project"**
3. Nome do projeto: `myads-platform`
4. Clique em **"Create"**

---

### Passo 2: Adicionar Serviço Docker Compose

1. No projeto, clique em **"Add Service"**
2. Selecione **"Docker Compose"**
3. Configure:
   - **Name**: `myads-stack`
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `docker-compose`
   - **Compose File Path**: `./docker-compose.yml`

---

### Passo 3: Configurar Variáveis de Ambiente

Crie um arquivo `.env` no Easypanel ou configure as variáveis:

```env
# Environment
ENVIRONMENT=production
BUILD_TARGET=production

# PostgreSQL
POSTGRES_USER=adsdashboard
POSTGRES_PASSWORD=P@ssw0rd!2024MyAds
POSTGRES_DB=adsdashboard
POSTGRES_PORT=5432

# Redis
REDIS_PASSWORD=R3dis!2024MyAds
REDIS_PORT=6379

# JWT
SECRET_KEY=sua-chave-secreta-super-forte-min-32-caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=seu-developer-token
GOOGLE_ADS_CLIENT_ID=seu-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=seu-client-secret
GOOGLE_ADS_REDIRECT_URI=https://SEU-DOMINIO/api/v1/ad-accounts/google-ads/callback

# Meta Ads API
META_APP_ID=seu-app-id
META_APP_SECRET=seu-app-secret
META_REDIRECT_URI=https://SEU-DOMINIO/api/v1/ad-accounts/meta-ads/callback

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha-de-app
SMTP_FROM_EMAIL=noreply@seudominio.com
SMTP_FROM_NAME=MyADs Platform

# CORS
CORS_ORIGINS=https://SEU-DOMINIO

# Frontend
VITE_API_URL=https://SEU-DOMINIO-BACKEND
VITE_GOOGLE_CLIENT_ID=seu-google-oauth-client-id.apps.googleusercontent.com
VITE_META_APP_ID=seu-meta-app-id

# Ports
BACKEND_PORT=8000
FRONTEND_PORT=5173
NGINX_HTTP_PORT=80
NGINX_HTTPS_PORT=443
```

---

### Passo 4: Deploy

1. Clique em **"Deploy"**
2. Aguarde o build de todos os serviços
3. Verifique os logs de cada container

---

### Passo 5: Executar Migrations

1. Acesse o terminal do container `backend`
2. Execute:

```bash
alembic upgrade head
```

---

### Passo 6: Criar Usuário Admin

No terminal do container `backend`:

```bash
python -c "
from app.database import SessionLocal
from app.models import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = SessionLocal()

user = User(
    email='admin@myads.com',
    hashed_password=pwd_context.hash('Admin@2024'),
    full_name='Administrador',
    role=UserRole.SUPER_ADMIN,
    is_active=True,
    is_verified=True
)

db.add(user)
db.commit()
print('✅ Admin criado!')
"
```

---

### Passo 7: Configurar Domínio

1. Configure DNS para apontar para o Easypanel
2. No Easypanel, adicione o domínio personalizado
3. SSL será configurado automaticamente

---

### ✅ Instalação Concluída!

Acesse: https://seudominio.com

---

## 📊 Comparação das Opções

| Característica | Opção 1: Padrão | Opção 2: Docker Compose |
|----------------|-----------------|-------------------------|
| **Complexidade** | Média | Baixa |
| **Tempo de Setup** | 20-30 min | 10-15 min |
| **Escalabilidade** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Controle** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Monitoramento** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Rollback** | Independente | Toda stack |
| **Ideal para** | Produção | Dev/Staging |

---

## 🔧 Gerar SECRET_KEY

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🆘 Troubleshooting

### Problema: Serviços não iniciam

**Solução**:
1. Verifique logs de cada serviço
2. Confirme que variáveis de ambiente estão corretas
3. Verifique se PostgreSQL e Redis estão rodando

### Problema: Migrations falham

**Solução**:
```bash
# No terminal do backend
alembic downgrade -1
alembic upgrade head
```

### Problema: Frontend não conecta ao Backend

**Solução**:
1. Verifique `VITE_API_URL` no frontend
2. Confirme que `CORS_ORIGINS` no backend inclui o domínio do frontend
3. Verifique se o backend está acessível

---

## 📞 Suporte

- **Documentação Completa**: [README.md](README.md)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Setup Detalhado**: [SETUP.md](SETUP.md)
- **Issues**: https://github.com/BrusCode/MyADs/issues

---

**Escolha a opção que melhor atende suas necessidades e comece a usar o MyADs Platform! 🚀**

