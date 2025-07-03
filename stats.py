import collections

def count_words(text):
    words = text.split()
    return len(words)

def count_character_stats(text):
    result = collections.defaultdict(int)
    for char in text:
        result[char.lower()] += 1
    return result

def create_stat_report(stats):
    result = []
    for char, count in stats.items():
        row = {"char": char, "count": count}
        result.append(row)

    def sort_fn(x):
        return x["count"]

    result.sort(reverse=True, key=sort_fn)
    return result
