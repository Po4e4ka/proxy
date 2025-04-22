#!/bin/bash

PORT=${1:-5000}  # По умолчанию 5000

# Проверка наличия Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python не найден. Установите Python 3 и попробуйте снова."
    exit 1
fi

# Проверка и установка зависимостей
REQUIRED_PKGS=("flask" "flask_cors" "requests")

for pkg in "${REQUIRED_PKGS[@]}"; do
    if ! python3 -c "import $pkg" &> /dev/null; then
        echo "📦 Устанавливается $pkg..."
        pip install $pkg || pip3 install $pkg
    fi
done

# Запуск сервера
echo "🚀 Прокси-сервер запущен!"
echo "👉 Используйте: http://localhost:${PORT}/proxy для подключения"
echo

python3 main.py $PORT
