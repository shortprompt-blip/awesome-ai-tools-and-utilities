# ⚡ Awesome AI Tools & Utilities — Claude Code Zero-Token Toolkit

> **Suite completa di strumenti per sviluppatori AI, prompt engineering e integrazione locale di Claude Code con Ollama.**  
> Tutti i tool e le utility sono **100% client-side** e ad accesso gratuito su [ShortPrompt](https://shortprompt.altervista.org).

---

## 📌 Indice
- [🚀 Toolkit in Evidenza: Claude Code Zero-Token](#-toolkit-in-evidenza-claude-code-zero-token)
  - [Cos'è e Come Funziona](#-cosè-e-come-funziona)
  - [Architettura del Sistema](#-architettura-del-sistema)
  - [Il Ruolo di `CLAUDE.md`](#-il-ruolo-di-claudemd)
  - [Guida all'Installazione & Configurazione](#-guida-allinstallazione--configurazione)
  - [Esempio di `CLAUDE.md`](#-esempio-di-claudemd)
  - [Workflow Ibrido (Locale ↔ Cloud)](#-workflow-ibrido-locale--cloud)
- [🧰 Suite dei Tool Gratuiti di ShortPrompt](#-suite-dei-tool-gratuiti-di-shortprompt)
  - [Featured AI Developer Tools](#-featured-ai-developer-tools)
  - [Prompt Engineering & Context Optimization](#-prompt-engineering--context-optimization)
  - [Sicurezza, Cifratura & Utility Dati Locali](#-sicurezza-cifratura--utility-dati-locali)
  - [Guide Tecniche & Documentazione](#-guide-tecniche--documentazione)
- [🛡️ Perché Utilizzare Tool Client-Side](#️-perché-utilizzare-tool-client-side)
- [❓ FAQ & Troubleshooting](#-faq--troubleshooting)

---

## 🚀 Toolkit in Evidenza: Claude Code Zero-Token

### 💡 Cos'è e Come Funziona
**Claude Code** è l'agente di sviluppo da terminale sviluppato da Anthropic. Di default invia ogni richiesta ai server cloud Anthropic (Claude 3.5/3.7 Sonnet). 

Questo toolkit sfrutta la **compatibilità nativa di Ollama con l'API Messages di Anthropic**, reindirizzando le chiamate dal terminale direttamente all'hardware locale (`http://localhost:11434`).

- **Costo ZERO ($0 Token API):** Esegui ricerche semantiche, refactoring, generazione di boilerplate e unit test senza pagare API.
- **Privacy Assoluta:** Il codice e i dati rimangono interamente sulla tua macchina.
- **Funzionamento Offline:** Lavora e sviluppa anche senza connessione Internet.

---

### 🏗️ Architettura del Sistema

```
+-------------------------------------------------------------------------+
|                              IL TUO COMPUTER                            |
|                                                                         |
|  +-------------------+       HTTP Messages API       +---------------+  |
|  |  Claude Code CLI  |  ===========================> | Ollama Server |  |
|  |  (Terminal Agent) |  (http://localhost:11434)     | (Local Daemon)|  |
|  +-------------------+                               +---------------+  |
|            |                                                 |          |
|            | Legge file di contesto                          | Carica   |
|            v                                                 v          |
|  +-------------------+                               +---------------+  |
|  |     CLAUDE.md     |                               | Local Coding  |  |
|  | (Context & Rules) |                               | LLM Model     |  |
|  +-------------------+                               | (qwen/llama)  |  |
|                                                      +---------------+  |
+-------------------------------------------------------------------------+
```

1. **Reindirizzamento API:** Impostando `ANTHROPIC_BASE_URL="http://localhost:11434"`, la CLI di Claude Code dialoga con il daemon di Ollama invece che con i server cloud.
2. **Supporto Function Calling:** Ollama gestisce il protocollo di messaggistica Anthropic, consentendo a Claude Code di leggere cartelle, modificare file ed eseguire comandi di terminale.
3. **Contesto via `CLAUDE.md`:** Claude Code legge il file `CLAUDE.md` nella radice del progetto per capire comandi di build, test e stile senza spreco di risorse.

---

### 📄 Il Ruolo di `CLAUDE.md`
`CLAUDE.md` definisce le linee guida del tuo progetto per l'agente AI:
- Struttura del repository e comandi (`npm test`, `npm run build`).
- Convenzioni di codice (TypeScript, Prettier, architettura).
- Cartelle da escludere (`node_modules`, `dist`, `.next`) per non saturare la memoria del modello locale.

---

### 🛠️ Guida all'Installazione & Configurazione

#### 1. Prepara Ollama e il modello di Coding
```bash
# Installa Ollama (macOS/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Scarica un modello ottimizzato per il coding
ollama pull qwen3-coder
```

#### 2. Configura le Variabili d'Ambiente
Aggiungi al tuo `~/.zshrc` o `~/.bashrc`:
```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY="ollama"
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder"
```

#### 3. Avvia Claude Code
```bash
claude --model qwen3-coder
```
All'interno del terminale, digita `/init` per generare automaticamente il file `CLAUDE.md` del progetto.

---

### 📝 Esempio di `CLAUDE.md`
```markdown
# Context & Guidelines per Claude Code

## 🛠️ Comandi
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## 📏 Regole di Sviluppo
- Utilizzare TypeScript rigido (evitare `any`).
- Seguire la formattazione Prettier predefinita.

## 🚫 Cartelle Escluse
- `node_modules/`
- `dist/`
- `.next/`
```

---

### 🔄 Workflow Ibrido (Locale ↔ Cloud)
Configura questi alias nel tuo shell profile per passare rapidamente da locale a cloud:

```bash
# Modalità Zero-Token Locale (Ollama)
alias claude-local='export ANTHROPIC_BASE_URL="http://localhost:11434" && export ANTHROPIC_AUTH_TOKEN="ollama" && export ANTHROPIC_API_KEY="ollama" && claude --model qwen3-coder'

# Modalità Ufficiale Cloud (Anthropic API)
alias claude-cloud='unset ANTHROPIC_BASE_URL && unset ANTHROPIC_AUTH_TOKEN && unset ANTHROPIC_API_KEY && claude'
```

---

## 🧰 Suite dei Tool Gratuiti di ShortPrompt

Oltre al toolkit per Claude Code, la piattaforma [ShortPrompt](https://shortprompt.altervista.org) offre un ecosistema di strumenti per sviluppatori AI che funzionano **100% in-browser**.

### ⚡ Featured AI Developer Tools
- 🎯 **[System Prompt Builder](https://shortprompt.altervista.org/system-prompt-builder/)**: Progetta prompt di sistema deterministici per OpenAI ChatGPT, Anthropic Claude e Google Gemini con vincoli di output JSON/Markdown.
- 🗜️ **[Prompt Token Compressor](https://shortprompt.altervista.org/prompt-token-compressor-reducer/)**: Riduisci i costi delle API LLM fino al 40% rimuovendo whitespace ridondanti, frasi di riempimento e formattazioni superflue.
- 📄 **[Universal Text to PDF Converter](https://shortprompt.altervista.org/universal-text-to-pdf-converter/)**: Converti codice sorgente, documentazione Markdown e testo in file PDF compressi senza inviare dati a server remoti.

---

### 📐 Prompt Engineering & Context Optimization
- 🧮 **[AI Context Window Calculator](https://shortprompt.altervista.org/ai-context-windows-calculator/)**: Calcola l'occupazione dei token e il limite di parole per contesti da 128k, 200k e 1M di token.
- ✍️ **[AI Text Humanizer](https://shortprompt.altervista.org/ai-text-humanizer/)**: Perfeziona il testo generato da AI bilanciando la struttura delle frasi ed eliminando pattern ripetitivi.
- ⏱️ **[Voiceover Script Timer](https://shortprompt.altervista.org/ai-voiceover-script-timer/)**: Calcola la durata audio, la cadenza di parlato e i ritmi per script generati da AI.
- 💬 **[Local Private AI Chatbot](https://shortprompt.altervista.org/local-ai-chatbot/)**: Esegui modelli LLM compatti direttamente nel browser senza inviare dati online.

---

### 🔐 Sicurezza, Cifratura & Utility Dati Locali
- 🔒 **[AES-256 File Encryptor](https://shortprompt.altervista.org/aes-256-file-encryptor/)**: Cifra e decifra file e credenziali in locale tramite le Web Cryptography API.
- 🔤 **[Base64 Encoder & Decoder](https://shortprompt.altervista.org/base64-encoder-decoder/)**: Codifica e decodifica file binari e stringhe in formato Base64 in totale sicurezza.
- 🛠️ **[LLM JSON Formatter](https://shortprompt.altervista.org/llm-json-formatter/)**: Valida, pulisci e ripara payload JSON malformati restituiti dalle function call degli LLM.

---

### 📖 Guide Tecniche & Documentazione
- 🎨 **[Midjourney v6 Prompt Guide](https://shortprompt.altervista.org/midjourney-v6-prompt-guide/)**: Guida ai parametri per aspect ratio, valori stylize, Niji 6 e prompt negativi.
- 👁️ **[Local OCR Guide](https://shortprompt.altervista.org/how-to-extract-text-from-image-locally/)**: Estrarre testo da immagini direttamente nel browser con WebAssembly OCR.
- ☕ **[AI Coffee News](https://shortprompt.altervista.org/ai-coffee-news/)**: Aggiornamenti quotidiani su modelli LLM, benchmark di engineering e novità dell'ecosistema AI.

---

## 🛡️ Perché Utilizzare Tool Client-Side

I tool tradizionali per sviluppatori richiedono spesso l'invio di codice sorgente, dati utente o prompt riservati a server terzi. Tutti i tool di ShortPrompt sono sviluppati con una **Zero-Server Architecture**:
1. **Riservatezza dei Dati:** I dati non abbandonano mai la RAM del tuo dispositivo.
2. **Zero Latenza:** Esecuzione immediata tramite le API WebAssembly e V8 del browser.
3. **Nessun Tracciamento:** Zero cookie di profilazione o tracciamento lato server.

---

## 💻 Requisiti Hardware (per Claude Code Locale)

| RAM / VRAM | Modello Consigliato | Caso d'Uso |
| :--- | :--- | :--- |
| **8 GB - 16 GB** | `qwen2.5-coder:7b` / `deepseek-r1:7b` | Refactoring rapido, boilerplate, query semantiche di base. |
| **32 GB (M1/M2/M3)** | `qwen3-coder` / `glm4-flash` | Ottimo bilanciamento tra velocità e finestra di contesto. |
| **64 GB+ / GPU 24GB+** | `qwen2.5-coder:32b` / `codellama:34b` | Analisi avanzata di intere codebase complesse. |

---

## ❓ FAQ & Troubleshooting

### Claude Code richiede comunque il login Anthropic?
Verifica che le variabili d'ambiente siano state caricate correttamente nella sessione corrente con `echo $ANTHROPIC_BASE_URL`.

### I tool call (scrittura/lettura file) funzionano con Ollama?
Sì, Ollama (v0.14+) supporta nativamente le function call e il formato Anthropic Messages API, consentendo a Claude Code di interagire autonomamente con il file system.

---

## 🔗 Link & Risorse
- 🌐 **Sito Ufficiale:** [shortprompt.altervista.org](https://shortprompt.altervista.org)
- 📖 **Guida Completa Claude Code:** [Integrazione Claude Code & Skill Locali](https://shortprompt.altervista.org/claude-code-zero-token)
- 📦 **GitHub Repository:** [Awesome AI Tools & Utilities](https://github.com/shortprompt-blip/awesome-ai-tools-and-utilities)
