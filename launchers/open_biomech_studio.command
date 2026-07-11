#!/bin/zsh
cd "/Users/evgenijarazguljaeva/Documents/Codex/biomech-wild-studio-publish" || exit 1

PORT=8788
URL="http://localhost:${PORT}/"

if lsof -nP -iTCP:${PORT} -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Biomech Studio уже запущена на ${URL}"
  open "${URL}"
  echo "Если страница выглядит старой, останови старый сервер в Терминале через Ctrl+C и запусти этот файл ещё раз."
  read "?Нажми Enter, чтобы закрыть это окно..."
  exit 0
fi

open "${URL}"
echo "Запускаю Biomech Studio на ${URL}"
echo "Не закрывай это окно, пока работаешь со страницей."
python3 -m http.server ${PORT}
