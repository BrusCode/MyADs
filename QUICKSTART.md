# ⚡ Quick Start Guide

Guia rápido para colocar o **Ads Dashboard Platform** no ar em minutos.

## 🎯 Opção 1: Deploy no Easypanel (Recomendado)

### Passo 1: Fork o Repositório

1. Acesse: https://github.com/seu-usuario/ads-dashboard-platform
2. Clique em **"Fork"**
3. Clone para sua conta

### Passo 2: Configurar no Easypanel

1. Acesse https://easypanel.io/
2. Crie novo projeto
3. Conecte ao seu repositório GitHub
4. Adicione PostgreSQL e Redis
5. Configure variáveis de ambiente (copie do `.env.example`)
6. Deploy automático!

**Tempo estimado: 10-15 minutos**

📖 **Guia completo**: Veja [DEPLOY.md](DEPLOY.md)

---

## 💻 Opção 2: Desenvolvimento Local

### Pré-requisitos

- Docker e Docker Compose instalados
- Git instalado

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/seu-usuario/ads-dashboard-platform.git
cd ads-dashboard-platform
```

### Passo 2: Configure Variáveis de Ambiente

```bash
cp .env.example .env
# Edite .env com suas credenciais
nano .env
```

**Mínimo necessário para desenvolvimento:**
```env
DATABASE_URL=postgresql://adsdashboard:changeme@postgres:5432/adsdashboard
REDIS_URL=redis://:changeme@redis:6379/0
SECRET_KEY=sua-chave-secreta-aqui
```

### Passo 3: Inicie os Serviços

```bash
# Usando Docker Compose
docker-compose up -d

# Ou usando Makefile
make up
```

### Passo 4: Execute Migrations

```bash
# Usando Docker Compose
docker-compose exec backend alembic upgrade head

# Ou usando Makefile
make migrate
```

### Passo 5: Acesse a Aplicação

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

**Tempo estimado: 5 minutos**

---

## 🔑 Credenciais Iniciais

Por padrão, não há usuários criados. Crie o primeiro usuário admin:

```bash
docker-compose exec backend python -c "
from app.database import SessionLocal
from app.models import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db = SessionLocal()

user = User(
    email='admin@example.com',
    hashed_password=pwd_context.hash('admin123'),
    full_name='Admin User',
    role=UserRole.SUPER_ADMIN,
    is_active=True,
    is_verified=True
)

db.add(user)
db.commit()
print('✅ Admin user created!')
print('Email: admin@example.com')
print('Password: admin123')
"
```

**⚠️ IMPORTANTE**: Altere a senha após o primeiro login!

---

## 📊 Próximos Passos

### 1. Conectar Contas de Anúncios

1. Faça login na aplicação
2. Vá para **"Configurações"** → **"Contas de Anúncios"**
3. Clique em **"Conectar Google Ads"** ou **"Conectar Meta Ads"**
4. Autorize o acesso
5. Selecione as contas para monitorar

### 2. Configurar Empresa

1. Vá para **"Configurações"** → **"Empresas"**
2. Clique em **"Nova Empresa"**
3. Preencha os dados
4. Salve

### 3. Visualizar Dashboard

1. Vá para **"Dashboard"**
2. Selecione a empresa
3. Visualize métricas em tempo real

---

## 🛠️ Comandos Úteis

### Docker Compose

```bash
# Iniciar serviços
docker-compose up -d

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Reiniciar serviço específico
docker-compose restart backend

# Acessar shell do backend
docker-compose exec backend bash

# Acessar banco de dados
docker-compose exec postgres psql -U adsdashboard -d adsdashboard
```

### Makefile

```bash
# Iniciar desenvolvimento
make dev

# Ver logs
make logs

# Executar migrations
make migrate

# Criar nova migration
make migrate-create MESSAGE="add new table"

# Testes
make test-backend
make test-frontend

# Backup do banco
make backup-db

# Ver status dos serviços
make status

# Ajuda
make help
```

---

## 🐛 Troubleshooting

### Problema: Porta já em uso

```bash
# Altere as portas no docker-compose.yml
# Ou pare o serviço que está usando a porta
sudo lsof -i :8000
sudo kill -9 PID
```

### Problema: Erro de conexão com banco

```bash
# Verifique se o PostgreSQL está rodando
docker-compose ps postgres

# Reinicie o PostgreSQL
docker-compose restart postgres

# Verifique logs
docker-compose logs postgres
```

### Problema: Frontend não carrega

```bash
# Limpe cache do npm
docker-compose exec frontend npm cache clean --force

# Reinstale dependências
docker-compose exec frontend npm install

# Reinicie o frontend
docker-compose restart frontend
```

---

## 📚 Documentação Completa

- **README.md**: Visão geral do projeto
- **DEPLOY.md**: Guia completo de deploy no Easypanel
- **CONTRIBUTING.md**: Como contribuir com o projeto
- **API Docs**: http://localhost:8000/docs (após iniciar)

---

## 📞 Precisa de Ajuda?

- **Issues**: https://github.com/seu-usuario/ads-dashboard-platform/issues
- **Email**: suporte@seudominio.com
- **Documentação**: https://docs.seudominio.com

---

**Pronto! Sua plataforma está funcionando! 🎉**

Agora você pode:
- ✅ Conectar contas do Google Ads e Meta Ads
- ✅ Visualizar métricas em tempo real
- ✅ Gerar relatórios automatizados
- ✅ Configurar alertas inteligentes
- ✅ Gerenciar múltiplas empresas e usuários

