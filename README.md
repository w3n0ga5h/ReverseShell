# ReverseShell

A small, from-scratch **TCP command listener** written in Python for hands-on learning of network programming and offensive-security fundamentals.

The program opens a TCP socket, waits for an incoming connection, reads commands sent over that connection, and executes each one locally through **PowerShell**, printing the output. It's a deliberately minimal build meant to demystify how sockets, connections, and command execution fit together.

> **Note:** the Python code in this repository was written **manually, by hand, without AI assistance** as a personal exercise to refresh my Python skills from the ground up. Only this README was generated with the help of AI.

---

## ⚠️ Legal & ethical disclaimer

This tool is intended **only** for:

- Learning and personal skill development
- Use on systems you **own** or have **explicit written permission** to test (e.g. your own lab, a CTF, an authorized pentest engagement)

Using tools like this against systems you do not own or are not authorized to test is **illegal** and unethical. You are solely responsible for how you use it. The author accepts no liability for misuse.

---

## How it works

1. It prints the local hostname and IP address.
2. It binds a TCP socket to an address/port (default `127.0.0.1:8080`) and listens.
3. When a client connects, it enters a loop:
   - receives up to 1024 bytes from the socket,
   - runs the received text as a command via `powershell -c <command>`,
   - prints the command's standard output and standard error locally.
4. The loop ends when the received command is `exit`.

> The current version is designed and tested on **Windows** because it executes commands through PowerShell.

---

## Requirements

- **Python 3.11+**
- **Windows** (uses PowerShell to run commands)

No third-party packages are required — it uses only the Python standard library (`socket`, `subprocess`).

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/ReverseShell.git
cd ReverseShell
```

That's it — there are no dependencies to install.

---

## Usage

### 1. Start the listener

```bash
python ReverseShell.py
```

You'll see output similar to:

```
Hostname: MY-PC
IP: 192.168.1.10
Waiting connection on port 8080
```

### 2. Connect and send commands

From another terminal, connect to the listener and type commands. For example, using **netcat**:

```bash
nc 127.0.0.1 8080
```

Then type a command (e.g. `whoami`) and press Enter. The command is executed on the machine running `ReverseShell.py`, and its output is printed there.

Send `exit` to end the session.

> **Changing the address/port:** edit the `addr = ("127.0.0.1", 8080)` line in [ReverseShell.py](ReverseShell.py) to bind to a different interface or port.
