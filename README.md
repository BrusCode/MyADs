# 📊 MyADs Platform

Plataforma completa de analytics e monitoramento para **Google Ads** e **Meta Ads**, com gestão de múltiplas empresas, usuários e permissões granulares.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6+-blue.svg)](https://www.typescriptlang.org/)

## 🚀 Funcionalidades

- ✅ Autenticação JWT com OAuth 2.0 (Google, Facebook)
- ✅ Sistema de permissões RBAC (5 níveis)
- ✅ Integração nativa com Google Ads API e Meta Marketing API
- ✅ Dashboards interativos e responsivos
- ✅ Relatórios automatizados com agendamento
- ✅ Sistema de alertas inteligentes
- ✅ Exportação em múltiplos formatos (PDF, Excel, CSV)
- ✅ Multi-tenant com isolamento de dados
- ✅ Cache com Redis para alta performance
- ✅ Jobs assíncronos com Celery

## 🏗️ Arquitetura

### Backend
- **Framework**: FastAPI 0.115+
- **Banco de Dados**: PostgreSQL 14+
- **Cache/Queue**: Redis 7+
- **ORM**: SQLAlchemy 2.0+
- **Jobs**: Celery + Celery Beat
- **Autenticação**: JWT + OAuth 2.0

### Frontend
- **Framework**: React 18+ com TypeScript
- **UI**: TailwindCSS + shadcn/ui
- **Gráficos**: Recharts
- **State**: Zustand + React Query
- **Build**: Vite

## 📦 Estrutura do Projeto

```
ads-dashboard-platform/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── api/            # Endpoints REST
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Lógica de negócio
│   │   ├── tasks/          # Celery tasks
│   │   └── utils/          # Utilitários
│   ├── alembic/            # Database migrations
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/               # React App
│   ├── src/
│   │   ├── components/    # Componentes React
│   │   ├── pages/         # Páginas/Rotas
│   │   ├── services/      # API clients
│   │   └── hooks/         # Custom hooks
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml      # Orquestração local
└── easypanel.yml          # Deploy Easypanel
```

## 🚀 Deploy no Easypanel

### 📌 Escolha sua Opção de Instalação

Este repositório oferece **duas opções** de instalação no Easypanel:

#### ⭐ Opção 1: Instalação Padrão (Branch: `main`) - **Recomendada para Produção**
- ✅ Deploy de cada serviço individualmente
- ✅ Maior controle e flexibilidade
- ✅ Escalabilidade independente por serviço
- ✅ Rollback independente
- ✅ Monitoramento granular
- 📖 **Guia completo**: [INSTALL_EASYPANEL.md - Opção 1](INSTALL_EASYPANEL.md#opção-1-instalação-padrão-branch-main)

#### 🐳 Opção 2: Docker Compose (Branch: `docker-compose`) - **Rápido e Simples**
- ✅ Deploy de toda a stack de uma vez
- ✅ Configuração simplificada (15 minutos)
- ✅ Ideal para desenvolvimento/staging
- ✅ Fácil replicação de ambiente
- 📖 **Guia completo**: [INSTALL_EASYPANEL.md - Opção 2](INSTALL_EASYPANEL.md#opção-2-instalação-via-docker-compose-branch-docker-compose)

**📚 Documentação Completa de Instalação**: [INSTALL_EASYPANEL.md](INSTALL_EASYPANEL.md)

---

### Pré-requisitos

1. Conta no Easypanel
2. Repositório GitHub conectado
3. Credenciais das APIs:
   - Google Ads Developer Token
   - Google OAuth Client ID/Secret
   - Meta App ID/Secret

### Passos para Deploy

1. **Fork ou Clone este repositório**
   ```bash
   git clone https://github.com/seu-usuario/ads-dashboard-platform.git
   cd ads-dashboard-platform
   ```

2. **Configure as variáveis de ambiente no Easypanel**
   - Acesse o painel do Easypanel
   - Crie um novo projeto
   - Conecte ao repositório GitHub
   - Configure as variáveis de ambiente (veja `.env.example`)

3. **Deploy automático**
   - O Easypanel detectará o `docker-compose.yml`
   - Build e deploy serão automáticos
   - Acesse via URL fornecida pelo Easypanel

### Variáveis de Ambiente Necessárias

```env
# Database
DATABASE_URL=postgresql://user:password@postgres:5432/adsdashboard

# Redis
REDIS_URL=redis://redis:6379/0

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256

# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=your-token
GOOGLE_ADS_CLIENT_ID=your-client-id
GOOGLE_ADS_CLIENT_SECRET=your-client-secret

# Meta Ads API
META_APP_ID=your-app-id
META_APP_SECRET=your-app-secret

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password
```

## 🛠️ Desenvolvimento Local

### Com Docker Compose

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ads-dashboard-platform.git
cd ads-dashboard-platform

# Configure as variáveis de ambiente
cp backend/.env.example backend/.env
# Edite backend/.env com suas credenciais

# Suba os serviços
docker-compose up -d

# Acesse a aplicação
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Sem Docker

#### Backend

```bash
cd backend

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Configure .env
cp .env.example .env

# Execute migrations
alembic upgrade head

# Inicie o servidor
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend

# Instale dependências
npm install

# Configure .env
cp .env.example .env

# Inicie o dev server
npm run dev
```

## 📚 Documentação da API

Após iniciar o backend, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🧪 Testes

### Backend

```bash
cd backend
pytest
```

### Frontend

```bash
cd frontend
npm test
```

## 🔐 Segurança

- Tokens OAuth criptografados no banco de dados
- Senhas com hash bcrypt (cost factor 12)
- Rate limiting em todos os endpoints
- CORS configurado
- Validação de input com Pydantic
- HTTPS obrigatório em produção

## 📊 Monitoramento

- **Logs**: Estruturados em JSON
- **Errors**: Sentry integration
- **Metrics**: Prometheus + Grafana (opcional)
- **Health Check**: `/health` endpoint

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **BrusCode** - *Desenvolvimento* - [BrusCode](https://github.com/BrusCode)

## 🙏 Agradecimentos

- FastAPI pela excelente framework
- React pela biblioteca UI
- Comunidade open source

## 📞 Suporte

Para suporte:
- 📧 **Email**: Abra uma issue no GitHub
- 🐛 **Bugs**: [GitHub Issues](https://github.com/BrusCode/MyADs/issues)
- 📖 **Documentação**: Veja os arquivos `.md` no repositório

---

**Desenvolvido com ❤️ para otimização de campanhas de marketing digital**

