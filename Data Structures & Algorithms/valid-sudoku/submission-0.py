class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        boxes_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == '.':
                    continue

                box_id = (row // 3, col // 3)

                if value in rows_dict[row] or value in cols_dict[col] or value in boxes_dict[box_id]:
                    return False

                rows_dict[row].add(value)
                cols_dict[col].add(value)
                boxes_dict[box_id].add(value)

        return True