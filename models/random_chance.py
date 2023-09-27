# Adapted from: https://github.com/lupantech/ScienceQA/blob/main/models/run_gpt3.py

import argparse
import json
import random
from typing import List

from utils import load_data, get_result_file, new_acc, compute_acc

parser = argparse.ArgumentParser()
parser.add_argument('--data_root', type=str, default='data/maplm_v0.1')
parser.add_argument('--output_dir', type=str, default='runs')
parser.add_argument('--test_split', type=str, default='test')
parser.add_argument('--test_number', type=int, default=-1, help='Number of test frames to run (default: -1, all)')
parser.add_argument('--exp_label', type=str, default='exp_random', help='Experiment label')
parser.add_argument('--random_seed', type=int, default=1, help='Random seed')
parser.add_argument('--debug', action='store_true', help='Debug mode')

args = parser.parse_args()

results = dict(
    question_overall=new_acc(),
    frame_overall=new_acc(),
)

if __name__ == "__main__":
    print('===== Input Arguments =====')
    print(json.dumps(vars(args), indent=4, sort_keys=True))
    load_data(args)

    random.seed(args.random_seed)

    frames, frame_ids = load_data(args)
    result_file_name = get_result_file(args)

    for i, frame_id in enumerate(frame_ids):
        frame = frames[frame_id]

        image = frame['image']
        qas = frame['qa']

        corrects = []
        for j, qa in enumerate(qas):
            if qa['task'] != 'closed choice':
                continue
            question = qa['question']
            choices: List[str] = qa['choices']
            true_answer: int = qa['answer']
            random_guess: int = random.randint(0, len(choices) - 1)

            if question not in results:
                results[question] = new_acc()

            correct = bool(random_guess == true_answer)
            corrects.append(correct)

            results[question]['total'] += 1
            results[question]['correct'] += int(correct)
            results['question_overall']['total'] += 1
            results['question_overall']['correct'] += int(correct)

        results['frame_overall']['total'] += 1
        results['frame_overall']['correct'] += int(all(corrects))

    print('===== Results =====')
    acc_dict = compute_acc(results)
    print(json.dumps(acc_dict, indent=4, sort_keys=True))
    print(json.dumps(results, indent=4, sort_keys=True))


