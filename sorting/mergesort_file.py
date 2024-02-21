import heapq
import os.path
import random
import array

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('-c', '--count', type=click.IntRange(256, clamp=True), default=256)
def makefile(count):
    filename = 'in.file'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'wb') as fp:
        for i in range(count):
            fp.write(
                array.array('I', [random.randint(0, 2048)]).tobytes()
            )


@cli.command()
@click.option('-f', '--infile', default='in.file', type=str)
@click.option('-o', '--outfile', default='out.file', type=str)
@click.option('-c', '--chunksize', default=16, type=click.IntRange(16, 2048))
def sort(infile, outfile, chunksize):
    if os.path.exists('chunks') and os.path.isdir('chunks'):
        ...
    else:
        os.makedirs('chunks')

    def get_chunk(fp, size: int):
        mem = array.array('I')
        mem.frombytes(fp.read(size * 4))
        return mem

    def chunk_generator(fp, size: int):
        while chunk := get_chunk(fp, size):
            yield chunk

    print(f'generate sorted chunks/*.file with up to {chunksize} items.', end=' ')
    with open(infile, 'rb') as fp:
        for cid, chunk in enumerate(chunk_generator(fp, chunksize)):
            f_name = f'chunks/{cid}.file'
            with open(f_name, 'wb') as out:
                mem = array.array('I', sorted(chunk))
                out.write(mem.tobytes())
                # print(f'{cid:<10}{f_name:<20}', f'sorted chunk with {len(mem)} items')

    print('Done.')

    def fp_reader(infile: str):
        with open(infile, 'rb') as fp:
            while data := fp.read(4):
                mem = array.array('I')
                mem.frombytes(data)
                yield mem[0]

    print(f'merge all {cid+1} chunks info {outfile}', end=' ')
    with open(outfile, 'wb') as fp:
        for w in heapq.merge(*[fp_reader(f'chunks/{i}.file') for i in range(cid + 1)]):
            fp.write(
                array.array('I', [w]).tobytes()
            )
    print('Done.')

    print(f'test {outfile}.', end=' ')
    fp = fp_reader(outfile)
    old = next(fp)
    for new in fp:
        assert old <= new
        old = new
    print('Done.')

if __name__ == '__main__':
    cli()
