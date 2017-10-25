# def get_block_count(rows):
#     return (rows * (rows + 1)) / 2
#
# blocks = get_block_count(5)
# print(blocks)


def get_block_count(rows):
    if rows <= 0:
        return 0
    return rows + get_block_count(rows - 1)


blocks = get_block_count(6)
print(blocks)
