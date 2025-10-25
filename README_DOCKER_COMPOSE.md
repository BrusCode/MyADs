# 🐳 MyADs Platform - Docker Compose Installation

Esta branch contém a configuração otimizada para instalação via **Docker Compose** no Easypanel.

---

## 🚀 Deploy Rápido no Easypanel

### Passo 1: Criar Projeto

1. Acesse o Easypanel
2. Crie novo projeto: `myads-platform`

### Passo 2: Adicionar Serviço Docker Compose

1. Clique em **"Add Service"**
2. Selecione **"Docker Compose"**
3. Configure:
   - **Repository**: `BrusCode/MyADs`
   - **Branch**: `docker-compose`
   - **Compose File**: `docker-compose.easypanel.yml`

### Passo 3: Configurar Variáveis de Ambiente

Adicione as seguintes variáveis no Easypanel:

```env
# PostgreSQL
POSTGRES_USER=adsdashboard
POSTGRES_PASSWORD=SuaSenhaForteAqui123!
POSTGRES_DB=adsdashboard

# Redis
REDIS_PASSWORD=SuaSenhaRedisForte456!

# JWT
SECRET_KEY=sua-chave-secreta-super-forte-min-32-caracteres-aqui

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=seu-developer-token
GOOGLE_ADS_CLIENT_ID=seu-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=seu-client-secret
GOOGLE_ADS_REDIRECT_URI=https://api.seudominio.com/api/v1/ad-accounts/google-ads/callback

# Meta Ads API
META_APP_ID=seu-app-id
META_APP_SECRET=seu-app-secret
META_REDIRECT_URI=https://api.seudominio.com/api/v1/ad-accounts/meta-ads/callback

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha-de-app
SMTP_FROM_EMAIL=noreply@seudominio.com
SMTP_FROM_NAME=MyADs Platform

# CORS
CORS_ORIGINS=https://app.seudominio.com,https://www.seudominio.com

# Frontend
VITE_API_URL=https://api.seudominio.com
VITE_GOOGLE_CLIENT_ID=seu-client-id.apps.googleusercontent.com
VITE_META_APP_ID=seu-app-id

# Domínios (Easypanel)
BACKEND_DOMAIN=api.seudominio.com
FRONTEND_DOMAIN=app.seudominio.com
```

### Passo 4: Deploy

1. Clique em **"Deploy"**
2. Aguarde o build (5-10 minutos)
3. Verifique os logs

### Passo 5: Executar Migrations

Acesse o terminal do container `backend`:

```bash
alembic upgrade head
```

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
print('Email: admin@myads.com')
print('Senha: Admin@2024')
"
```

---

## ✅ Pronto!

Acesse:
- **Frontend**: https://app.seudominio.com
- **Backend API**: https://api.seudominio.com
- **API Docs**: https://api.seudominio.com/docs

---

## 📊 Serviços Incluídos

- ✅ PostgreSQL 14
- ✅ Redis 7
- ✅ Backend (FastAPI)
- ✅ Celery Worker
- ✅ Celery Beat
- ✅ Frontend (React + Nginx)

---

## 🔧 Comandos Úteis

### Ver Logs

```bash
# Todos os serviços
docker-compose -f docker-compose.easypanel.yml logs -f

# Serviço específico
docker-compose -f docker-compose.easypanel.yml logs -f backend
```

### Reiniciar Serviço

```bash
docker-compose -f docker-compose.easypanel.yml restart backend
```

### Acessar Terminal

```bash
docker-compose -f docker-compose.easypanel.yml exec backend bash
```

---

## 📞 Suporte

- **Documentação**: [INSTALL_EASYPANEL.md](INSTALL_EASYPANEL.md)
- **Issues**: https://github.com/BrusCode/MyADs/issues

---

**Deploy completo em menos de 15 minutos! 🚀**

