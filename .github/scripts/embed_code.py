import re
import os
from pathlib import Path

def embed_code_in_readme(readme_path='README.md'):
    """Заменяет пустые блоки кода на содержимое файлов"""
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ищем паттерн: ```python:path/to/file.py\n\n```
    pattern = r'```(\w+):([^\n]+)\n\n```'
    
    def replace_block(match):
        language = match.group(1)
        file_path = match.group(2).strip()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as code_file:
                code = code_file.read()
            
            # Убираем лишние пустые строки в начале и конце
            code = code.strip('\n')
            
            # Возвращаем блок с кодом
            return f'```{language}\n{code}\n```'
        except FileNotFoundError:
            print(f"⚠️ Файл не найден: {file_path}")
            return match.group(0)  # оставляем как было
    
    new_content = re.sub(pattern, replace_block, content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README.md обновлён!")
    else:
        print("ℹ️ Изменений не требуется")

if __name__ == "__main__":
    embed_code_in_readme()