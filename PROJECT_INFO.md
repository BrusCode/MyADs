# 📊 MyADs Platform - Informações do Projeto

## ✅ Status: Completo e Publicado

**Repositório**: https://github.com/BrusCode/MyADs

---

## 🎯 Resumo

Plataforma completa de analytics para **Google Ads** e **Meta Ads** com gestão de múltiplas empresas, usuários e permissões granulares.

---

## 📦 Branches Disponíveis

### Branch `main` - Instalação Padrão ⭐
- Deploy de cada serviço individualmente no Easypanel
- Ideal para produção
- Maior controle e escalabilidade

### Branch `docker-compose` - Instalação Simplificada 🐳
- Deploy via Docker Compose
- Setup em 15 minutos
- Ideal para desenvolvimento/staging

---

## 📚 Documentação

- **README.md** - Visão geral e quick start
- **INSTALL_EASYPANEL.md** - Guia completo de instalação (2 opções)
- **QUICKSTART.md** - Início rápido em 5 minutos
- **SETUP.md** - Configuração detalhada das APIs
- **DEPLOY.md** - Deploy no Easypanel
- **CONTRIBUTING.md** - Guia de contribuição

---

## 🛠️ Stack Tecnológica

**Backend**: Python 3.11+ | FastAPI | PostgreSQL | Redis | Celery
**Frontend**: React 18+ | TypeScript | TailwindCSS | Vite
**DevOps**: Docker | Docker Compose | Nginx

---

## 🚀 Como Começar

### Opção 1: Deploy no Easypanel (Recomendado)

1. Acesse https://easypanel.io/
2. Conecte ao repositório `BrusCode/MyADs`
3. Escolha a branch (`main` ou `docker-compose`)
4. Configure variáveis de ambiente
5. Deploy automático!

📖 [Guia Completo](INSTALL_EASYPANEL.md)

### Opção 2: Local com Docker

```bash
git clone https://github.com/BrusCode/MyADs.git
cd MyADs
cp .env.example .env
docker-compose up -d
```

📖 [Quick Start](QUICKSTART.md)

---

## 📊 Estatísticas

- **51 arquivos** criados
- **~5.000 linhas** de código
- **~2.500 linhas** de documentação
- **2 branches** (main, docker-compose)
- **5 modelos** de banco de dados
- **7 routers** REST API
- **6 serviços** Docker

---

## 🎁 O Que Está Incluído

✅ Autenticação JWT + OAuth 2.0
✅ RBAC com 5 níveis de permissão
✅ Integração Google Ads API (estrutura)
✅ Integração Meta Ads API (estrutura)
✅ Dashboards responsivos
✅ Sistema de alertas
✅ Relatórios automatizados
✅ Multi-tenant
✅ Cache Redis
✅ Jobs assíncronos Celery
✅ Docker completo
✅ Documentação profissional

---

## 📞 Suporte

- **Issues**: https://github.com/BrusCode/MyADs/issues
- **Documentação**: Arquivos `.md` no repositório

---

**Desenvolvido com ❤️ por BrusCode**

