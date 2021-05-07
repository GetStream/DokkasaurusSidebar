from sidebar.functions.dokka_function import sidebar_command
import sys

sidebar_command(
    path=sys.argv[1],
    root_name=sys.argv[2],
    root_position=sys.argv[3],
    output_path=sys.argv[4],
    auto_generated=eval(sys.argv[5]),
    multi_module=eval(sys.argv[6]),
    filter_file=sys.argv[7]
)
