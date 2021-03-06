#!/usr/bin/env python3
# Copyright (c) Pelagicore AB 2016

import click
from qface.generator import FileSystem, Generator


def generate(input, output):
    system = FileSystem.parse_dir(input)
    generator = Generator(searchpath='templates')
    ctx = {'output': output, 'system': system}
    generator.write('{{output}}/modules.csv', 'modules.csv', ctx)


@click.command()
@click.option('--input', type=click.Path(exists=True))
@click.option('--output', type=click.Path(exists=True))
def runner(input, output):
    generate(input, output)

if __name__ == '__main__':
    runner()
