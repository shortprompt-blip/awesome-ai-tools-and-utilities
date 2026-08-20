# ⚡ Awesome AI Tools & Utilities — ShortPrompt & Claude Code Toolkit

> **Suite completa di strumenti per sviluppatori AI, prompt engineering e integrazione locale di Claude Code con Ollama.**  
> Tutti i tool e le utility sono **100% client-side** e ad accesso gratuito su [ShortPrompt](https://shortprompt.altervista.org).

---

## 📌 Indice
- [🚀 Claude Code & ShortPrompt Integration](#claude-code--shortprompt-integration)
  - [Cos'è e Come Funziona](#cosè-e-come-funziona)
  - [Istruzioni & Protocolli d'Esecuzione](#istruzioni--protocolli-desecuzione)
  - [Skills e Comandi Locali](#skills-e-comandi-locali)
  - [Setup Ambiente Locale (Ollama / Docker)](#setup-ambiente-locale-ollama--docker)
- [🧰 Suite dei Tool Gratuiti di ShortPrompt](#suite-dei-tool-gratuiti-di-shortprompt)
  - [Featured AI Developer Tools](#featured-ai-developer-tools)
  - [Prompt Engineering & Context Optimization](#prompt-engineering--context-optimization)
  - [Sicurezza, Cifratura & Utility Dati Locali](#sicurezza-cifratura--utility-dati-locali)
  - [Guide Tecniche & Documentazione](#guide-tecniche--documentazione)
- [🛡️ Perché Utilizzare Tool Client-Side](#perché-utilizzare-tool-client-side)
- [💻 Requisiti Hardware](#requisiti-hardware)
- [❓ FAQ & Troubleshooting](#faq--troubleshooting)
- [🔗 Link & Risorse](#link--risorse)

---

## 🚀 Claude Code & ShortPrompt Integration

### 💡 Cos'è e Come Funziona
**Claude Code** è l'agente di sviluppo da terminale di Anthropic. Questo workspace è ottimizzato per l'esecuzione locale a **costo zero ($0 Token API)** e con un'elevata efficienza del contesto tramite l'integrazione con **Ollama** e gli script della suite **ShortPrompt**.

---

### ⚡ Istruzioni & Protocolli d'Esecuzione

Prima di avviare refactoring complessi o implementazioni multi-file, esegui lo script di briefing d'impatto locale per generare una mappa AST compressa:

```bash
python claude_impact_briefing.py --task "DESCRIZIONE_FEATURE_O_BUG"
```

#### ✂️ ShortPrompt Skill (`/shortprompt`)
Quando è necessario ottimizzare, accorciare o minificare un prompt, esegui l'engine ShortPrompt locale:

```bash
python shortprompt.py --prompt "IL_TUO_PROMPT_VERBOSE"
```

---

### 🛠️ Skills e Comandi Locali

1. **Pre-Execution Impact Briefing (`/briefing`)**: Scansiona firme AST, diff Git e grafi di importazione per creare un riassunto ad alta densità prima di eseguire compiti complessi.
   ```bash
   python claude_impact_briefing.py --task "DESCRIZIONE_DEL_TASK"
   ```

2. **ShortPrompt Engine (`/shortprompt`)**: Comprime istruzioni verbose in direttive dense e deterministiche.
   ```bash
   python shortprompt.py --prompt "TESTO_PROMPT_VERBOSE"
   ```

3. **Local Semantic Code Search (`/local-search`)**: Utilizza l'istanza locale Ollama per individuare funzioni o logica in modo semantico nei file candidati senza leggere intere cartelle.
   ```bash
   python shortprompt_local.py --search "QUERY_DA_CERCARE"
   ```

4. **Task Offloading to Local LLM (`/delegate`)**: Delega compiti di generazione semplici (mock, boilerplate, schemi) al modello locale a costo $0.
   ```bash
   python shortprompt_local.py --delegate "DESCRIZIONE_TASK" --file "PERCORSO_FILE_CONTESTO"
   ```

---

### 🚀 Setup Ambiente Locale (Ollama / Docker)
- **Host Locale:** `http://localhost:11434`
- **Modello Predefinito:** `qwen2.5-coder:1.5b`
- **Comando Docker:**
  ```bash
  docker run -d --name shortprompt-ollama -v ollama_data:/root/.ollama -p 11434:11434 ollama/ollama
  docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b
  ```

---

## 🧰 Suite dei Tool Gratuiti di ShortPrompt

Oltre al toolkit per Claude Code, la piattaforma [ShortPrompt](https://shortprompt.altervista.org) offre un ecosistema di strumenti per sviluppatori AI che funzionano **100% in-browser**.

### ⚡ Featured AI Developer Tools
- 🎯 **[System Prompt Builder](https://shortprompt.altervista.org/system-prompt-builder/)**: Progetta prompt di sistema deterministici per OpenAI ChatGPT, Anthropic Claude e Google Gemini con vincoli di output JSON/Markdown.
- 🗜️ **[Prompt Token Compressor](https://shortprompt.altervista.org/prompt-token-compressor-reducer/)**: Riduci i costi delle API LLM fino al 40% rimuovendo whitespace ridondanti, frasi di riempimento e formattazioni superflue.
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
- 👁️ **[Local OCR Guide](https://shortprompt.altervista.org/how-to-extract-text-from-image-locally/)**: Estrai testo da immagini direttamente nel browser con WebAssembly OCR.
- ☕ **[AI Coffee News](https://shortprompt.altervista.org/ai-coffee-news/)**: Aggiornamenti quotidiani su modelli LLM, benchmark di engineering e novità dell'ecosistema AI.

---

## 🛡️ Perché Utilizzare Tool Client-Side

I tool tradizionali per sviluppatori richiedono spesso l'invio di codice sorgente, dati utente o prompt riservati a server terzi. Tutti i tool di ShortPrompt sono sviluppati con una **Zero-Server Architecture**:
1. **Riservatezza dei Dati:** I dati non abbandonano mai la RAM del tuo dispositivo.
2. **Zero Latenza:** Esecuzione immediata tramite le API WebAssembly e V8 del browser.
3. **Nessun Tracciamento:** Zero cookie di profilazione o tracciamento lato server.

---

## 💻 Requisiti Hardware (per Modelli Locali)

| RAM / VRAM | Modello Consigliato | Caso d'Uso |
| :--- | :--- | :--- |
| **8 GB - 16 GB** | `qwen2.5-coder:1.5b` / `qwen2.5-coder:7b` | Briefing rapido, boilerplate, query semantiche di base. |
| **32 GB (M1/M2/M3)** | `qwen3-coder` / `glm4-flash` | Ottimo bilanciamento tra velocità e finestra di contesto. |
| **64 GB+ / GPU 24GB+** | `qwen2.5-coder:32b` / `codellama:34b` | Analisi avanzata di intere codebase complesse. |

---

## ❓ FAQ & Troubleshooting

### Come faccio a verificare se Ollama risponde correttamente?
Esegui `curl http://localhost:11434/api/tags` da terminale per verificare la lista dei modelli caricati.

### I comandi Python richiedono dipendenze esterne?
Gli script `claude_impact_briefing.py`, `shortprompt.py` e `shortprompt_local.py` sono progettati per funzionare con la libreria standard o con dipendenze minime.

---

## 🔗 Link & Risorse
- 🌐 **Sito Ufficiale:** [shortprompt.altervista.org](https://shortprompt.altervista.org)
- 📖 **Guida Completa Claude Code:** [Integrazione Claude Code & Skill Locali](https://shortprompt.altervista.org/claude-code-zero-token)
- 📦 **GitHub Repository:** [Awesome AI Tools & Utilities](https://github.com/shortprompt-blip/awesome-ai-tools-and-utilities)
