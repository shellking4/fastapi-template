from sqlalchemy import MetaData


def combine_metadata(*args):
    all_in_one_metadata = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(all_in_one_metadata)
    return all_in_one_metadata