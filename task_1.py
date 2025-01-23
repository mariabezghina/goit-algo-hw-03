import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument("destination_dir", nargs='?', default="dist", help="Path to the destination directory. Defaults to 'dist'.")
    return parser.parse_args()

def copy_and_sort_files(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)

            if os.path.isdir(source_item):
                copy_and_sort_files(source_item, destination_dir)
            elif os.path.isfile(source_item):
                file_extension = os.path.splitext(item)[1].lstrip(".").lower() or "no_extension"
                destination_path = os.path.join(destination_dir, file_extension)

                os.makedirs(destination_path, exist_ok=True)
                shutil.copy2(source_item, destination_path)
                print(f"Copied: {source_item} -> {destination_path}")
    except Exception as e:
        print(f"Error processing {source_dir}: {e}")

def main():
    args = parse_arguments()
    source_dir = os.path.abspath(args.source_dir)
    destination_dir = os.path.abspath(args.destination_dir)

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    os.makedirs(destination_dir, exist_ok=True)
    copy_and_sort_files(source_dir, destination_dir)
    print(f"Files have been successfully copied and sorted into '{destination_dir}'")

if __name__ == "__main__":
    main()
