#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for idx, weight in enumerate(weights):
        complement = limit - weight

        comp_idx = hash_table_retrieve(ht, complement)
        if comp_idx is not None:
            return idx > comp_idx and (idx, comp_idx) or (comp_idx, idx)

        hash_table_insert(ht, weight, idx)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
