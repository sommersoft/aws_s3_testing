#! /usr/bin/python3

# Output a simple file to test AWS S3 deployment

import argparse
import datetime

# Setup ArgumentParser
cmd_line_parser = argparse.ArgumentParser(
    description="Testing S3 Deploy.",
    prog="yes"
)
cmd_line_parser.add_argument(
    "output_file",
    help="Output log to the filename provided.",
    metavar="<OUTPUT FILENAME>",
)


if __name__ == "__main__":
    run_time = datetime.datetime.now().strftime("%d %B %Y, %I:%M%p")
    startup_message = [
        "Creating file for AWS S3 testing...",
        "Report Date: {}".format(run_time)
    ]
    cmd_line_args = cmd_line_parser.parse_args()
    output_filename = cmd_line_args.output_file

    startup_message.append(" - Report output will be saved to: {}".format(output_filename))

    print("\n".join(startup_message))

    with open(output_filename, "w") as f:
        f.write("This is your file.\n\nIt was created at: {}".format(run_time))

    print("File created.")
