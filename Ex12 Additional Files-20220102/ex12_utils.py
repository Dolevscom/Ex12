import boggle_board_randomizer
from typing import Tuple, List

def in_board_size(cord, max_r=4, max_c=4):
    r = cord[0]
    c = cord[1]
    if 0 <= r < max_r and 0 <= c < max_c:
        return True
    return False


def coord_legal_kernel(coord):
    final_cor = [coord]
    for i in range(2):
        for j in range(2):
            coor1 = coord[0] - i, coord[1] - j
            coor2 = coord[0] + i, coord[1] + j
            coor3 = coord[0] - i, coord[1] + j
            coor4 = coord[0] + i, coord[1] - j
            if coor1 not in final_cor and in_board_size(coor1):
                final_cor.append(coor1)
            if coor2 not in final_cor and in_board_size(coor2):
                final_cor.append(coor2)
            if coor3 not in final_cor and in_board_size(coor3):
                final_cor.append(coor3)
            if coor4 not in final_cor and in_board_size(coor4):
                final_cor.append(coor4)
    final_cor.remove(coord)
    return final_cor


def check_all_path(board, path, words):
    mx_rows = len(board)
    mx_cols = len(board[0])
    for i in path:
        i_index = path.index(i)
        if in_board_size(i, mx_rows, mx_cols) is False or path.count(i) > 1:
            return False
        if (i_index + 1) <= len(path) - 1:
            if path[i_index + 1] not in coord_legal_kernel(i):
                return False
    for word in words:
        if len(path) > len(word):
            return False
    return True


def is_valid_path(board, path, words):
    """
    A function that verify if the path is legal and decribe a word from 'words'
    :param board: list  lists of str (the letters for the game)
    :param path: list of of tuples (coordinates of a letter combination)
    :param words: all of the legal words in the cuurent game.
    :return:str of the legal word, None if its not legal.
    """
    fit_word = []
    if check_all_path(board, path, words) is False:
        return None
    for i in path:
        r = i[0]
        c = i[1]
        fit_word.append(board[r][c])
        test_word = "".join(fit_word)
        if test_word in words:
            return test_word
    return None


def next_possible_move(path_list):
    if path_list:
        leg_cor = coord_legal_kernel(path_list[-1])
        l3 = [x for x in leg_cor if x not in path_list]
        return l3
    return []


def all_possible_paths(board, n, words, current_path, path_list):
    current_word = ""
    # current_len = len(current_path)

    if not next_possible_move(current_path):
        return

    for cord in current_path:
        current_word += board[cord[0]][cord[1]]

    for direct in next_possible_move(current_path):
        current_len = len(current_path)

        if current_len == n and current_word in words:
            path_list.append(current_path)
            # print(f"(FOUND): word: {current_word}, current_path: {current_path}, path_list: {path_list}")
            all_possible_paths(board, n, words, current_path + [direct], path_list)
            return

        elif current_len > n:
            return

        elif current_len < n:
            all_possible_paths(board, n, words, current_path + [direct], path_list)


def paths_for_every_coord(n, board, words):
    mx_rows = len(board)
    mx_cols = len(board[0])
    path_list = []
    for i in range(mx_rows):
        for j in range(mx_cols):
            all_possible_paths(board, n, words, [(i, j)], path_list)
    return path_list


def find_length_n_paths(n, board, words):
    if n == 0:
        return []
    return paths_for_every_coord(n, board, words)


def word_vr_all_pos(board, n, words, current_path, path_list):
    current_word = ""
    # len_of_word = len(current_word)
    if not next_possible_move(current_path):
        return

    for cord in current_path:
        current_word += board[cord[0]][cord[1]]
    len_of_word = len(current_word)

    for direct in next_possible_move(current_path):
        # current_len = len(current_path)

        if len_of_word == n and current_word in words:
            path_list.append(current_path)
            # print(f"(FOUND): word: {current_word}, current_path: {current_path}, path_list: {path_list}")
            all_possible_paths(board, n, words, current_path + [direct], path_list)
            return

        elif len_of_word > n:
            return

        elif len_of_word < n:
            all_possible_paths(board, n, words, current_path + [direct], path_list)


def word_vr_for_every_cord(n, board, words):
    mx_rows = len(board)
    mx_cols = len(board[0])
    path_list = []
    for i in range(mx_rows):
        for j in range(mx_cols):
            word_vr_all_pos(board, n, words, [(i, j)], path_list)
    return path_list


def find_length_n_words(n, board, words):
    if n == 0:
        return []
    return word_vr_for_every_cord(n, board, words)


# def scr_vr_all_pos(board, n, words, current_path, word_n_path_dict):
#     current_word = ""
#     if not next_possible_move(current_path):
#         return
#
#     for cord in current_path:
#         current_word += board[cord[0]][cord[1]]
#     len_of_word = len(current_word)
#
#     for direct in next_possible_move(current_path):
#
#         if len_of_word == n and current_word in words:
#             word_n_path_dict[current_word] = current_path
#             # print(f"(FOUND): word: {current_word}, current_path: {current_path}, path_list: {path_list}")
#             all_possible_paths(board, n, words, current_path + [direct], word_n_path_dict)
#             return
#
#         elif len_of_word > n:
#             return
#
#         elif len_of_word < n:
#             all_possible_paths(board, n, words, current_path + [direct], word_n_path_dict)
#
# def scr_vr_for_every_cord(n, board, words):
#     mx_rows = len(board)
#     mx_cols = len(board[0])
#     word_n_path_dict = {}
#     for i in range(mx_rows):
#         for j in range(mx_cols):
#             word_vr_all_pos(board, n, words, [(i, j)], word_n_path_dict)
#     return word_n_path_dict
#
# def filter_by_score(word_n_path_dict):
#     filtered_list = []
#     duplicates = set(x.name for x in d if x.name in seen or seen.add(x.name))
#     for word in word_n_path_dict:
#         if word
#
# def max_score_paths(board, words):
#     pass




if __name__ == '__main__':
    my_board = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['QU', 'Q', 'U', 'A']]
    needed_path_length = 8
    my_words = ["ABC", "AFKHGJQU", "BAE", "AEI", "AFG"]
    possible_paths = []
    board1 = [['Q', 'Q', 'Q', 'Q'],
             ['D', 'O', 'G', 'Q'],
             ['Q', 'Q', 'Q', 'Q'],
             ['Q', 'Q', 'Q', 'Q']]
    word_dict = {'D': True, 'O': True, 'G': True}
    print(find_length_n_words(1, board1, word_dict))
        # expected = [[(1, 0)], [(1, 1)], [(1, 2)]]
        # assert sorted(find_length_n_words(1, board, word_dict)) == \
        #        sorted(expected)
    # all_possible_paths(my_board, needed_path_length, my_words, [(0, 0)], possible_paths)
    # print(find_length_n_paths(needed_path_length, my_board, my_words))
    # print(find_length_n_words(needed_path_length, my_board, my_words))
# board = [['a', 'b', 'c', 'd'], ['t', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
# path = [(0, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
# words = {'ab': True, 'cc': True, 'arg': True}
# [['R', 'E', 'J', 'E'], ['H', 'S', 'A', 'U'], ['W', 'O', 'W', 'I'], ['E', 'T', 'A', 'T']]
# board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
# words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
# print(find_length_n_paths(2, board, words))