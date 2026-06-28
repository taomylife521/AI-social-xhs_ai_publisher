# Runtime Config

This project supports both source runs and packaged desktop builds. Runtime data is stored outside the application directory so packaged releases can be updated or replaced without losing user data.

## Data Directory

Default:

- Source and packaged builds: `~/.xhs_system`

Override:

- `XHS_DATA_DIR`
- `XHS_APP_DATA_DIR`

The application stores settings, database files, logs, cookies, storage state, scheduled task assets, generated images, and Playwright browsers under this directory.

## Playwright Browsers

Default:

- `${XHS_DATA_DIR}/ms-playwright`

Override:

- `PLAYWRIGHT_BROWSERS_PATH`

Packaged desktop builds should not assume Chromium is bundled. The app checks this path at runtime and can guide the user to install Chromium if it is missing.

Manual install:

```bash
PLAYWRIGHT_BROWSERS_PATH="$HOME/.xhs_system/ms-playwright" python -m playwright install chromium
```

On Windows PowerShell:

```powershell
$env:PLAYWRIGHT_BROWSERS_PATH="$HOME\.xhs_system\ms-playwright"
python -m playwright install chromium
```

## Model Runtime

Common environment variables:

- `XHS_LLM_BASE_URL`
- `XHS_LLM_MODEL`
- `XHS_LLM_API_KEY`
- `XHS_LLM_OVERRIDE`
- `XHS_LLM_TIMEOUT`
- `XHS_LLM_MAX_TOKENS`

Provider-specific keys are also supported, for example:

- `OPENAI_API_KEY`
- `ZHIPUAI_API_KEY`
- `DASHSCOPE_API_KEY`
- `MOONSHOT_API_KEY`
- `ARK_API_KEY`

## Web Runtime

The desktop application is the primary packaged target. If the FastAPI web runtime is used, configure:

- `XHS_WEB_HOST`
- `XHS_WEB_PORT`
- `XHS_WEB_DEBUG`
- `XHS_WEB_RELOAD`

Do not expose the web runtime to an untrusted network without adding authentication and restrictive CORS settings.

## Chrome Profile Runtime

Relevant variables:

- `XHS_USE_PERSISTENT_CONTEXT`
- `XHS_CHROME_USER_DATA_DIR`
- `XHS_CHROME_PROFILE_DIRECTORY`
- `XHS_AUTO_IMPORT_SYSTEM_CHROME_STATE`
- `XHS_ALLOW_CLEAR_COOKIES`

## Logs

Logs are written under:

```text
${XHS_DATA_DIR}/logs/
```

The desktop startup error log is:

```text
${XHS_DATA_DIR}/logs/xhsai_error.log
```
