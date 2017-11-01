#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from setuptools import setup, find_packages
import shutil
import sys
import os


__author__ = "Yun Rock Qu"
__copyright__ = "Copyright 2016, Xilinx"
__email__ = "yunq@xilinx.com"


GIT_DIR = os.path.dirname(os.path.realpath(__file__))


def fill_notebook_symlinks():
    symlinks_folder = '/home/xilinx/jupyter_notebooks/symlinks'
    if os.path.exists(symlinks_folder):
        shutil.rmtree(symlinks_folder)
    shutil.copytree(os.path.join(GIT_DIR, 'symlinks'),
                    symlinks_folder)


if len(sys.argv) > 1 and sys.argv[1] == 'install':
    fill_notebook_symlinks()


setup(name='pynq_debug',
      version='1.0',
      description='PYNQ debug package',
      author='Yun Rock Qu',
      author_email='yunq@xilinx.com',
      url='https://github.com/yunqu/PYNQ-Debug-Notebooks',
      packages=find_packages(),
      download_url='https://github.com/yunqu/PYNQ-Debug-Notebooks'
      )