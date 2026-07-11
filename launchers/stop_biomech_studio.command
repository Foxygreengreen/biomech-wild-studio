#!/bin/zsh
PORT=8788
PIDS=$(lsof -tiTCP:${PORT} -sTCP:LISTEN 2>/dev/null)
if [ -z "$PIDS" ]; then
  echo "На порту ${PORT} ничего не запущено."
else
  echo "Останавливаю Biomech Studio на порту ${PORT}: $PIDS"
  kill $PIDS
  sleep 1
  echo "Готово. Теперь можно заново открыть open_biomech_studio.command"
fi
read "?Нажми Enter, чтобы закрыть это окно..."
