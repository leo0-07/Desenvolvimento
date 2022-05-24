#!/usr/bin/perl
    use warnings;
    use strict;
    use Switch;
    package MyBot;
    use base qw( Bot::BasicBot );
     my $result='';
     my $filename = '';
     my $fh = '';
     my $row = '';
     my $msg = "";
    # the 'said' callback gets called when someone says something in
    # earshot of the bot.
    sub said {
      $filename="";
      $msg="";
      my ($self, $message) = @_;
#      $self->say(
#        channel => "#capacitation",
#        body => "$message->{who} said '$message->{body}' in $message->{channel}",);
switch ($message->{body}) {
case "cap" {
$msg = "";
$filename = 'capacitation.txt';
}
case 1{
$msg = "";
$filename='cap/1.txt';
}
case 2 {
$msg = "";
$filename='cap/2.txt';
}
case 3 {
$msg="";
$filename='cap/3.txt';
}
case 4 {
$msg = "";
$filename ='cap/4.txt';
}
case 5 {
$msg = "";
$filename ='cap/5.txt';
}
case 6 {
$msg = "";
$filename = 'cap/6.txt';
}
case 7 {
$msg = "";
$filename = 'cap/7.txt';
}
case 8 {
$msg = "";
$filename = 'cap/8.txt';
}
case 9 {
$msg = "";
$filename = 'cap/9.txt';
}
case 10 {
$msg = "";
$filename = 'cap/10.txt';
}
case 11 {
$msg = "";
$filename = 'cap/12.txt';
}
case 12 {
$msg = "";
$filename = 'cap/12.txt';
}
case 13 {
$msg = "";
$filename = 'cap/13.txt';
}
case 14 {
$msg = "";
$filename = 'cap/14.txt';
}
case 15 {
$msg = "";
$filename = 'cap/15.txt';
}
case 16 {
$msg = "";
$filename = 'cap/16.txt';
}
case 17 {
$msg = "";
$filename = 'cap/17.txt';
}
case 18 {
$msg = "";
$filename = 'cap/18.txt';
}
case 19 {
$msg = "";
$filename = 'cap/19.txt';
}
}
open my $handle, '<:encoding(UTF-8)', $filename;
while ($row = <$handle>){
$msg.=$row;
}
binmode(STDOUT, ":utf8");
print "$msg\n";
$self->say(
channel=>"#capacitation-sl",
body=>"$msg",);
close $handle;

      return undef;
}
    sub help {"Eu sou o Bot de suporte do canal." }
    MyBot->new(
      server => 'irc.freenode.net',
      channels => [ '#Capacitation-sl' ],
      nick => 'alone-dust',
    )->run();
