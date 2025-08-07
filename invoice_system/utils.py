def paginate(items, page_size=10):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]