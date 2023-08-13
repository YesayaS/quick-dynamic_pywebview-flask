from natsort import natsorted

"""target = [col {suffix}]"""

old_folders = [
    1,
    3,
    2,
    4,
    5,
    "karage",
    "col 0",
    "col 3",
    "col 2",
    "col 4",
    "col 5",
    "col 6",
    "col 7",
]
new_folder = ["col {}".format(suffix) for suffix in range(len(old_folders))]
# # print(natsorted(old_folders))


def method_two():
    folders = old_folders
    for e, folder in enumerate(folders):
        suffix = 0
        while "col {}".format(suffix) in old_folders:
            suffix += 1
        folders[e] = "col {}".format(suffix)
        assert folders[e] in old_folders
        # suffix += 1

    natsorted(folders)
    # print(folders)


def method_one():
    set_old_items = set(old_folders)
    set_new_items = set(new_folder)

    true_format = list(set_old_items.intersection(set_new_items))
    true_format = natsorted(true_format)

    false_format = [item for item in old_folders if item not in set_new_items]
    false_format = natsorted(false_format)

    # print(old_folders)
    # print(true_format)
    # print(false_format)

    folders = true_format + false_format
    # folders = natsorted(folders)
    print(folders)

    for e, folder in enumerate(folders):
        if folders[e] == "col {}".format(e):
            continue
        suffix = 0
        while "col {}".format(suffix) in folders:
            suffix += 1
        print("col {}".format(suffix), folders)
        assert "col {}".format(suffix) not in folders
        folders[e] = "col {}".format(suffix)

    print(folders)


method_one()
# method_two()


# new_format = [item for item in new_items if item not in old_items]
# to_rename = [item for item in old_items if item not in new_items]
