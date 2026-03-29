import re
import os
import sys
from pathlib import Path

def embed_code_in_readme(readme_path='README.md'):
    """Заменяет пустые блоки кода на содержимое файлов"""
    
    if not os.path.exists(readme_path):
        print(f"❌ Файл {readme_path} не найден!")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'```(\w+):([^\n]+)\n*```'
    
    matches = re.findall(pattern, content, flags=re.MULTILINE)
    print(f"🔍 Найдено блоков для вставки: {len(matches)}")
    
    if not matches:
        print("⚠️ В README.md нет блоков вида ```python:path/to/file.py\\n\\n```")
        return False
    
    def replace_block(match):
        language = match.group(1)
        file_path = match.group(2).strip()
        
        print(f"📄 Обработка файла: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"   ❌ Файл не существует: {file_path}")
            return match.group(0)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as code_file:
                code = code_file.read()
            
            code = code.rstrip('\n')
            print(f"   ✅ Вставлено {len(code)} символов")
            
            return f'```{language}\n{code}\n```'
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return match.group(0)
    
    new_content = re.sub(pattern, replace_block, content, flags=re.MULTILINE)
    
    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README.md обновлён!")
        return True
    else:
        print("ℹ️ README.md не изменился")
        return False

if __name__ == "__main__":
    print("🚀 Запуск скрипта встраивания кода...")
    print(f"📁 Текущая директория: {os.getcwd()}")
    print(f"📁 Содержимое: {os.listdir('.')}")
    
    success = embed_code_in_readme()
    sys.exit(0 if success else 1)