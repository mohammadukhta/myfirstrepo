import subprocess
from pathlib import Path

# проверка существования файла с паролем
path = Path("update1.txt")
    
print("Файл существует" if path.exists() else "Файл не существует")