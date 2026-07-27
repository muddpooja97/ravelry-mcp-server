# Ravelry MCP Server

A small Model Context Protocol (MCP) server for reading data from the Ravelry API.

## What it provides

This server exposes a few useful Ravelry tools:

- `current_user()` - returns information about the authenticated user
- `search_patterns(query, page=1)` - searches Ravelry patterns
- `get_pattern(pattern_id)` - fetches a specific pattern
- `get_yarn(yarn_id)` - fetches a specific yarn

## Setup

1. Create a `.env` file Ravelry app credentials:

```env
RAVELRY_USERNAME=your-username
RAVELRY_PASSWORD=your-password
```

2. Install the required Python packages:

```bash
pip install requests python-dotenv mcp
```

3. Run the server:

```bash
python server.py
```

## Notes

The server reads credentials from the environment and requires both `RAVELRY_USERNAME` and `RAVELRY_PASSWORD` to be set.
