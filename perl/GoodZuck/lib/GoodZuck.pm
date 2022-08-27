#!/usr/bin/perl
# Copyright 2022 Leonardo de Araújo Lima
#
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see http://www.gnu.org/licenses/.
#
#
#
#
package GoodZuck;
use Moose;
 
 has 'id' => (is => 'rw');
 
 has 'nome' => (is => 'rw');
 
 has 'tipo' => (is => 'rw');
 
 sub show()
 {
 my ($self) = @_;
 print $self->id . "\n" . $self->nome . "\n" . $self->tipo . "\n";
 }
1;
