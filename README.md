# QR Code generation

This is a simple demonstration of creating QR code files with two different 
libraries.

## qrcode library

[qrcode repository](https://github.com/lincolnloop/python-qrcode)

This is listed as a pure Python library.  By default, it uses Pillow to 
generate png files.  The images are created in memory as pillow images.  
Fortunately, pillow has a save function for its images so writing it out as 
binary file is not a problem.  SVG images can also be produced with this 
library.  The png files in the work directory were generated with this 
library. 

## pyqrcode library

[pyqrcode repository](https://github.com/mnooner256/pyqrcode)

This is also listed as a pure Python library.  It can also generate either 
png or svg files.  I chose to use the svg option in this demo.  Unlike 
qrcode, this library writes the QR code image directly to a file name that 
is specified at the time of image generation.  The svg files in the work 
directory were generated with this library. 

## Common traits

Both libraries allow one to specify a "version" that identifies how big the 
blocks that make up the QR code are supposed to be.  There are also four 
levels of redundancy that can be specified.  

Both libraries have fairly extensive documentation about how to use each 
library and refer to options given in the QR code specification itself.

## Project Background

This project is a "proof-of-concept" and does not attempt to evaluate the 
merits of either library.  Folks are welcome to use this as a starting point
for their own investigations.  If the docuemntation is insufficient to 
answer your questions, please direct inquiries to the maintainer of the 
respective library.

These programs were run with Python 3.7 and include some boilerplate code 
that I use as a starter for my programs.  They expect to have the work 
directory set as their working directory when run.

As noted in the license file, this project is copywrited under the MIT 
license. 
