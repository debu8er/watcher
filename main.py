import argparse
from mymongo import (
    initialize_mongo_collection,
    get_status_changed,
    get_tech_changed,
    get_fresh,
    get_all_sub,
    add_domain,
    remove_domain,
    filter_status,
    filter_tech,
    get_full
    )
from update import update_project

def main():
    parser = argparse.ArgumentParser(description="Watch")
    parser.add_argument("-d", "--domain", help="domain input.")
    parser.add_argument("-a", "--add", help="add new domain", action="store_true")
    parser.add_argument("-r", "--remove", help="remove domain", action="store_true")
    parser.add_argument("-s", "--status", help="filter by status.")
    parser.add_argument("-t", "--tech", help="filter by technologies.")
    parser.add_argument("-sc", "--status-changed", help="filter by status changed", action="store_true")
    parser.add_argument("-tc", "--tech-changed", help="filter by technologies.", action="store_true")
    parser.add_argument("-f", "--fresh", help="filter by fresh", action="store_true")
    parser.add_argument("-as", "--all-sub", help="get all sub in result.", action="store_true")
    parser.add_argument("-fr", "--full-result", help="get full result.", action="store_true")

    args = parser.parse_args()

    print(args)

    if args.domain is None:
        print("Please provide a domain using the -d option.")
        return

    mongodb_uri = "mongodb://localhost:27017"
    collection = initialize_mongo_collection(args.domain.split(".")[0], mongodb_uri)
    collection2 = initialize_mongo_collection("domains", mongodb_uri)
    
    if args.domain and not any([args.add, args.remove, args.status, args.tech, args.status_changed, args.tech_changed, args.fresh, args.full_result]):
        get_full(collection)   

    if args.add:
        add_domain(collection2, args.add)
    elif args.remove:
        remove_domain(collection2, args.remove)
    elif args.fresh:
        get_fresh(collection)
    elif args.status_changed:
        get_status_changed(collection)
    elif args.tech_changed:
        get_tech_changed(collection)
    elif args.all_sub:
        get_all_sub(collection)
    elif args.full_result:
        get_full(collection)
    elif args.status:
        filter_status(collection, int(args.status))
    elif args.tech:
        filter_tech(collection, args.tech)
if __name__ == "__main__":
    main()
