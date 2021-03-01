#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:38:14 2021

@author: Ghassan Dabane
"""
from __future__ import absolute_import
from sequence import Sequence
from burros_wheeler import BurrosWheeler
from huffman import HuffmanTree

class Decoder:

    def __init__(self: object, path: str) -> None:

        self.path = path[:-4]
        self.seq = Sequence(path)
        self.huffman_decode = Sequence(self.path + '_debwt.txt')
        self.bwt_decode = Sequence(self.path + '_decompressed.txt')

    def decode_huffman(self: object) -> None:

        seq = self.seq.read_bytes()
        header = seq[:seq.index('\n')]
        uni = seq[seq.index('\n')+1:]


        re_codes = HuffmanTree.header_to_codes(header)


        binary = HuffmanTree.unicode_to_binstr(uni)

        padding = int(re_codes['pad'])
        no_pad_bin = HuffmanTree.remove_padding(binary, padding)


        tf = HuffmanTree.binstr_to_seq(no_pad_bin, re_codes)
        self.huffman_decode.write(tf)


    def decode_bwt(self: object) -> None:

        seq = self.huffman_decode.read()
        bwm = BurrosWheeler.reconstruct_bwm(seq)


        original_seq = BurrosWheeler.decode_bwt(bwm)
        self.bwt_decode.write(original_seq)
        
    def full_protocol(self: object) -> None:
        pass

###########test
"""
RandomSequence('../data/randseq2kb.txt', 2000).generate()
yo = Encoder('../data/randseq2kb.txt')
pf = yo.encode_bw()
next(pf)
pft = yo.encode_huffman()
next(pft)
yo = Decoder('../data/randseq2kb_compressed.txt')
pf = yo.decode_huffman()
next(pf)
pft = yo.decode_bwt()
next(pft)
"""