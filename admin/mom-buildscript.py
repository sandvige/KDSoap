#!/usr/bin/env python
#
# KDAB confidential
#
# This file is part of KDAB's internal build system setup. It is the
# build script for KD SOAP, which integrates it into the continuous
# integration system. 
#
# Author: Mirko Boehm, mirko.boehm@kdab.com

from core.helpers.BoilerPlate import BuildProject
from products.ProductBoilerPlate import ProductConfigurations

build, project = BuildProject( name = 'KD SOAP', version = '1.1.0-trunk', url = 'svn+ssh://svn.kdab.com/home/SVN-klaralv/products/kdsoap' )
configs = ProductConfigurations( project )
build.build()
