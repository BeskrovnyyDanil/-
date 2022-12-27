#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  без_имени.py
#  
#  Copyright 2022 Unknown <stud@comp-424-01.localdomain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import random
n=int(input('Введите кол-во строк и столбцов: '))
h=('')
matrix=[[random.randrange(10) for i in range(n)] for j in range(n)]
for elem in matrix:
	print(elem)
for k in range(0,n-1):
	for l in range(k+1,n):
		if matrix[k][l]!=matrix[l][k]:
			h=('False')
			break
if h!=('False'):
	print('Матрица симметрична')
else:
	print('Матрица несимметрична')
