<a href="https://www.buymeacoffee.com/ArabicAI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
# MCP_Sample
based on https://www.youtube.com/watch?v=0C6aXoqzm5s

**MCP Demo 2**
has the MCP server which searches sqlite quran.db for the search word
```
# Create a new directory for our project
uv init MCPDemo2
cd MCPDemo2

# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install dependencies
uv add mcp[cli] 

# Create our server file
new-item server.py
```

**claude_desktop_config.json**
has the configuration of the above server in claude desktop app
