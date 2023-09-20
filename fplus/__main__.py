import click
from .runner import _run
from os import system
@click.group()
def main(): pass

@main.command()
@click.argument("file", type=click.File("r"))
def run(file):
    system("clear")
    click.echo(_run(file.read()))

@main.command
def test():
    click.echo("Hello, World!")
    
if __name__ == "__main__":
    main()