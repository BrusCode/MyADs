# 🔧 Setup Completo - Ads Dashboard Platform

Guia detalhado para configurar completamente o **Ads Dashboard Platform** do zero.

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Configuração das APIs](#configuração-das-apis)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Deploy Local](#deploy-local)
5. [Deploy Produção](#deploy-produção)
6. [Configuração Avançada](#configuração-avançada)

---

## 🎯 Pré-requisitos

### Ferramentas Necessárias

- **Git**: Para clonar o repositório
- **Docker**: Para containerização
- **Docker Compose**: Para orquestração
- **Conta GitHub**: Para hospedar o código
- **Conta Easypanel**: Para deploy (opcional)

### Instalação das Ferramentas

#### Linux (Ubuntu/Debian)

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Git
sudo apt install git -y

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Instalar Docker Compose
sudo apt install docker-compose -y

# Verificar instalação
docker --version
docker-compose --version
```

#### macOS

```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Git
brew install git

# Instalar Docker Desktop
brew install --cask docker

# Verificar instalação
docker --version
docker-compose --version
```

#### Windows

1. Instale **Git**: https://git-scm.com/download/win
2. Instale **Docker Desktop**: https://www.docker.com/products/docker-desktop
3. Reinicie o computador

---

## 🔑 Configuração das APIs

### 1. Google Ads API

#### Passo 1: Criar Projeto no Google Cloud

1. Acesse: https://console.cloud.google.com/
2. Clique em **"Select a project"** → **"New Project"**
3. Nome: `Ads Dashboard Platform`
4. Clique em **"Create"**

#### Passo 2: Ativar Google Ads API

1. No menu lateral, vá para **"APIs & Services"** → **"Library"**
2. Busque por **"Google Ads API"**
3. Clique em **"Enable"**

#### Passo 3: Criar Credenciais OAuth 2.0

1. Vá para **"APIs & Services"** → **"Credentials"**
2. Clique em **"Create Credentials"** → **"OAuth client ID"**
3. Configure:
   - **Application type**: Web application
   - **Name**: Ads Dashboard
   - **Authorized redirect URIs**: 
     - `http://localhost:8000/api/v1/ad-accounts/google-ads/callback`
     - `https://seu-dominio.com/api/v1/ad-accounts/google-ads/callback`
4. Clique em **"Create"**
5. **Copie** o Client ID e Client Secret

#### Passo 4: Obter Developer Token

1. Acesse: https://ads.google.com/
2. Vá para **"Tools & Settings"** → **"API Center"**
3. Clique em **"Apply for access"**
4. Preencha o formulário
5. Aguarde aprovação (pode levar alguns dias)
6. Após aprovação, copie o **Developer Token**

### 2. Meta Ads API (Facebook/Instagram)

#### Passo 1: Criar App no Facebook Developers

1. Acesse: https://developers.facebook.com/
2. Clique em **"My Apps"** → **"Create App"**
3. Selecione **"Business"**
4. Preencha:
   - **App Name**: Ads Dashboard Platform
   - **Contact Email**: seu-email@example.com
5. Clique em **"Create App"**

#### Passo 2: Adicionar Produto Marketing API

1. No dashboard do app, clique em **"Add Product"**
2. Encontre **"Marketing API"** e clique em **"Set Up"**

#### Passo 3: Configurar OAuth

1. Vá para **"Settings"** → **"Basic"**
2. Copie o **App ID** e **App Secret**
3. Em **"App Domains"**, adicione: `localhost` e `seu-dominio.com`
4. Clique em **"Save Changes"**

#### Passo 4: Configurar Redirect URIs

1. Vá para **"Facebook Login"** → **"Settings"**
2. Em **"Valid OAuth Redirect URIs"**, adicione:
   - `http://localhost:8000/api/v1/ad-accounts/meta-ads/callback`
   - `https://seu-dominio.com/api/v1/ad-accounts/meta-ads/callback`
3. Clique em **"Save Changes"**

#### Passo 5: Solicitar Permissões

1. Vá para **"App Review"** → **"Permissions and Features"**
2. Solicite as seguintes permissões:
   - `ads_read`
   - `ads_management`
   - `business_management`
3. Preencha o formulário de revisão
4. Aguarde aprovação

### 3. Email (SMTP)

#### Opção 1: Gmail

1. Acesse: https://myaccount.google.com/security
2. Ative **"2-Step Verification"**
3. Vá para **"App passwords"**
4. Selecione **"Mail"** e **"Other"**
5. Nome: `Ads Dashboard`
6. Clique em **"Generate"**
7. **Copie** a senha gerada (16 caracteres)

Configuração:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=senha-de-app-gerada
```

#### Opção 2: SendGrid

1. Acesse: https://sendgrid.com/
2. Crie uma conta gratuita (100 emails/dia)
3. Vá para **"Settings"** → **"API Keys"**
4. Clique em **"Create API Key"**
5. Nome: `Ads Dashboard`
6. Permissões: **"Full Access"**
7. **Copie** a API Key

Configuração:
```env
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASSWORD=sua-api-key-aqui
```

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/ads-dashboard-platform.git
cd ads-dashboard-platform
```

### 2. Configurar Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com suas credenciais
nano .env
# ou
vim .env
# ou
code .env  # VS Code
```

### 3. Configuração Mínima (.env)

```env
# ==============================================
# CONFIGURAÇÃO MÍNIMA PARA DESENVOLVIMENTO
# ==============================================

# Environment
ENVIRONMENT=development

# Database
DATABASE_URL=postgresql://adsdashboard:changeme@postgres:5432/adsdashboard

# Redis
REDIS_URL=redis://:changeme@redis:6379/0

# JWT (GERAR NOVA CHAVE!)
SECRET_KEY=cole-aqui-a-chave-gerada-abaixo

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=seu-developer-token
GOOGLE_ADS_CLIENT_ID=seu-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=seu-client-secret

# Meta Ads API
META_APP_ID=seu-app-id
META_APP_SECRET=seu-app-secret

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASSWORD=sua-senha-de-app
```

### 4. Gerar SECRET_KEY

```bash
# Gerar chave secreta forte
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Copie o resultado e cole no .env
```

---

## 🚀 Deploy Local

### 1. Iniciar Serviços

```bash
# Usando Docker Compose
docker-compose up -d

# Verificar status
docker-compose ps
```

### 2. Executar Migrations

```bash
# Criar tabelas no banco
docker-compose exec backend alembic upgrade head
```

### 3. Criar Usuário Admin

```bash
docker-compose exec backend python -c "
from app.database import SessionLocal
from app.models import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = SessionLocal()

user = User(
    email='admin@example.com',
    hashed_password=pwd_context.hash('Admin@123'),
    full_name='Administrador',
    role=UserRole.SUPER_ADMIN,
    is_active=True,
    is_verified=True
)

db.add(user)
db.commit()
print('✅ Usuário admin criado!')
print('Email: admin@example.com')
print('Senha: Admin@123')
"
```

### 4. Acessar Aplicação

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### 5. Verificar Logs

```bash
# Todos os serviços
docker-compose logs -f

# Serviço específico
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f celery_worker
```

---

## 🌐 Deploy Produção (Easypanel)

### 1. Preparar Repositório

```bash
# Commit todas as alterações
git add .
git commit -m "feat: configuração inicial"

# Push para GitHub
git push origin main
```

### 2. Configurar no Easypanel

Siga o guia completo em: **[DEPLOY.md](DEPLOY.md)**

Resumo:
1. Criar projeto no Easypanel
2. Conectar ao GitHub
3. Adicionar PostgreSQL e Redis
4. Configurar variáveis de ambiente
5. Deploy automático

### 3. Configurar Domínio

#### Opção 1: Subdomínio Easypanel (Gratuito)

Easypanel fornece automaticamente:
- `https://seu-projeto.easypanel.host`

#### Opção 2: Domínio Personalizado

1. Registre um domínio (ex: Registro.br, GoDaddy, Namecheap)
2. Configure DNS:
   ```
   Tipo: CNAME
   Nome: @
   Valor: seu-projeto.easypanel.host
   TTL: 3600
   ```
3. No Easypanel, adicione o domínio personalizado
4. Aguarde propagação DNS (até 24h)

### 4. Configurar SSL/HTTPS

Easypanel configura SSL automaticamente com Let's Encrypt.

Verifique:
```bash
curl -I https://seu-dominio.com
```

Deve retornar: `HTTP/2 200`

---

## 🔧 Configuração Avançada

### 1. Configurar Sentry (Monitoramento de Erros)

1. Acesse: https://sentry.io/
2. Crie conta gratuita
3. Crie novo projeto Python
4. Copie o DSN
5. Adicione ao `.env`:
   ```env
   SENTRY_DSN=https://xxx@xxx.ingest.sentry.io/xxx
   ```

### 2. Configurar Backups Automáticos

#### Backup do PostgreSQL

```bash
# Criar script de backup
cat > backup.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
docker-compose exec -T postgres pg_dump -U adsdashboard adsdashboard > backup_$DATE.sql
echo "Backup criado: backup_$DATE.sql"
EOF

chmod +x backup.sh

# Adicionar ao cron (diariamente às 2h)
crontab -e
# Adicione: 0 2 * * * /caminho/para/backup.sh
```

#### Backup no Easypanel

1. Vá para o serviço PostgreSQL
2. Clique em **"Backups"**
3. Configure:
   - **Frequency**: Daily
   - **Retention**: 7 days
4. Clique em **"Enable"**

### 3. Configurar Logs Centralizados

#### Opção 1: Papertrail (Gratuito até 50MB/mês)

1. Acesse: https://papertrailapp.com/
2. Crie conta
3. Adicione novo sistema
4. Copie o endpoint (ex: `logs.papertrailapp.com:12345`)
5. Configure no `docker-compose.yml`:

```yaml
logging:
  driver: syslog
  options:
    syslog-address: "udp://logs.papertrailapp.com:12345"
    tag: "ads-dashboard"
```

### 4. Configurar Monitoramento

#### Opção 1: Uptime Robot (Gratuito)

1. Acesse: https://uptimerobot.com/
2. Crie conta
3. Adicione novo monitor:
   - **Type**: HTTP(S)
   - **URL**: `https://seu-dominio.com/health`
   - **Interval**: 5 minutes
4. Configure alertas por email

### 5. Configurar CDN (Opcional)

#### Cloudflare (Gratuito)

1. Acesse: https://cloudflare.com/
2. Adicione seu domínio
3. Configure DNS para apontar para Cloudflare
4. Ative:
   - **SSL/TLS**: Full (strict)
   - **Caching**: Standard
   - **Minify**: JS, CSS, HTML
   - **Brotli**: On

---

## 🧪 Testes

### Backend

```bash
# Executar todos os testes
docker-compose exec backend pytest

# Com cobertura
docker-compose exec backend pytest --cov=app

# Teste específico
docker-compose exec backend pytest app/tests/test_auth.py
```

### Frontend

```bash
# Executar todos os testes
docker-compose exec frontend npm test

# Com cobertura
docker-compose exec frontend npm test -- --coverage

# Modo watch
docker-compose exec frontend npm test -- --watch
```

---

## 📊 Monitoramento de Performance

### Métricas do Backend

```bash
# Acessar Flower (Celery monitoring)
# Adicione ao docker-compose.yml:
flower:
  build: ./backend
  command: celery -A app.tasks.celery_app flower
  ports:
    - "5555:5555"
  environment:
    - CELERY_BROKER_URL=${REDIS_URL}

# Acesse: http://localhost:5555
```

### Métricas do Banco de Dados

```bash
# Conectar ao PostgreSQL
docker-compose exec postgres psql -U adsdashboard -d adsdashboard

# Ver tamanho do banco
SELECT pg_size_pretty(pg_database_size('adsdashboard'));

# Ver tabelas maiores
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
LIMIT 10;
```

---

## 🔒 Segurança

### Checklist de Segurança

- [ ] SECRET_KEY forte e único
- [ ] Senhas do banco alteradas
- [ ] HTTPS configurado
- [ ] CORS configurado corretamente
- [ ] Rate limiting ativado
- [ ] Backups automáticos configurados
- [ ] Monitoramento de erros (Sentry)
- [ ] Logs centralizados
- [ ] Firewall configurado
- [ ] Atualizações automáticas de segurança

### Hardening do Sistema

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Configurar firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# Desabilitar root login SSH
sudo nano /etc/ssh/sshd_config
# Altere: PermitRootLogin no
sudo systemctl restart sshd
```

---

## 📞 Suporte

Se precisar de ajuda:

- **Documentação**: [README.md](README.md)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Deploy**: [DEPLOY.md](DEPLOY.md)
- **Issues**: https://github.com/seu-usuario/ads-dashboard-platform/issues
- **Email**: suporte@seudominio.com

---

**Setup completo! Sua plataforma está pronta para uso! 🎉**

