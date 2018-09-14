<h2>DEKRIPSI ROT3 + KODE GESER</h2>
<form action="" method="post" >
<table class="form">
	<tr><td>Chipertext<br /><textarea rows="3" cols="50" name="chiper" ></textarea></td></tr>
	
	<tr><td><input type="submit" value="GO"/></td></tr>
</table>

</form>
	<?php 
if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
	if(!empty($_POST[chiper]))
	{
		$kata = $_POST[chiper];
		$data = str_split($kata);

		$i=0;
		foreach($data as $aaa){
			$ee = d_rot3($aaa);
			$r[$i]=$ee;
			$i++;
		}
		
		
		$dekrip = implode($r);
		
		$dd = d_geser($dekrip);
	
		echo"
		<h3>Chipertext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$_POST[chiper]</textarea></p>
		
		<h3>Plaintext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$dd</textarea></p>";
		
		
	}
	else
	{
		echo"<span style=\"color:#f00;\">Masukkan Chipertext...</span>";
	}
}
?>