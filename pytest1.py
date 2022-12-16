import pytest

def py(x):
    return x+5

def main():
    assert py(0)==5
main()