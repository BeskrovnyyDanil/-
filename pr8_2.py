#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pr8_2.py
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


n=2
m=3
a=[[5,2,3,5],[9,8,6]]
for i in a:
	print(i)
max=a[0][0]
for i in range(n):
	for j in range(n):
		if  max<a[i][j]:
			 max=a[i][j]
print('Максимальное значение: ',max)
for i in range(n-1):
	for j in range(m-1):
		if a[i][j]<a[i+1][j]:
			a[i],a[j]=a[j],a[i]
for j in range(m-1):
	for i in range(n-1):
		if a[i][j]<a[i][j+1]:
			a[i],a[j]=a[j],a[i]
for i in a:
	print(i)
