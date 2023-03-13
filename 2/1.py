import os


def get_summary_rss(path: str):
    with open(os.path.join(path, 'output_file.txt'), 'r') as f:
        lines = f.readlines()[1:]
        result = 0
        for line in lines:
            result += int(line.split()[5])
        return f"Использованная память: {result} Б, {result // 1024} Кб,  {result // 1024**2} Мб"


path_to_file = os.path.abspath(os.path.join(''))
print(get_summary_rss(path_to_file))
