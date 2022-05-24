#!/usr/local/bin/perl

my ($fval, $lval) = @ARGV;
my $result = 0;
print $fval . "\n";
for (my $i = 0; $i <  ($fval +  1); $i++)
{
my $cvalue = 0;
my $nc = "" . $i;
$sval = length($nc);
	for (my $t = 0; $t < ($sval); $t++)
	{
		$tvalue = substr($nc, $t, 1);
#		print "dígito: $tvalue \n";
		$cvalue += $tvalue;
	if ($cvalue == $lval)
		{
		$result+= 1;
		}
	}
}
	print "valor a ser localizado: $lval \n";
print "encontrados: $result" . "\n";

