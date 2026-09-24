# Add a Local MCP Server to the Codex VS Code Extension

This guide describes how to connect a local Python MCP server to the Codex VS Code extension by using a project-level `.codex/config.toml` file.

The example assumes:

- The MCP server is implemented in Python with FastMCP.
- The MCP server runs through `stdio`.
- The Python virtual environment already contains all required packages.
- The MCP server may use a `.env` file for environment variables such as dbt project paths and credentials.

---

## 1. Verify the Python Environment

Open the VS Code terminal and activate the Python environment where the MCP server already works.

Then run:

```powershell
python -c "import sys; print(sys.executable)"
```

Example result:

```text
C:\Users\<user>\Development\project\.venv\Scripts\python.exe
```

Save this full path.

Codex should start the MCP server using this exact Python executable so that all required packages are available.

---

## 2. Verify the MCP Server File Path

From the directory containing the MCP server, run:

```powershell
Resolve-Path .\metricflow_mcp.py
```

Example:

```text
C:\Users\<user>\Development\project\semantic\metricflow_mcp.py
```

Also get the directory containing the MCP server:

```powershell
Resolve-Path .
```

Example:

```text
C:\Users\<user>\Development\project\semantic
```

This directory can be used as the MCP server working directory.

---

## 3. Verify the `.env` File

If the MCP server uses:

```python
from dotenv import load_dotenv

load_dotenv()
```

keep the `.env` file in the MCP server working directory.

Example:

```text
semantic/
├── .env
├── metricflow_mcp.py
└── .venv/
```

Example `.env`:

```text
DBT_PROJECT_DIR=C:\Users\<user>\Development\dbt\LCom_DW
DBT_PROFILES_DIR=C:\Users\<user>\.dbt
DBT_TARGET=dev
```

If the `.env` file contains credentials or secrets, add it to `.gitignore`.

Example:

```gitignore
.env
```

---

## 4. Create the Codex Configuration Directory

At the root of the repository opened in VS Code, create:

```text
.codex/
```

Inside it, create:

```text
config.toml
```

The repository structure should look similar to:

```text
project/
│
├── .codex/
│   └── config.toml
│
├── AGENTS.md
│
├── semantic/
│   ├── metricflow_mcp.py
│   └── .env
│
└── ...
```

---

## 5. Add the MCP Server to `.codex/config.toml`

Add a configuration block for the MCP server.

Example:

```toml
[mcp_servers.lcom_metrics]
command = 'C:\FULL\PATH\TO\.venv\Scripts\python.exe'
args = ['C:\FULL\PATH\TO\semantic\metricflow_mcp.py']
cwd = 'C:\FULL\PATH\TO\semantic'

enabled = true
required = true
startup_timeout_sec = 60
tool_timeout_sec = 120
```

Replace the example paths with the real paths from Steps 2 and 3.

Using single quotes in TOML is convenient on Windows because backslashes do not need to be escaped.

For example:

```toml
[mcp_servers.lcom_metrics]
command = 'C:\Users\<user>\Development\project\.venv\Scripts\python.exe'
args = ['C:\Users\<user>\Development\project\semantic\metricflow_mcp.py']
cwd = 'C:\Users\<user>\Development\project\semantic'

enabled = true
required = true
startup_timeout_sec = 60
tool_timeout_sec = 120
```

### Configuration fields

- `mcp_servers.lcom_metrics` — MCP server name visible to Codex.
- `command` — Python executable used to start the server.
- `args` — path to the MCP server Python file.
- `cwd` — working directory used when the MCP process starts.
- `enabled` — enables the MCP server.
- `required` — treats the MCP server as required for the Codex session.
- `startup_timeout_sec` — maximum startup time.
- `tool_timeout_sec` — maximum execution time for an MCP tool call.

---

## 6. Restart the Codex VS Code Extension

After saving `.codex/config.toml`, restart the Codex extension.

You can also reload the VS Code window.

The MCP server should then be started automatically when Codex loads the project configuration.

---

## 7. Verify That Codex Sees the MCP Server

If the Codex CLI is installed, run:

```powershell
codex mcp list
```

The configured MCP server should appear in the list.

Example:

```text
lcom_metrics    enabled
```

You can also inspect the MCP servers from the Codex extension UI.

---

## 8. Test a Simple MCP Tool

Start with a tool that does not require complex parameters.

For example, if the MCP server exposes:

```text
get_metrics
```

ask Codex:

```text
Use the lcom_metrics MCP server and tell me which metrics are available.
```

Codex should call the MCP tool instead of generating SQL or guessing metric names.

Then test another tool, for example:

```text
Which dimensions are available for ARR?
```

Codex should call something similar to:

```text
get_dimensions(metric="arr")
```

---

## 9. Test the Full MCP Workflow

For a semantic metrics server, test a complete business question.

Example:

```text
What was ARR for California in June 2026?
Use the lcom_metrics MCP tools, not SQL.
```

A typical tool sequence can be:

```text
get_metrics
    ↓
get_dimensions
    ↓
get_state_codes
    ↓
run_metricflow_query
```

The MCP server is responsible for validating metric names, dimensions, controlled values, dates, ordering, and limits before executing the MetricFlow query.

---

## 10. Add Repository Instructions in `AGENTS.md`

Create an `AGENTS.md` file at the repository root.

Codex automatically reads repository instructions from this file.

Example:

```markdown
# Codex Instructions

## Learning.com Metrics

For questions requiring Learning.com business metric values, use the
`lcom_metrics` MCP server instead of generating SQL.

Before querying:

1. Use `get_metrics` to identify the exact metric name.
2. Use `get_dimensions` to identify dimensions available for the requested metric.
3. Use controlled-value tools such as `get_state_codes` or `get_countries`
   when filtering those dimensions.
4. Execute the metric query using `run_metricflow_query`.

Do not invent metric names, dimensions, or controlled dimension values.

If `run_metricflow_query` returns `success: false`, use the returned validation
error to correct the MCP query and retry.
```

`AGENTS.md` is separate from Codex Skills.

Use:

- `AGENTS.md` for repository-level instructions and MCP routing rules.
- Skills for reusable business knowledge, ontology, metric definitions, and workflows.
- MCP tools for retrieving or calculating actual data.

---

## 11. Recommended Architecture

```text
User question
    ↓
Codex
    ↓
AGENTS.md
    ↓
Business Knowledge Skills
    ↓
MCP tools
    ↓
MetricFlow
    ↓
dbt Semantic Layer
    ↓
Data Warehouse
```

For example:

```text
"What was ARR for CA in June 2026?"
        ↓
Codex understands the business question
        ↓
AGENTS.md tells Codex to use lcom_metrics
        ↓
Skill provides business meaning of ARR
        ↓
MCP validates metric/dimension/value names
        ↓
run_metricflow_query
        ↓
MetricFlow builds the semantic query
        ↓
Redshift returns the data
```

This keeps responsibilities separated:

- **Codex** interprets the user's request.
- **Skills** provide business context.
- **MCP** exposes controlled tools and validation.
- **MetricFlow** generates the semantic query.
- **dbt Semantic Layer** defines metrics and dimensions.
- **Redshift** provides the underlying data.

---

## Troubleshooting

### MCP server does not appear

Check:

```powershell
codex mcp list
```

Then verify:

- `.codex/config.toml` exists at the repository root.
- `command` points to the correct Python executable.
- `args` points to the correct MCP server file.
- `enabled = true`.
- The Codex extension was restarted after the configuration change.

---

### MCP server fails during startup

Run the server manually with the same Python executable configured in Codex:

```powershell
"C:\FULL\PATH\TO\.venv\Scripts\python.exe" "C:\FULL\PATH\TO\metricflow_mcp.py"
```

If it fails here, fix the Python/MCP environment before testing through Codex.

Typical causes include:

- Missing Python packages.
- Incorrect `DBT_PROJECT_DIR`.
- Incorrect `DBT_PROFILES_DIR`.
- Incorrect dbt target.
- Missing environment variables.
- Database authentication issues.

---

### `.env` values are not found

Verify that `cwd` points to the directory containing `.env`.

Example:

```toml
cwd = 'C:\Users\<user>\Development\project\semantic'
```

Alternatively, explicitly provide required environment variables through the MCP configuration.

---

### MCP protocol errors occur

Make sure the Python server does not write normal output to `stdout`.

Avoid startup code such as:

```python
print("Server started")
```

or local test blocks such as:

```python
if __name__ == "__main__":
    print(run_metricflow_query(...))
```

For the production MCP server, use only:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

Logging, if needed, should be configured so that it does not interfere with MCP `stdio` communication.

---

## Final Checklist

Before using the MCP server from Codex, confirm:

- [ ] MCP server runs with `mcp.run(transport="stdio")`
- [ ] Test `print()` statements are removed from startup code
- [ ] Correct Python virtual environment is used
- [ ] MCP Python file path is correct
- [ ] `.env` is available
- [ ] `.env` is excluded from Git if it contains secrets
- [ ] `.codex/config.toml` exists
- [ ] MCP server is enabled in `config.toml`
- [ ] Codex extension has been restarted
- [ ] `codex mcp list` shows the server
- [ ] Simple MCP tool call works
- [ ] Full metric workflow works
- [ ] `AGENTS.md` contains MCP usage instructions
