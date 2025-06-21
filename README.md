# 🎙️ ConvoCLI

> Terminal-based Conversation Logger & Analyzer  
> 🐍 Built with pure Python — no external dependencies

---

## 🚀 Features

✅ Log conversations from the command line  
✅ Add optional tags for easy filtering  
✅ View a summary of trending words  
✅ Manage your own persistent stopwords list  
✅ Filter logs by specific tag  
✅ Minimal, fast, and local (no internet needed)

---

## 💻 How to Use

### 1. 🔧 Install it locally

```bash
git clone https://github.com/note-9/convo-cli.git
cd convo-cli
pip install .
```
### 2. 📝 Commands
➕ Log a new entry
```bash
convo log "Talked to mentor about backend dev" --tags backend mentor
```
📊 View summary of most used words
```bash
convo summary
```
    You’ll also be able to add words to ignore (like “the”, “to”) — they’re stored in data/stopwords.json.

🔍 Filter logs by tag
```bash
convo filter --tag backend
```
