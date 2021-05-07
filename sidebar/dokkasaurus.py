import click
from sidebar.functions.dokka_function import sidebar_command

base_path = "./"

@click.command()
@click.argument('path')
@click.argument('root_name')
@click.option('-p', '--root-position', default=1, show_default=True)
@click.option('-o', '--output-path', default="./", show_default=True)
@click.option('--auto-generated', is_flag=True)
@click.option('--multi-module', is_flag=True)
@click.option('--filter-file')
def cli(path, root_name, root_position, output_path, auto_generated, multi_module, filter_file):
    """This command traverses the dokka directory and
    look for .md files to map the hierarchy of files
    """
    sidebar_command(
        path,
        root_name,
        root_position,
        output_path,
        auto_generated,
        multi_module,
        filter_file
    )
