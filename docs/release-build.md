# Release Build

This project can be packaged with Nuitka in standalone mode. Build each operating system on that operating system; do not rely on cross-compilation for desktop releases.

## Supported Python

Use Python 3.8-3.12. Python 3.11 or 3.12 is recommended.

Python 3.13 is not currently recommended for this project because PyQt5 and the test environment can fail in that runtime.

## Install Build Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-build.txt
```

On Windows:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-build.txt
```

## Build Standalone

```bash
python scripts/build_nuitka.py --clean
```

Windows keeps the console hidden by default. To keep it visible while debugging:

```bash
python scripts/build_nuitka.py --clean --with-console
```

Print the command without running Nuitka:

```bash
python scripts/build_nuitka.py --dry-run
```

On macOS, the default output directory is under `/tmp/xhs-nuitka-dist`. This avoids local Finder/provenance extended attributes in project directories breaking the mandatory app signing step. To force a project-local output directory:

```bash
python scripts/build_nuitka.py --clean --output-dir dist-nuitka
```

## Output

Nuitka writes outputs under:

```text
macOS: /tmp/xhs-nuitka-dist/
Windows/Linux: dist-nuitka/
```

The first release target is standalone/onedir, not onefile. On macOS, Nuitka uses `app-dist`, which is standalone-style output packaged as a `.app` bundle because PyQt5 requires app mode in current Nuitka releases.

Onefile can be tested later:

```bash
python scripts/build_nuitka.py --clean --onefile
```

## Runtime Data

Packaged builds keep runtime data outside the application directory. See:

```text
docs/runtime-config.md
```

## Playwright Chromium

Chromium is not bundled in the first standalone release. The app uses:

```text
${XHS_DATA_DIR}/ms-playwright
```

Users can install Chromium with:

```bash
PLAYWRIGHT_BROWSERS_PATH="$HOME/.xhs_system/ms-playwright" python -m playwright install chromium
```

Future release variants may provide a larger offline package with Chromium preinstalled.
