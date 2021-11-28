#!/usr/bin/python3
#
#
# Author: Rajesh Prashanth
# Date: Fri Nov 26 07:17:46 IST 2021
#
#--------------------------------------------
import os
import sys
import ase.io.espresso as espresso
import ase.io.vasp as vasp

def pwi2poscar(pw_input_file,vasp_poscar):
    try:
        fin = open (pw_input_file, 'r')
        fout = open (vasp_poscar, 'w')
        #
        data = espresso.read_espresso_in(pw_input_file)
        vasp.write_vasp(vasp_poscar,data,direct=True,long_format=True, vasp5=True)
        #
    except IOError as e:
    	print(e)
    	exit(-1)

def pwo2poscar(pw_output_file,vasp_poscar):
    try:
        fin = open (pw_output_file, 'r')
        fout = open (vasp_poscar, 'w')
        #
        data = espresso.read_espresso_out(pw_output_file,index=slice(None), results_required=True)
        #
        print (data.gi_frame())
        #vasp.write_vasp(vasp_poscar,data,direct=True,long_format=True, vasp5=True)
        #
    except IOError as e:
    	print(e)
    	exit(-1)


pwi2poscar("Li3Sb.qe.std_prim.in","pwi2poscar.out")
pwo2poscar("Li3Sb.qe.std_prim.out","pwo2poscar.out")
