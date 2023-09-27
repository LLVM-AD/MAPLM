import json
import os
from typing import Dict


def load_data(args):
    problems = json.load(open(os.path.join(args.data_root, 'problems.json'), 'r'))
    pid_splits = json.load(open(os.path.join(args.data_root, 'pid_splits.json'), 'r'))

    frame_ids = pid_splits[args.test_split]
    frame_ids = frame_ids[:args.test_number] if args.test_number > 0 else frame_ids
    print(f'Number of test frames: {len(frame_ids)}\n')

    return problems, frame_ids


def get_result_file(args):
    result_file = f"{args.data_root}/{args.exp_label}_seed_{args.random_seed}.json"
    return result_file


def new_acc():
    return {
        'total': 0,
        'correct': 0
    }


def compute_acc(results: Dict[str, Dict[str, int]]):
    acc_dict = {}
    for metric in results:
        acc_dict[metric] = results[metric]['correct'] / results[metric]['total'] * 100
    return acc_dict
