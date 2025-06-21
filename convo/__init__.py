import argparse
import json
import os
from datetime import datetime, timezone
from collections import Counter


def handle_log(text, tags):
    os.makedirs("data", exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "text": text,
        "tags": tags
    }
    log_path = "data/logs.json"
    if os.path.exists(log_path):
        try:            
            with open(log_path, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    else:
        logs = []
    logs.append(entry)
    with open(log_path, "w") as f:
        json.dump(logs, f, indent=4)


def handle_summary():
    os.makedirs("data", exist_ok=True)
    log_path = "data/logs.json"
    stop_path = "data/stopwords.json"
    
    with open(log_path, "r") as f:
        logs = json.load(f)

    if os.path.exists(stop_path):
        with open(stop_path, "r") as f:
            stopwords = json.load(f)
    else:
        stopwords = ["the", "to", "and", "a", "of", "in", "on", "about", "with", "as", "along"]
    
    all_words = []
    for entry in logs:
        words = entry["text"].lower().split()
        all_words.extend(words)
    
    filtered_words = [w for w in all_words if w not in stopwords]
    top_words = Counter(filtered_words).most_common(5)
    
    print("\nConvo Summary\n" + "-"*30)
    print(f"Total logs: {len(logs)}")
    print("Most common words:")
    for word, count in top_words:
        print(f"- {word}: {count}")
    
    choice = int(input("\nType 1 if you don't want to see some words again: "))
    if choice == 1:
        new_stop_words = input("\nEnter the words here with a space in between: ").lower().split()
        stopwords.extend(new_stop_words)
        stopwords = list(set(stopwords))
        with open(stop_path, "w") as f:
            json.dump(stopwords, f, indent=4)
        print("Saved")

def handle_filter(tag):
    logs_path = "data/logs.json"
    if not os.path.exists(logs_path):
        print("No logs found.")
        return
    
    with open(logs_path, "r") as f:
        logs = json.load(f)
    a=0

    print(f"\nLogs tagged with: {tag}\n" + "-"*30)
    for entry in logs:
        if tag in entry["tags"]:
            print(f"[{entry['timestamp']}] {entry['text']}")
            a+=1
    if a == 0:
        print("No logs found.")


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    
    log_parser = subparsers.add_parser("log", help="Log a conversation")
    log_parser.add_argument("text", help="The conversation text to log")
    log_parser.add_argument("--tags", nargs="*", default=[], help="Optional tags for the log entry")

    summary_parser = subparsers.add_parser("summary", help="Show summary of logs")

    filter_parser = subparsers.add_parser("filter", help="Filter logs by tag")
    filter_parser.add_argument("--tag", required=True, help="Tag to search logs for")

    args = parser.parse_args()

    if args.command == "log":
        handle_log(args.text, args.tags)
    elif args.command == "summary":
        handle_summary()
    elif args.command == "filter":
        handle_filter(args.tag)
