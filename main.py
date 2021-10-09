#!/usr/bin/python3
import argparse
from todo import Todo

parser = argparse.ArgumentParser(description='Simple to-do lists')

# Instantiate mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("--list", action="store_true",
                   help="lists out all tasks")
group.add_argument("--add", nargs="+", type=str, dest="add_list",
                   help="add new task")
group.add_argument("--done", nargs="+", type=int, dest="done_list",
                   help="mark task as completed")
group.add_argument("--remove", nargs="+", type=int, dest="remove_list",
                   help="remove a task")
group.add_argument("--sort", action="store_true",
                   help="sort completed and uncompleted tasks")

args = parser.parse_args()

# Instantiate todo instance
todo = Todo()

# Execute action depends on arguments
if args.list:
    todo.list()
elif args.add_list:
    todo.add(args.add_list)
elif args.done_list:
    todo.done(args.done_list)
elif args.remove_list:
    todo.remove(args.remove_list)
elif args.sort:
    todo.sort()
else:
    print("try -h for for info")
