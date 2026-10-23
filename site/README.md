# SacraScript Medieval: strona WWW

## Uruchomienie lokalne
Otwórz plik site/index.html w przeglądarce. Generator działa lokalnie i nie wymaga instalacji ani klucza API.

## Publikacja przez GitHub Pages
Workflow .github/workflows/pages.yml publikuje katalog site/ po zmianie plików strony na gałęzi main.

1. Wejdź w Settings → Pages w repozytorium.
2. W sekcji Build and deployment ustaw Source: GitHub Actions.
3. Otwórz zakładkę Actions i sprawdź wykonanie workflow „Deploy SacraScript Medieval to GitHub Pages”.
4. Po udanym wdrożeniu adres strony pojawi się w Settings → Pages oraz w podsumowaniu workflow.

Docelowy adres projektu dla konta hogcraft2-cpu to zwykle:
https://hogcraft2-cpu.github.io/sacrascript-medieval/

## Ważne ograniczenie
Obecna wersja tworzy teksty z lokalnych wzorców JavaScript. Nie korzysta z modelu AI, nie weryfikuje źródeł historycznych i nie zastępuje zatwierdzonych tekstów liturgicznych. Szkic mszy jest materiałem poglądowym, nie instrukcją sprawowania liturgii.
