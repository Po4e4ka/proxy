# 🌀 Simple Proxy Server

A minimal Flask-based proxy server that safely forwards HTTP requests.

## 📦 Features

- Supports all HTTP methods
- Full proxying of requests and responses without modification
- Helps bypass CORS errors
- Perfect for forwarding requests from the browser to third-party services
- Works on **Windows** and **Linux**

---

### 🪟 Windows

1. Go to the `dist` folder
2. Run the binary:

```bash
windows_main.exe 8080
```

> If no port is specified, it defaults to `5000`.

---

### 🐧 Linux

1. Make the binary executable (once):

```bash
chmod +x dist/linux_main
```

2. Run it:

```bash
./dist/linux_main 8080
```

> You can also use the `run.sh` script, but you need to install dependencies first:

1. Install dependencies (once):

```bash
pip install flask flask-cors requests
```

2. Launch with:

```bash
./run.sh 8080
```

---

## 🔁 Example Request

Send a `POST` request to `http://localhost:<port>/proxy` with the following body:

```json
{
  "url": "https://httpbin.org/post",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"test\":123}"
}
```

### ✅ Example Response:

```json
{
  "status": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{...}"
}
