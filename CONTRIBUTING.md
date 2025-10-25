# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o **Ads Dashboard Platform**! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Código de Conduta

Este projeto adere a um Código de Conduta. Ao participar, você concorda em manter um ambiente respeitoso e inclusivo.

## 🚀 Como Contribuir

### 1. Fork o Repositório

```bash
git clone https://github.com/seu-usuario/ads-dashboard-platform.git
cd ads-dashboard-platform
```

### 2. Crie uma Branch

```bash
git checkout -b feature/minha-nova-feature
```

Convenções de nomenclatura:
- `feature/` - Nova funcionalidade
- `fix/` - Correção de bug
- `docs/` - Documentação
- `refactor/` - Refatoração de código
- `test/` - Testes

### 3. Faça suas Alterações

Certifique-se de:
- Seguir o estilo de código do projeto
- Adicionar testes para novas funcionalidades
- Atualizar a documentação se necessário
- Fazer commits com mensagens claras

### 4. Commit suas Alterações

```bash
git add .
git commit -m "feat: adiciona nova funcionalidade X"
```

Convenção de commits (Conventional Commits):
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Manutenção

### 5. Push para o GitHub

```bash
git push origin feature/minha-nova-feature
```

### 6. Abra um Pull Request

1. Vá para o repositório no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Descreva suas alterações
5. Aguarde revisão

## 🧪 Executando Testes

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

## 📝 Estilo de Código

### Python (Backend)

- Seguir PEP 8
- Usar Black para formatação
- Usar type hints
- Docstrings em inglês

```python
def calculate_roas(cost: float, revenue: float) -> float:
    """
    Calculate Return on Ad Spend (ROAS).
    
    Args:
        cost: Total ad spend
        revenue: Total revenue generated
    
    Returns:
        ROAS value
    """
    if cost == 0:
        return 0.0
    return revenue / cost
```

### TypeScript (Frontend)

- Seguir ESLint rules
- Usar Prettier para formatação
- Componentes funcionais com hooks
- Props tipadas

```typescript
interface DashboardCardProps {
  title: string;
  value: number;
  change: number;
}

export function DashboardCard({ title, value, change }: DashboardCardProps) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <p>{value}</p>
      <span>{change}%</span>
    </div>
  );
}
```

## 🐛 Reportando Bugs

Ao reportar bugs, inclua:

1. **Descrição clara** do problema
2. **Passos para reproduzir**
3. **Comportamento esperado**
4. **Comportamento atual**
5. **Screenshots** (se aplicável)
6. **Ambiente** (OS, browser, versões)

## 💡 Sugerindo Funcionalidades

Ao sugerir funcionalidades:

1. **Descreva o problema** que a funcionalidade resolve
2. **Descreva a solução** proposta
3. **Alternativas consideradas**
4. **Contexto adicional**

## 📚 Documentação

Ao adicionar funcionalidades, atualize:

- README.md
- Comentários no código
- Documentação da API (Swagger)
- CHANGELOG.md

## ✅ Checklist do Pull Request

Antes de submeter um PR, verifique:

- [ ] Código segue o estilo do projeto
- [ ] Testes foram adicionados/atualizados
- [ ] Todos os testes passam
- [ ] Documentação foi atualizada
- [ ] Commit messages seguem convenção
- [ ] Branch está atualizada com main
- [ ] Não há conflitos

## 🎯 Áreas que Precisam de Ajuda

- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Documentação
- [ ] Tradução (i18n)
- [ ] Melhorias de UI/UX
- [ ] Performance
- [ ] Acessibilidade

## 📞 Dúvidas?

Se tiver dúvidas, abra uma issue ou entre em contato:

- **Email**: dev@seudominio.com
- **Discord**: [Link do servidor]
- **GitHub Discussions**: [Link]

---

**Obrigado por contribuir! 🎉**

