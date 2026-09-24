# Attach a Local MCP Server to Codex Desktop

This guide configures a local Python MCP server for Codex Desktop by using the global Codex configuration file:

```text
%USERPROFILE%\.codex\config.toml
```

The MCP server uses `stdio` transport.

## 1. Verify the Python executable

Run in PowerShell:

```powershell
python -c "import sys; print(sys.executable)"
```

For this setup:

```text
C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\.venv\Scripts\python.exe
```

This must be the Python environment where the MCP server dependencies are installed.

## 2. Verify the MCP server path

From the MCP server directory, run:

```powershell
Resolve-Path .\metricflow_mcp.py
```

For this setup:

```text
C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp\metricflow_mcp.py
```

The working directory is:

```text
C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp
```

## 3. Confirm the MCP server uses `stdio`

The Python server must start with:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

Do not write normal application output to standard output while the MCP server is running, because `stdio` is used for MCP communication.

## 4. Open the Codex configuration file

Run in PowerShell:

```powershell
notepad "$HOME\.codex\config.toml"
```

On this machine the file is:

```text
C:\Users\KDrogaieva\.codex\config.toml
```

If the file does not exist, create it.

## 5. Add the MCP server configuration

Add the following block to `config.toml`:

```toml
[mcp_servers.lcom_metrics]
command = 'C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\.venv\Scripts\python.exe'
args = ['C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp\metricflow_mcp.py']
cwd = 'C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp'
startup_timeout_sec = 30
enabled = true
default_tools_approval_mode = "approve"
```

### What each setting means

- `command` — Python executable used to start the MCP server.
- `args` — path to the MCP Python file.
- `cwd` — working directory used when the MCP process starts.
- `startup_timeout_sec = 30` — gives MetricFlow/dbt extra time to initialize.
- `enabled = true` — enables the MCP server.
- `default_tools_approval_mode = "approve"` — automatically approves tools from this MCP server instead of asking for approval for every tool call.

## 6. Verify the `.env` file

The MCP server loads environment variables with:

```python
load_dotenv()
```

and expects:

```text
DBT_PROJECT_DIR
DBT_PROFILES_DIR
DBT_TARGET
```

Keep the `.env` file in the MCP working directory:

```text
lcom-plugins\
└── workbench\
    └── metricflow_mcp\
        ├── metricflow_mcp.py
        └── .env
```

Example `.env`:

```dotenv
DBT_PROJECT_DIR=C:\path\to\dbt\project
DBT_PROFILES_DIR=C:\Users\KDrogaieva\.dbt
DBT_TARGET=your_target
```

Do not put passwords or credentials directly in `config.toml` if they are already managed securely through environment variables or the dbt profile.

## 7. Restart Codex Desktop

Save `config.toml`.

Completely close Codex Desktop and start it again so the MCP configuration is reloaded.

## 8. Verify the MCP server

If the Codex CLI is available, run:

```powershell
codex mcp list
```

The configured server should appear as:

```text
lcom_metrics
```

You can also test it from Codex Desktop with a prompt such as:

```text
Use the lcom_metrics MCP server and return the available metrics.
```

Codex should be able to discover and call the tools exposed by `metricflow_mcp.py`.

## Final configuration

```toml
[mcp_servers.lcom_metrics]
command = 'C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\.venv\Scripts\python.exe'
args = ['C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp\metricflow_mcp.py']
cwd = 'C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp'
startup_timeout_sec = 30
enabled = true
default_tools_approval_mode = "approve"
```

## Troubleshooting

If the MCP server does not start:

1. Run the MCP Python file manually with the same virtual-environment Python:

   ```powershell
   & "C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\.venv\Scripts\python.exe" `
     "C:\Users\KDrogaieva\OneDrive - Learning.com\Development\lcom-plugins\workbench\metricflow_mcp\metricflow_mcp.py"
   ```

2. Verify that the required packages are installed in that virtual environment.

3. Verify that `.env` contains `DBT_PROJECT_DIR`, `DBT_PROFILES_DIR`, and `DBT_TARGET`.

4. Verify that the dbt profile and target work outside Codex.

5. Check that the paths in `config.toml` exactly match the actual Python executable and MCP server paths.

## References

OpenAI Codex configuration reference:

https://developers.openai.com/docs/config-file/config-reference

OpenAI MCP documentation:

https://developers.openai.com/learn/docs-mcp
