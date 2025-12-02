# Sara & Lucas - Site de Casamento

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-success)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Responsive](https://img.shields.io/badge/design-responsive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-blue)

**Link do projeto:** [sara-e-lucas](https://vinisoarescastro.github.io/sara-e-lucas/)

Site de casamento completo desenvolvido para celebração real, oferecendo experiência digital moderna e intuitiva para convidados confirmarem presença, acessarem informações do evento e presentearem os noivos.

---

## Sobre o Projeto

Landing page responsiva desenvolvida para o casamento da Sara e Lucas, integrando funcionalidades essenciais para gestão de convidados e informações do evento. O projeto resolve o problema de centralizar todas as informações do casamento em um único local acessível, eliminando a necessidade de múltiplos canais de comunicação e facilitando a organização pelos noivos.

### Problema Resolvido
- **Centralização de informações**: Local único para data, horário, endereço e detalhes do evento
- **Gestão de presença**: Sistema de confirmação integrado via Google Forms
- **Lista de presentes**: Integração com plataforma de presentes e PIX
- **Engajamento**: Galeria de fotos e links para redes sociais dos noivos

---

## Funcionalidades Principais

| Funcionalidade | Descrição |
|----------------|-----------|
| **Home Interativa** | Seção hero com imagem de fundo, overlay e indicador de scroll animado (mobile) |
| **Nossa História** | Narrativa do casal com layout texto + imagem responsivo |
| **Contagem Regressiva** | Timer dinâmico em tempo real até a data do casamento |
| **Informações do Evento** | Data, horário, local e mapa do Google Maps integrado |
| **Lista de Presentes** | Link direto para loja online e opção de PIX com QR Code |
| **Confirmação RSVP** | Integração com Google Forms para gestão de convidados |
| **Galeria de Fotos** | Grid responsivo com fotos do casal |
| **Contato Social** | Cards interativos com links para Instagram dos noivos |
| **Navegação Suave** | Menu fixo com scroll suave entre seções |

---

## Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura semântica e acessível
- **CSS3**: 
  - Grid Layout e Flexbox para layouts responsivos
  - CSS Variables para gerenciamento de cores
  - Media queries para responsividade mobile-first
  - Animações e transições CSS nativas
- **JavaScript (Vanilla)**: 
  - Manipulação de DOM
  - Contagem regressiva dinâmica
  - Scroll suave e interações
  - Clipboard API para copiar chave PIX

### Backend/Ferramentas
- **Python 3.14.1**: 
  - Geração de QR Code PIX
  - Bibliotecas: `qrcode`, `Pillow (PIL)`
- **Google Forms**: Sistema de RSVP
- **Google Maps API**: Mapa interativo do local

### Design
- **Google Fonts**: Poppins (sans-serif) e Playfair Display (serif)
- **Paleta de Cores Personalizada**: Tons neutros e elegantes
- **Responsive Design**: Breakpoints otimizados para mobile, tablet e desktop

### Hospedagem
- **GitHub Pages**: Deploy estático e gratuito

---

## Estrutura do Projeto

```
sara-e-lucas/
│
├── css/
│   └── style.css          # Estilos globais e responsivos
│
├── js/
│   └── script.js          # Lógica de contagem, scroll e interações
│
├── img/                   # Imagens do casal e QR Code PIX
│
├── python/
│   └── gerar_qrcode.py    # Script para geração de QR Code
│
└── index.html             # Estrutura HTML principal
```

---

## Destaques Técnicos

### Responsividade
- **Mobile-first approach**: Design otimizado para dispositivos móveis
- **Breakpoint estratégico**: `@media (max-width: 768px)` e `(max-width: 380px)`
- **Grid adaptativo**: Layouts que transitam de múltiplas colunas para coluna única
- **Indicador de scroll mobile**: Animação de dedo apenas em telas pequenas

### Performance
- **Fontes otimizadas**: Preconnect e preload do Google Fonts
- **Imagens otimizadas**: Background-image com lazy loading do Maps
- **CSS eficiente**: Variáveis CSS para reutilização de valores
- **JavaScript leve**: Vanilla JS sem dependências externas

### UX/UI
- **Navegação intuitiva**: Menu fixo com scroll suave
- **Feedback visual**: Hover states e transições suaves
- **Acessibilidade**: Estrutura semântica e contraste adequado
- **Micro-interações**: Animações sutis que melhoram a experiência

### Integração de Terceiros
- **Google Maps embed**: Localização do evento
- **Google Forms**: RSVP sem necessidade de backend próprio
- **Infinite Pay**: Plataforma de lista de presentes

---

## Diferenciais do Projeto

- ✅ **100% responsivo**: Funciona perfeitamente em qualquer dispositivo
- ✅ **Zero dependências JS**: Código vanilla puro e performático
- ✅ **Design elegante**: Interface clean e moderna
- ✅ **Fácil manutenção**: Código organizado e comentado
- ✅ **Solução completa**: Todas funcionalidades essenciais integradas
- ✅ **Geração automatizada**: Script Python para QR Code personalizado

---

## Métricas de Qualidade

- **Linhas de código**: ~800 (CSS), ~100 (JS), ~200 (HTML)
- **Tempo de carregamento**: < 1 segundo
- **Compatibilidade**: Chrome, Firefox, Safari, Edge (últimas versões)
- **Responsividade**: 100% mobile-friendly

---

## Desenvolvedor

**Vinicius Soares Castro**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinisoarescastro/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/vinisoarescastro)

- Assessor Especial de Desenvolvimento Web & Engenharia de Dados - Câmara Municipal de Goiânia
- Engenharia de Software, UFG.
- Goiânia, Goiás, Brasil

---

## Licença

Este projeto foi desenvolvido para uso privado em evento real. O código está disponível para fins de portfólio e demonstração de habilidades técnicas.

---

## Aprendizados e Competências Demonstradas

Este projeto demonstra competências em:

- **Desenvolvimento Frontend**: HTML5, CSS3, JavaScript vanilla
- **Design Responsivo**: Mobile-first, Grid, Flexbox
- **Integração de APIs**: Google Maps, Google Forms
- **Automação**: Scripts Python para geração de assets
- **UX/UI**: Interface intuitiva e acessível
- **Gestão de Projeto**: Entrega de solução completa e funcional
- **Atenção a detalhes**: Código limpo, organizado e documentado

---

<div align="center">

**Desenvolvido com 💙 por Vinicius Soares**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
