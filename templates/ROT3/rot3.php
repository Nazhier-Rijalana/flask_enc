<h2>ROT3</h2>
<form action="" method="post" >
<table class="form">
	<tr><td>Plaintext<br /><textarea rows="3" cols="50" name="plain" ></textarea></td></tr>
	<tr><td><input type="submit" value="GO"/></td></tr>
</table>

</form>
	<?php 
if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
	if(!empty($_POST[plain]))
	{
		$kata = $_POST[plain];
		$data = str_split($kata);

		$i=0;
		foreach($data as $aaa){
			$ee = rot3($aaa);
			$r[$i]=$ee;
			$i++;
		}
		
		
		$rot3 = implode($r);
		echo"<h3>Plaintext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$kata</textarea></p>
		<h3>Chipertext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$rot3</textarea></p>
	
	
	
	
	";
	}
	else
	{
		echo"<span style=\"color:#f00;\">Masukkan Plaintext...</span>";
	}
}
?>