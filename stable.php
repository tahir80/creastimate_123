<?php 
//$data ='{"numOfUniqueWords" :' . $_POST["numOfUniqueWords"] . ', "numOfDifficultWords" :' . $_POST["numOfDifficultWords"] . ', "smartHomeXP" :' . $_POST["smartHomeXP"] . ', "familySize" :' . $_POST["familySize"] . '}';
$_POST["numOfUniqueWords"] =1;
$_POST["numOfDifficultWords"] =2;
$_POST["smartHomeXP"] =12;
$_POST["familySize"] =5;

$data =$_POST["numOfUniqueWords"] . ' ' . $_POST["numOfDifficultWords"] . ' ' . $_POST["smartHomeXP"] . ' ' . $_POST["familySize"];
//$command ='python stable.py ' . $data;
$command ='python /Library/WebServer/Documents/scenariot/stable.py ' . $data;
//$command ='python /Library/WebServer/Documents/scenariot/t.py ';
echo $command;
//$command = escapeshellcmd($c);
//$output = exec($command, $o, $ret);
$output = system($command, $ret);
echo "<hr>o:".$output.  " r:". $ret;
//print_r($o);

?>