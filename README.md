# 📖 Book Page Tracker

A Python class that simulates reading a book: it keeps track of the current page, lets you turn pages forward and warns you when you reach the end. Terminal output is colorful thanks to the [`rich`](https://github.com/Textualize/rich) library.

## Features

- Opens a book with a title and a total number of pages, starting on page 1
- Advances any number of pages, printing each page turned
- Never goes past the last page: asking for more pages than remain stops at the end
- Shows an alert when the end of the book is reached
- Colored text and emojis in the terminal

## Concepts practiced

- Classes, `__init__` and instance state (`pagina_atual`)
- Boundary handling (`if`/`else` around the last page)
- `for` loops with `range`
- Using a third-party library (`rich`)

## Requirements

- Python 3.8+
- `rich`

```bash
pip install -r requirements.txt
```

## How to run

```bash
git clone https://github.com/<your-user>/book-page-tracker.git
cd book-page-tracker
pip install -r requirements.txt
python book.py
```

## Usage

```python
l1 = Livro("10 coisas que eu aprendi", 20)   # book with 20 pages
l1.avançar_paginas(5)                         # turns 5 pages
l1.avançar_paginas(10)
l1.avançar_paginas(200)                       # more than what is left: stops on the last page
l1.avançar_paginas(5)                         # already at the end
```

## Example output

```
📖 Você acabou de abrir o livro '10 coisas que eu aprendi' que tem 20 páginas no total.
Você agora está na página 1
Pág2➡️ Pág3➡️ Pág4➡️ Pág5➡️ Pág6➡️ Você avançou 5 páginas e agora está na página 6
Pág7➡️ Pág8➡️ ... Pág16➡️ Você avançou 10 páginas e agora está na página 16
Pág17➡️ Pág18➡️ Pág19➡️ Pág20➡️ Você avançou 4 páginas e agora está na página 20
🚨 Você chegou ao final do livro '10 coisas que eu aprendi'
```

## Ideas for improvement

- Add a method to go back pages and to jump straight to a given page
- Add bookmarks and a reading-progress percentage
- Move the demo code under `if __name__ == "__main__":` so the class can be imported
- Read the title and the pages interactively with `input()`
