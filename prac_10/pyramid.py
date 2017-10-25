def get_block_count_a(rows):
    """Using math"""
    return (rows * (rows + 1)) // 2

blocks = get_block_count_a(6)
print(blocks)


def get_block_count_b(rows):
    """using recursion"""
    if rows <= 0:
        return 0
    return rows + get_block_count_b(rows - 1)


blocks = get_block_count_b(6)
print(blocks)
