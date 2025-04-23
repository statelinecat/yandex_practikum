from sys import stdin

lines = []
try:
    for line in stdin:
        lines.append(line)
except KeyboardInterrupt:  # Если пользователь нажмет Ctrl+C
    pass
print(lines)