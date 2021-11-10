def do_undo(undo_lst, redo_lst, current_list):
    """
    :param undo_lst:
    :param redo_lst:
    :return:
    """
    if undo_lst:
        redo_lst.append(current_list)
        return undo_lst.pop()
    return None


def do_redo(undo_lst, redo_lst, current_list):
    """
    :param undo_lst:
    :param redo_lst:
    :return:
    """
    if redo_lst:
        undo_lst.append(current_list)
        return redo_lst.pop()
    return None
