<?php 
$n=range(0, 100); 
foreach ($n as $a) 
{
echo $a;
if($a%3==0) 
{
$sum+=$a;
} 
echo $a;
}
?>

