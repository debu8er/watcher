import argparse
from mymongo import (
    initialize_mongo_collection,
    get_status_changed,
    get_tech_changed,
    get_fresh,
    get_all,
    add_domain,
    delete_domain,
    get_full
    )
from update import update_project

def main():
    parser = argparse.ArgumentParser(description="Watch")
    parser.add_argument("-d", "--domain", help="domain input.")
    parser.add_argument("-m", "--method", choices=['add', 'delete', 'status', 'tech', 'fresh', 'all', 'full'], help="method", default="full")
    parser.add_argument("-up", "--update", action="store_true", help="update watcher to the latest released")
    args = parser.parse_args()

    if args.domain is None:
        print("Please provide a domain using the -d option.")
        return

    mongodb_uri = "mongodb://localhost:27017/"
    collection = initialize_mongo_collection(args.domain.split(".")[0], mongodb_uri)
    collection2 = initialize_mongo_collection("domains", mongodb_uri)

    if args.method == "fresh":
        get_fresh(collection)
    elif args.method == "status":
        get_status_changed(collection)
    elif args.method == "tech":
        get_tech_changed(collection)
    elif args.method == "all":
        get_all(collection)
    elif args.method == "add":
        add_domain(collection2, args.domain)
    elif args.method == "delete":
        delete_domain(collection2, args.domain)
    elif args.method == "full":
        get_full(collection)
    elif args.update:
        update_project("main")
if __name__ == "__main__":
    main(1)
